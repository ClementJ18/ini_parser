from .enums import *
from .utils import is_end, to_float
from .objects import FilterList

import sys
import logging

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
        
    def references(self, name, values, dict_name):
        setattr(self, f"_{name}", values)
        setattr(self.__class__, name, property(lambda x: [self.parser.get(dict_name, value) for value in getattr(self, f"_{name}")]))

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.name}"
        
    special_attributes = {}
    nested_attributes = {}
    
    @staticmethod
    def default_line_parse(data, value):
        return value.strip()

    @classmethod
    def parse(cls, parser, name, lines):
        line = next(lines)
        data = {x : y["default"]() for x, y in cls.special_attributes.items()}
        
        while not is_end(line):
            logging.debug(line)
            if "=" in line:
                key, value = line.split("=")
                key = key.strip()
                
                for special, func in cls.special_attributes.items():
                    if key == special:
                        returned = func["func"](data, value)
                        if returned is not None:
                            data[key] = returned
                        break
                else:
                    data[key] = cls.default_line_parse(data, value)
            else:
                try:
                    possible_name = line.split()
                    if len(possible_name) == 2:
                        obj_name = possible_name[0]
                        new_name = possible_name[1]
                    else:
                        obj_name = line.strip()
                        new_name = name
                        
                    cls.nested_attributes[obj_name].parse(parser, new_name, lines)  
                except KeyError:
                    pass
            
            line = next(lines) 
            
        return cls(name, data, parser)

class Armor(IniObject):
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
        self.DEFAULT = damage_types.pop("DEFAULT", 1.0)
        self.flanked = damage_types.pop("FlankedPenalty", 1.0)
        self.scalar = damage_types.pop("DamageScalar", 1.0)
        
        for damage in DamageTypes.__members__:
            setattr(self, damage, damage_types.pop(damage, self.DEFAULT))
            
        self.parser.armorsets[name] = self
            
    def __repr__(self):
        return f"<ArmorSet {self.name}>"
        
    special_attributes = {
        "FlankedPenalty": {"default": lambda: 1, "func": lambda data, value: to_float(value)},
        "DamageScalar": {"default": lambda: 1, "func": lambda data, value: to_float(value)}
    }
        
    @staticmethod
    def default_line_parse(data, value):
        damage, percent = value.split()
        data[damage.strip()] = to_float(percent)
        
    def get_damage_scalar(self, damagetype):
        return getattr(self, damagetype.name)

class CommandSet(IniObject):
    """
    
    name : str
    initial : int
    commandbuttons : Dict[int : str]
    
    
    """
    def __init__(self, name, data, parser):
        self.parser = parser
        
        self.name = name
        self.initial = data.pop("InitialVisible", None)
        self.commandbuttons = {int(x) : y for x,y in data.items()}
        
        self.parser.commandsets[name] = self
        
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
        
    special_attributes = {
        "InitialVisible": {"default": lambda: None, "func": lambda data, value: int(value)}
    }
    
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
        
        self.parser.commandbuttons[name] = self
                
    def __repr__(self):
        return f"<CommandButton {self.name}>"
        
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
    RequiredObjectFilter : FilterList
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
        
        self.persist_in_campaign = data.pop("PersistsInCampaign", "No") == "Yes"
        self.no_upgrade_discount = data.pop("NoUpgradeDiscount", "No") == "Yes"
        
        self.reference("object_for_discount", data.pop("UseObjectTemplateForCostDiscount", None), "objects")
        self.required_objects = FilterList(None, data.pop("RequiredObjectFilter", []))
        
        self.reference("icon", data.pop("StrategicIcon", None), "images")
        self.references("sub_upgrades", data.pop("SubUpgradeTemplateNames", []), "upgrades")
        
        self.parser.upgrades[name] = self
        
    def __repr__(self):
        return f"<Upgrade {self.name}>"
        
class SelectionDecal(IniObject):
    def __init__(self, name, data, parser):
        self.name = name

class ExperienceLevel(IniObject):
    """
    TargetNames : List[Object]
    RequiredExperience : float
    ExperienceAward : float
    Rank : float
    ExperienceAwardOwnGuysDie : float
    Upgrades : Upgrade
    InformUpdateModule : bool
    LevelUpTintColor : str
    LevelUpTintPreColorTime : float
    LevelUpTintPostColorTime : float
    LevelUpTintSustainColorTime : float
    AttributeModifiers - ModifierList
    LevelUpFx : FX
    ShowLevelUpTint : bool
    EmotionType : EmotionTypes
    SelectionDecal : SelectionDecal (nested)
    
    """
    def __init__(self, name, data, parser):
        self.parser = parser
        
        
        self.parser.levels[name] = self
        
    nested_attributes = {"SelectionDecal": SelectionDecal}  
        
def modifier_func(data, value):
    key, value = value.split(maxsplit=1)
    data["Modifier"][key.strip()] = value.split()

class ModifierList(IniObject):
    """
    Category : ModifierCategories
    Duration : int
    Modifier : Tuple[Modifier, float]
    FX : FX
    ReplaceInCategoryIfLongest : bool
    IgnoreIfAnticategoryActive : bool
    FX2 : FX
    FX3 : FX
    MultiLevelFX : bool
    ModelCondition : ModelConditions
    ClearModelCondition : ModelConditions
    Upgrade : Upgrade
    EndFX : FX
    """
    def __init__(self, name, data, parser):
        self.parser = parser
        
        self.name = name
        self.category = ModifierCategories[data.pop("Category")] if "Category" in data else None
        
        self.macro("duration", data.pop("Duration", None))
        
        self.replace_if_longest = data.pop("ReplaceInCategoryIfLongest", "No") == "Yes"
        self.ignore_if_anti = data.pop("IgnoreIfAnticategoryActive", "No") == "Yes"
        
        self.multi_level_fx = data.pop("MultiLevelFX", "No") == "Yes"
        
        self.reference("upgrade", data.pop("Upgrade", None), "upgrades")
        
        self.modifiers = {}
        for key, value in data.pop("Modifiers", {}).items():
            key = Modifier[key]
            
            try:
                value = to_float(value)
            except ValueError:
                value = [DamageTypes[x] for x in value.split()[1:]]
                
            self.modifiers[key] = value
            
        self.parser.modifiers[name] = self
            
    def __repr__(self):
        return f"<ModifierList {self.name}>"
        
    special_attributes = {
        "Modifier": {"default": dict, "func": modifier_func},
        "Upgrade": {"default": lambda: None, "func": lambda data, value: value.split()[0].strip()}
    }
        
    
class Object(IniObject):
    def __init__(self, name, kindsof):
        self.name = name
        self.kindof = kindsof
    