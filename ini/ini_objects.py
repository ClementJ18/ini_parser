from .enums import *
from .utils import is_end, to_float
from .objects import FilterList
from .types import Float, Bool

import sys
import logging

def get_obj(name):
    return getattr(sys.modules[__name__], name, None)

class IniObject:
    def recursive(self, func, values):
        values = self.parser.get_macro(values)
        if isinstance(values, list):
            return [self.recursive(func, value) for value in values]
        
        if isinstance(values, dict):
            return {x : self.recursive(func, y) for x, y in values.items()}
            
        return func(self, values)
        
    def string(other, name, value):
        setattr(other, f"_{name}", value)
        setattr(other.__class__, name, property(lambda self: self.parser.get_string(getattr(self, f"_{name}"))))

    def value(other, name, value, value_type):
        def func(self, v):
            return value_type.convert(self.parser, v)
            
        setattr(other, f"_{name}", value)
        setattr(other.__class__, name, property(lambda self: self.recursive(func, getattr(self, f"_{name}"))))
        
    def enum(other, name, value, value_enum):
        def func(self, v):
            if v is not None:
                return value_enum[v]
            
            return None

        setattr(other, f"_{name}", value)
        setattr(other.__class__, name, property(lambda self: self.recursive(func, getattr(self, f"_{name}"))))
    
    def reference(other, name, values, dict_name):
        def func(self, v):
            return self.parser.get(dict_name, v)
        
        setattr(other, f"_{name}", values)
        setattr(other.__class__, name, property(lambda self: self.recursive(func, getattr(self, f"_{name}")) ))

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.name}>"
        
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
                key, value = line.split("=", maxsplit=1)
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
        
        SEE DAMEGETYPES FOR THE REST
        
        """
        self.parser = parser
        
        self.name = name
        self.value("DEFAULT", damage_types.pop("DEFAULT", 1.0), Float)
        self.value("flanked", damage_types.pop("FlankedPenalty", 1.0), Float)
        self.value("scalar", damage_types.pop("DamageScalar", 1.0), Float)
        
        for damage, value in damage_types.items():
            if damage in DamageTypes.__members__:
                self.value(damage, value, Float)
            
        self.parser.armorsets[name] = self
        
    special_attributes = {
        "FlankedPenalty": {"default": lambda: 1, "func": lambda data, value: to_float(value)},
        "DamageScalar": {"default": lambda: 1, "func": lambda data, value: to_float(value)}
    }
        
    @staticmethod
    def default_line_parse(data, value):
        damage, percent = value.split()
        data[damage.strip()] = to_float(percent)
        
    def get_damage_scalar(self, damagetype, flanked = False):
        value = getattr(self, damagetype.name, self.DEFAULT) * self.scalar
        
        if flanked:
            return value + (value * flanked)
        
        return value

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
        
        self.enum("type", data.pop("Type", None), UpgradeTypes)
        
        self.string("label", data.pop("DisplayName", None))
        self.string("description", data.pop("Tooltip", None))
        
        self.value("build_time", data.pop("BuildTime", None), Float)
        self.value("build_cost", data.pop("BuildCost", None), Float)
        
        self.reference("button_image", data.pop("ButtonImage", None), "images")
        self.reference("cursor", data.pop("Cursor", None), "cursors")
        
        self.value("persist_in_campaign", data.pop("PersistsInCampaign", "No"), Bool)
        self.value("no_upgrade_discount", data.pop("NoUpgradeDiscount", "No"), Bool)
        
        self.reference("object_for_discount", data.pop("UseObjectTemplateForCostDiscount", None), "objects")
        self.required_objects = FilterList(None, data.pop("RequiredObjectFilter", []))
        
        self.reference("icon", data.pop("StrategicIcon", None), "images")
        self.reference("sub_upgrades", data.pop("SubUpgradeTemplateNames", []), "upgrades")
        
        self.__dict__.update(data)
        
        self.parser.upgrades[name] = self
  
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
    Upgrades : List[Upgrade]
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
        self.name = name
        
        self.reference("targets", data.pop("TargetNames", []), "objects")
        self.value("required", data.pop("RequiredExperience", 0), Float)
        self.value("award", data.pop("ExperienceAward", 0), Float)
        self.value("rank", data.pop("Rank", 0), Float)
        self.value("own_award", data.pop("ExperienceAwardOwnGuysDie", 0), Float)
        
        self.reference("upgrades", data.pop("Upgrades", []), "upgrades")
        
        self.value("inform_update", data.pop("InformUpdateModule", "No"), Bool)
        
        self.__dict__.update(data)
        
        self.parser.levels[name] = self
        
    nested_attributes = {"SelectionDecal": SelectionDecal} 
    special_attributes = {
        "TargetNames": {"default": list, "func": lambda data, value: value.split()},
        "Upgrades": {"default": list, "func": lambda data, value: value.split()}
    } 
        
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
        self.enum("category", data.pop("Category", None), ModifierCategories)
        self.value("duration", data.pop("Duration", None), Float)
        
        self.value("replace_if_longest", data.pop("ReplaceInCategoryIfLongest", "No"), Bool)
        self.value("ignore_if_anti", data.pop("IgnoreIfAnticategoryActive", "No"), Bool)
        self.value("multi_level_fx", data.pop("MultiLevelFX", "No"), Bool)

        self.reference("upgrade", data.pop("Upgrade", None), "upgrades")
        
        self.modifiers = {}
        for key, value in data.pop("Modifiers", {}).items():
            key = Modifier[key]
            
            try:
                value = to_float(value)
            except ValueError:
                value = [DamageTypes[x] for x in value.split()[1:]]
                
            self.modifiers[key] = value
            
        self.__dict__.update(data)
            
        self.parser.modifiers[name] = self
  
    special_attributes = {
        "Modifier": {"default": dict, "func": modifier_func},
        "Upgrade": {"default": lambda: None, "func": lambda data, value: value.split()[0].strip()}
    }
        
class Science(IniObject):
    """
    PrerequisiteSciences : List[Science]
    SciencePurchasePointCost - int
    IsGrantable - bool
    SciencePurchasePointCostMP - int
    """
    
    special_attributes = {
        # "PrerequisiteSciences": {"default": list, "func": lambda data, value: value.split()} 
    }
    
    def __init__(self, name, data, parser):
        self.parser = parser
        
        self.name = name
        sciences = data.pop("PrerequisiteSciences", ["NONE"])
        if sciences[0] == "NONE":
            sciences = []
        else:
            sciences = [x.split() for x in sciences.split("OR")]
            
        self.reference("prequisites", [] if sciences[0] == "NONE" else sciences, "sciences")
        self.value("cost", data.pop("SciencePurchasePointCost", 0), Float)
        self.value("is_grantable", data.pop("IsGrantable", "No"), Bool)
        self.value("cost_mp", data.pop("SciencePurchasePointCostMP", 0), Float)
        
        self.__dict__.update(data)
        
        self.parser.sciences[name] = self
        
    def is_unlocked(self, sciences):
        sciences = [y.name for y in sciences]
        return any(all(x in sciences for x in preq) for preq in self._prequisites)
    
class Object(IniObject):
    def __init__(self, name, kindsof):
        self.name = name
        self.kindof = kindsof
        
class SpecialPower(IniObject):
    """
    Enum : SpecialPowerEnums
    ReloadTime : float
    PublicTimer : bool
    ObjectFilter : FilterList
    Flags : List[Flags]
    RequiredSciences : List[Sciences]
    InitiateAtLocationSound : Sound
    ViewObjectDuration : float
    ViewObjectRange : float
    RadiusCursorRadius : float
    MaxCastRange : float
    ForbiddenObjectFilter : FilterList
    ForbiddenObjectRange : float
    """
    def __init__(self, name, data, parser):
        self.parser = parser
        self.name = name
        
        self.enum("special_enum", data.pop("Enum", None), SpecialPowerEnums)
        self.value("reload", data.pop("ReloadTime", 0), Float)
        self.value("public_timer", data.pop("PublicTimer", "No"), Bool)
        self.filter = FilterList(None, data.pop("ObjectFilter", []))
        self.enum("flags", data.pop("Flags", []), Flags)
        self.reference("sciences", data.pop("RequiredSciences", []), "sciences")
        self.value("cursor_radius", data.pop("RadiusCursorRadius", 0), Float)
        self.value("max_cast", data.pop("MaxCastRange", 0), Float)
        self.forbidden = FilterList(None, data.pop("ForbiddenObjectFilter", 0))
        self.value("forbidden_range", data.pop("ForbiddenObjectRange", 0), Float)
        
        self.parser.specialpowers[name] = self
        
    special_attributes = {
        "Flags": {"default": list, "func": lambda data, value: value.split()},
        "ForbiddenObjectFilter": {"default": list, "func": lambda data, value: value.split()}
    }