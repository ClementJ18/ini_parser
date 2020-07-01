from .enums import *
from .utils import is_end

import re
import sys
import numbers

def get_obj(name):
    return getattr(sys.modules[__name__], name, None)
    
class IniObject:
    def string(self, name, value):
        setattr(self, f"_{name}", value)
        setattr(self.__class__, name, property(lambda x: self.parser.get_string(getattr(self, f"_{name}"))))
        
    def macro(self, name, value):
        setattr(self, f"_{name}", value)
        setattr(self.__class__, name, property(lambda x: self.parser.get_macro(getattr(self, f"_{name}"))))
        
    def reference(self, name, value, dict_name):
        setattr(self, f"_{name}", value)
        setattr(self.__class__, name, property(lambda x: self.parser.get(dict_name, getattr(self, f"_{name}"))))

class Armor:
    def __init__(self, name, damage_types, parser):
        """
        
        name : str
        DEFAULT : float
        flanked : float
        scalar : float
        
        SEE DAMAGETYPES FOR THE RESTS
        
        """
        self.parser = parser
        
        self.name = name
        self.DEFAULT = damage_types.pop("DEFAULT", 1)
        self.flanked = damage_types.pop("FlankedPenalty", 1)
        self.scalar = damage_types.pop("DamageScalar", 1)
        
        for damage in DamageTypes.__members__:
            setattr(self, damage, damage_types.pop(damage, self.DEFAULT))
            
    def __repr__(self):
        return f"<ArmorSet {self.name}>"
        
    @classmethod
    def parse(cls, parser, name, lines):
        armorset = {}
        line = next(lines)
        
        while not is_end(line):
            damage, percent = line.split("=")
            if damage.strip() in ["FlankedPenalty", "DamageScalar"]:
                armorset[damage] = float(percent.replace("%", "").strip())/100
            else:
                damage, percent = percent.split()
                armorset[damage.strip()] = float(percent.replace("%", "").strip())/100
            
            line = next(lines)
            
        parser.armorsets[name] = cls(name, armorset, parser)
        
        
class CommandSet:
    """
    
    name : str
    initial : int
    commandbuttons : Dict[int : str]
    
    
    """
    def __init__(self, name, initial, commandbuttons, parser):
        self.parser = parser
        
        self.name = name
        self.initial = initial
        self.commandbuttons = commandbuttons
        
    def __repr__(self):
        return f"<CommandSet {self.name} len={len(self.commandbuttons)}>"
        
    def as_list(self):
        size = max(list(self.commandbuttons.keys()))
        return [self.commandbuttons[index] if index in self.commandbuttons else None for index in range(size)] 
        
    def initial_visible(self):
        visible = sorted(list(self.commandbuttons.items()), key=lambda x: x[0])[:self.initial]
        return {x[0]: x[1] for x in visible}
    
    def get_button(self, index):
        return self.parser.get_button(self.commandbuttons[index])
        
    @classmethod
    def parse(cls, parser, name, lines):
        line = next(lines)
        data = {}
        initial = None
        
        while not is_end(line):
            if line.startswith("InitialVisible"):
                initial = int(line.split("=")[1])
            else:
                index, button = line.split("=")
                data[int(index)] = button.strip()
                
            line = next(lines)
            
        parser.commandsets[name] = cls(name, initial, data, parser)
    
class CommandButton(IniObject):
    """
    Command buttons are buttons that we place on the in game UI to create the context sensitive command sets.
    
    ButtonBorderType : ButtonBorderTypes
    
    CommandTrigger : CommandButton
    ToggleButtonName : CommandButton
    
    Command : CommandTypes
    
    CursorName : Cursor
    InvalidCursorName : Cursor
    RadiusCursorType : Cursor
    
    FlagsUsedForToggle : Flags
    ButtonImage : Image
    AffectsKindOf : KindsOf
    Options : List[Options]
    Stances : List[Stances]
    CreateAHeroUIAllowableUpgrades : List[Upgrade]
    
    AutoAbilityDisallowedOnModelCondition : ModelConditions
    DisableOnModelCondition : ModelConditions
    EnableOnModelCondition : ModelConditions
    
    Object : Object
    Science : Science
    
    UnitSpecificSound : Sound
    SetAutoAbilityUnitSound : Sound
    
    SpecialPower : SpecialPower
    
    DescriptLabel : String
    TextLabel : String
    LacksPrerequisiteLabel : String
    ConflictingLabel : String
    PurchasedLabel : String
    CreateAHeroUIPrerequisiteButtonName : String
    
    Upgrade : Upgrade
    NeededUpgrade : Upgrade
    
    WeaponSlot : WeaponSlots
    WeaponSlotToggle1 : WeaponSlots
    WeaponSlotToggle2 : WeaponSlots
    
    DoubleClick : bool
    Radial : bool
    InPalantir : bool
    AutoAbility : bool
    TriggerWhenReady : bool
    ShowButton : bool
    NeedDamagedTarget : bool
    IsClickable : bool
    ShowProductionCount : bool
    NeededUpgradeAny : bool
    RequiresValidContainer : bool
    
    PresetRange : float
    AutoDelay : float
    
    CommandRangeStart : int
    CommandRangeCount : int
    CreateAHeroUIMinimumLevel : int
    CreateAHeroUICostIfSelected : int
    
    """
    def __init__(self, name, data, parser):
        self.parser = parser
               
        self.name = name
        
        self.string("label", data.pop("TextLabel", None))
        self.string("description", data.pop("DescriptLabel", None))
        
        self.command = CommandTypes[data.pop("Command")] if "Command" in data else None
        # self.options = [Options[x] for x in data.pop("Options")]
        
        self.__dict__.update(data)
                
    def __repr__(self):
        return f"<CommandButton {self.name}>"
        
    @classmethod
    def parse(cls, parser, name, lines):
        line = next(lines)
        data = {}
        
        while not is_end(line):
            key, value = line.split("=")
            data[key.strip()] = value.strip()  
            
            line = next(lines) 
            
        parser.commandbuttons[name] = cls(name, data, parser)
        
    @property
    def label(self):
        return self.parser.get_string(self._label)
        
    @property
    def description(self):
        return self.parser.get_string(self._description)
        
class Upgrade(IniObject):
    """
    Type : UpgradeTypes
    DisplayName : String
    BuildTime : int
    BuildCost : int
    ButtonImage : Image
    Tooltip : String
    Cursor : Cursor
    PersistsInCampaign : bool
    LocalPlayerGainsUpgradeEvaEvent : EvaEvent
    AlliedPlayerGainsUpgradeEvaEvent : EvaEvent
    EnemyPlayerGainsUpgradeEvaEvent : EvaEvent
    AlliedPlayerLosesUpgradeEvaEvent : EvaEvent
    EnemyPlayerLosesUpgradeEvaEvent : EvaEvent
    NoUpgradeDiscount : bool
    UseObjectTemplateForCostDiscount : Object
    SkirmishAIHeuristic : AI
    ResearchCompleteEvaEvent : EvaEvent
    ResearchSound : Sound
    RequiredObjectFilter : List[Objects, KindsOf]
    StrategicIcon : Image
    SubUpgradeTemplateNames : List[Upgrades]
    
    """
    def __init__(self, name, data, parser):
        self.parser = parser
        
        self.name = name
        self.type = UpgradeTypes[data.pop("Type")] if "Type" in data else None
        
        self.string("label", data.pop("DisplayName", None))
        self.string("description", data.pop("Tooltip", None))
        
        self.macro("build_time", data.pop("BuildTime", None))
        self.macro("build_cost", data.pop("BuildCost", None))
        
        self.reference("button_image", data.pop("ButtonImage", None), "images")
        self.reference("cursor", data.pop("Cursor", None), "cursors")
        
        self.persist_in_campaign = data.pop("PersistsInCampaign") == "Yes" if "PersistsInCampaign" in data else None
        
        
    def __repr__(self):
        return f"<Upgrade {self.name}>"    
        
    @classmethod
    def parse(cls, parser, name, lines):
        line = next(lines)
        data = {}
        
        while not is_end(line):
            key, value = line.split("=")
            data[key.strip()] = value.strip()  
            
            line = next(lines)
            
        parser.upgrades[name] = cls(name, data, parser)        

class String:
    """
    
    type : str
    name : str
    value : str
    shortcut : Optional[str]
    
    """
    def __init__(self, name, value):
        self.type, self.name = name.rsplit(":", 1)
        self.value = value
        match = re.search(r"&([A-Za-z])", value)
        self.shortcut = match.group(1) if match else None
        
    def __str__(self):
        return self.value
        
    def __repr__(self):
        return f"<String {self.name}>"
        
    @property
    def full_name(self):
        return f"{self.type}:{self.name}"
        
class FilterList:
    def __init__(self, name, values):
        self.name = name
        
        self.descriptor = None
        self.relations = []
        self.inclusion = []
        self.exclusion = []
        
        for value in values:
            if value in Descriptors.__members__:
                self.descriptor = Descriptors[value]
            elif value in Relations.__members__:
                self.relations.append(Relations[value])
            elif value.startswith(('-', '+')):
                if value[1:] in KindsOf.__members__:
                    member = KindsOf[value[1:]]
                else:
                    member = value[1:]

                if value[0] == "-":
                    self.exclusion.append(member)
                else:
                    self.inclusion.append(member)
                    
    def __repr__(self):
        return f"<FilterList {self.name}>"
        
    def is_in(self, obj, relation = None):
        exclusions = [x == obj.name or x in obj.kindof for x in self.exclusion]
        if any(exclusions):
            return False
            
        if relation not in self.relations and relation is not None:
            return False
        
        inclusions = bools = [x == obj.name or x in obj.kindof for x in self.inclusion]
        if self.descriptor == Descriptors.ALL:
            return all(inclusions)
        elif self.descriptor == Descriptors.ANY:
            return any(inclusions)
        elif self.descriptor == Descriptors.NONE:
            return not any(inclusions)
        
        
        return False
                    
class Operation:
    operation_mapping = {
        "MULTIPLY": lambda x, y: x*y,
    }
    
    def __init__(self, operation, args, parser):
        self.parser = parser
        
        self.key = operation
        self.operation = self.operation_mapping[operation]
        self.args = args
        
    def __repr__(self):
        return f"<Operation {self.key}>"
    
    @property
    def value(self):
        return self.operation(*[self.parser.get_macro(x) for x in self.args])
        
class ModifierList:
    pass
    
class Object(IniObject):
    def __init__(self, name, kindsof):
        self.name = name
        self.kindof = kindsof
    