from .enums import *
from .utils import is_end, to_float
from .objects import FilterList, IniObject
from .types import Float, Bool, Coords
from .nuggets import *

import sys
import logging

def get_obj(name):
    return getattr(sys.modules[__name__], name, None)

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
        self.decal = data.pop("SelectionDecal")[0] if data.get("SelectionDecal") else None
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
    
class CreateObject(IniObject):
    """
    ObjectNames : List[Object]
    IgnoreCommandPointLimit : bool
    Disposition : Dispositions
    Count : float
    UseJustBuiltFlag : bool
    JustBuiltDuration : float
    StartingBusyTime : float
    ClearRemovables : bool
    FadeIn : bool
    FadeTime : float
    RequiredUpgrades : List[Upgrades]
    Offset : coords
    DispositionAngle : float
    SpreadFormation : bool
    MinDistanceAFormation : float
    MinDistanceBFormation : float
    MaxDistanceFormation : float
    OrientInSecondaryDirection : bool
    OrientationOffset : float
    IssueMoveAfterCreation : bool
    IgnoreAllObjects : bool
    """
    def __init__(self, name, data, parser):
        self.name = None
        
        self.reference("objects", data.pop("ObjectNames", []), "objects")
        self.value("ignore_cp_limit", data.pop("IgnoreCommandPointLimit", "No"), Bool)
        self.enum("disposition", data.pop("Disposition", None), Dispositions)
        self.value("count", data.pop("Count", 0), Float)
        self.value("just_built_flag", data.pop("UseJustBuiltFlag", "No"), Bool)
        self.value("just_built_duration", data.pop("JustBuiltDuration", 0), Float)
        self.value("starting_busy_time", data.pop("StartingBusyTime", 0), Float)
        self.value("clear_removables", data.pop("ClearRemovables", "No"), Bool)
        self.value("fade_in", data.pop("FadeIn", "No"), Bool)
        self.value("fade_time", data.pop("FadeTime", 0), Float)
        self.reference("required_upgrades", data.pop("RequiredUpgrades", []), "upgrades")
        self.value("disposition_angle", data.pop("DispositionAngle", 0), Float)
        self.value("spread_formation", data.pop("SpreadFormation", "No"), Bool)
        self.value("offset", data.pop("Offset", None), Coords)
        
    special_attributes = {
        "ObjectNames": {"default": list, "func": lambda data, value: value.split()},
        "RequiredUpgrades": {"default": list, "func": lambda data, value: value.split()}
    }

class ObjectCreationList(IniObject):
    def __init__(self, name, data, parser):
        parser.objectcreationlists[name] = data.pop("CreateObject")
        
    nested_attributes = {
        "CreateObject": CreateObject
    }
    
class Weapon(IniObject):
    """
    AttackRange : LEGOLAS_BOW_RANGE
    RangeBonusMinHeight : EDAIN_SIEGE_RANGEBONUS_MINHEIGHT
    RangeBonus : EDAIN_ARCHER_RANGEBONUS
    RangeBonusPerFoot : EDAIN_SIEGE_RANGEBONUS_PERFOOT
    WeaponSpeed : 801
    MinWeaponSpeed : 300
    MaxWeaponSpeed : 641
    FireFX : FX_GloinShatterhammer
    ScaleWeaponSpeed : Yes
    HitPercentage : 70
    ScatterRadius : 0
    AcceptableAimDelta : 60
    DelayBetweenShots : 1000
    PreAttackDelay : GLORFINDEL_SWORD_PREATTACKDELAY
    PreAttackType : PER_SHOT
    FiringDuration : 1584
    ClipSize : 3
    AutoReloadsClip : NO
    AutoReloadWhenIdle : 1800
    ClipReloadTime : Max:1800
    ContinuousFireOne : 0
    ContinuousFireCoast : DWARVEN_MENOFDALE_BOW_RELOADTIME_MAX
    AntiAirborneVehicle : Yes
    AntiAirborneMonster : Yes
    CanFireWhileMoving : Yes
    ProjectileCollidesWith : WALLS
    RadiusDamageAffects : SUICIDE
    HitStoredTarget : Yes
    PreferredTargetBone : B_LLLID
    LeechRangeWeapon : Yes
    MeleeWeapon : Yes
    DamageDealtAtSelfPosition : Yes
    PreAttackFX : FX_TrollTreeSwing
    ShouldPlayUnderAttackEvaEvent : No
    FireFlankFX : FX_Flanking
    InstantLoadClipOnActivate : Yes
    IdleAfterFiringDelay : 2000
    MinimumAttackRange : ELVEN_VIGILANTENT_ROCK_RANGE_MIN
    ProjectileSelf : Yes
    PreAttackRandomAmount : 0
    HitPassengerPercentage : 20%
    CanBeDodged : Yes
    NoVictimNeeded : Yes
    BombardType : Yes
    OverrideVoiceAttackSound : CorsairVoiceAttackFirebomb
    OverrideVoiceEnterStateAttackSound : ElvenWarriorVoiceEnterStateAttackBow
    RequireFollowThru : Yes
    FinishAttackOnceStarted : Yes
    HoldDuringReload : Yes
    IsAimingWeapon : Yes
    HoldAfterFiringDelay : 2000
    ProjectileFilterInContainer : +GIMLI
    AntiStructure : Yes
    AntiGround : Yes
    ScatterRadiusVsInfantry : 0.08
    ScatterIndependently : Yes
    PlayFXWhenStealthed : Yes
    AimDirection : 270
    FXTrigger : CATAPULT_ROCK
    ShareTimers : Yes
    DisableScatterForTargetsOnWall : Yes
    DamageType : FLAME
    CanSwoop : Yes
    PassengerProportionalAttack : Yes
    MaxAttackPassengers : 4
    ChaseWeapon : Yes
    CanFireWhileCharging : yes
    IgnoreLinearFirstTarget : Yes
    LinearTarget : 3.2
    ForceDisplayPercentReady : Yes
    AntiAirborneInfantry : Yes
    LockWhenUsing : Yes
    ProjectileStreamName : FlamethrowerProjectileStream
    UseInnateAttributes : Yes
    """
