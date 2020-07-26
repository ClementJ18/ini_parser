
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
        
        self.enum("command", data.pop("Command", None), CommandTypes)
        self.enum("options", data.pop("Options", []), Options)
        
        self.__dict__.update(data)
        
        self.parser.commandbuttons[name] = self

    @property
    def label(self):
        return self.parser.get_string(self._label)
        
    @property
    def description(self):
        return self.parser.get_string(self._description)
  
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
        
    nested_attributes = {"SelectionDecal": [SelectionDecal]} 
    special_attributes = {
        "TargetNames": {"default": list, "func": lambda data, value: value.split()},
        "Upgrades": {"default": list, "func": lambda data, value: value.split()}
    } 
        
def modifier_func(data, value):
    key, value = value.split(maxsplit=1)
    data["Modifier"][key.strip()] = value

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
    ARMOR_BUFFS = ["INVULNERABLE", "ARMOR"]
    
    def __init__(self, name, data, parser):
        self.parser = parser
        
        self.name = name
        self.enum("category", data.pop("Category", None), ModifierCategories)
        self.value("duration", data.pop("Duration", None), Float)
        
        self.value("replace_if_longest", data.pop("ReplaceInCategoryIfLongest", "No"), Bool)
        self.value("ignore_if_anti", data.pop("IgnoreIfAnticategoryActive", "No"), Bool)
        self.value("multi_level_fx", data.pop("MultiLevelFX", "No"), Bool)

        self.reference("upgrade", data.pop("Upgrade", None), "upgrades")
        
        self._modifiers = {}
        for key, value in data.pop("Modifier", {}).items():
            key = Modifier[key]                        
            self._modifiers[key] = value
            
        self.parser.modifiers[name] = self
  
    special_attributes = {
        "Modifier": {"default": dict, "func": modifier_func},
        "Upgrade": {"default": lambda: None, "func": lambda data, value: value.split()[0].strip()}
    }
    
    def description(self):
        pass
        
    def get_modifier(self, modifier_type : Modifier, damage_type : DamageTypes = None):
        if self._modifiers.get(modifier_type) is None:
            return None
        
        modifier = self.parser.get_macro(self._modifiers[modifier_type])
        if modifier_type.name in self.ARMOR_BUFFS:
            value = modifier.split(maxsplit=1)
            mod = to_float(self.parser.get_macro(value[0]))
            if len(value) > 1:
                damage_types = [DamageTypes[self.parser.get_macro(x)] for x in value[1].split()]
            else:
                damage_types = []
                
            if damage_type is None:
                return (mod, damage_types)
            
            if damage_type in damage_types or not damage_types:
                return mod
            
            return 1 if damage_type.is_mult() else 0
        
        return to_float(modifier)
            
        
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
        "CreateObject": [CreateObject]
    }
    
class Weapon(IniObject):
    """
    AttackRange : float
    RangeBonusMinHeight : float
    RangeBonus : float
    RangeBonusPerFoot : float
    WeaponSpeed : float
    MinWeaponSpeed : float
    MaxWeaponSpeed : float
    FireFX : FX
    ScaleWeaponSpeed : bool
    HitPercentage : float
    ScatterRadius : float
    AcceptableAimDelta : float
    DelayBetweenShots : float
    PreAttackDelay : float
    PreAttackType : float
    FiringDuration : float
    ClipSize : float
    AutoReloadsClip : bool
    AutoReloadWhenIdle : float
    ClipReloadTime : Max:1800
    ContinuousFireOne : float
    ContinuousFireCoast : float
    AntiAirborneVehicle : bool
    AntiAirborneMonster : bool
    CanFireWhileMoving : bool
    ProjectileCollidesWith : WALLS
    RadiusDamageAffects : SUICIDE
    HitStoredTarget : bool
    PreferredTargetBone : B_LLLID
    LeechRangeWeapon : bool
    MeleeWeapon : bool
    DamageDealtAtSelfPosition : bool
    PreAttackFX : FX
    ShouldPlayUnderAttackEvaEvent : bool
    FireFlankFX : FX
    InstantLoadClipOnActivate : bool
    IdleAfterFiringDelay : float
    MinimumAttackRange : float
    ProjectileSelf : bool
    PreAttackRandomAmount : float
    HitPassengerPercentage : float
    CanBeDodged : bool
    NoVictimNeeded : bool
    BombardType : bool
    OverrideVoiceAttackSound : Sound
    OverrideVoiceEnterStateAttackSound : Sound
    RequireFollowThru : bool
    FinishAttackOnceStarted : bool
    HoldDuringReload : bool
    IsAimingWeapon : bool
    HoldAfterFiringDelay : float
    ProjectileFilterInContainer : FilterList
    AntiStructure : bool
    AntiGround : bool
    ScatterRadiusVsInfantry : float
    ScatterIndependently : bool
    PlayFXWhenStealthed : bool
    AimDirection : float
    FXTrigger : FX
    ShareTimers : bool
    DisableScatterForTargetsOnWall : bool
    DamageType : DamageTypes
    CanSwoop : bool
    PassengerProportionalAttack : bool
    MaxAttackPassengers : float
    ChaseWeapon : bool
    CanFireWhileCharging : bool
    IgnoreLinearFirstTarget : bool
    LinearTarget : float
    ForceDisplayPercentReady : bool
    AntiAirborneInfantry : bool
    LockWhenUsing : bool
    ProjectileStreamName : FlamethrowerProjectileStream
    UseInnateAttributes : bool
    """
    
    nested_attributes = {
        "Nuggets": [
            AttributeModifierNugget, ClearNuggets, DOTNugget, DamageContainedNugget, DamageFieldNugget, 
            DamageNugget, EmotionWeaponNugget, FireLogicNugget, GrabNugget, HordeAttackNugget, LuaEventNugget, 
            MetaImpactNugget, OpenGateNugget, ParalyzeNugget, ProjectileNugget, SlaveAttackNugget, SpawnAndFadeNugget, 
            SpecialModelConditionNugget, StealMoneyNugget, WeaponOCLNugget
        ]
    }
    
    def __init__(self, name, data, parser):
        self.name = name
        self.parser = parser
        
        self.nuggets = data.pop("Nuggets")
        self.value("range", data.pop("AttackRange", None), Float)
        self.value("delay", data.pop("DelayBetweenShots", None), Float)
        self.value("firing_duration", data.pop("FiringDuration", None), Float)
        
        self.parser.weapons[name] = self
    
    @property
    def attack_speed(self):
        return self.firing_duration + self.delay
