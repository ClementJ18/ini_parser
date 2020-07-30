from .enums import *
from .objects import IniObject
from .types import *
from .nuggets import *

import sys
    
class Upgrade(IniObject):
    key = "upgrades"
    
    Type : UpgradeTypes
    DisplayName : String
    BuildTime : Int = 0
    BuildCost : Int = 0
    # ButtonImage : Image
    Tooltip : String
    # Cursor : Cursor
    PersistsInCampaign : Bool = False
    # LocalPlayerGainsUpgradeEvaEvent : EvaEvent
    # AlliedPlayerGainsUpgradeEvaEvent : EvaEvent
    # EnemyPlayerGainsUpgradeEvaEvent : EvaEvent
    # AlliedPlayerLosesUpgradeEvaEvent : EvaEvent
    # EnemyPlayerLosesUpgradeEvaEvent : EvaEvent
    NoUpgradeDiscount : Bool = False
    UseObjectTemplateForCostDiscount : "Object"
    # SkirmishAIHeuristic : AI
    # ResearchCompleteEvaEvent : EvaEvent
    # ResearchSound : Sound
    RequiredObjectFilter : FilterList
    # StrategicIcon : Image
    SubUpgradeTemplateNames : List("Upgrade") = []

class Armor(IniObject):
    key = "armorsets"
    
    DEFAULT : Float = 1
    FlankedPenalty : Float = 1
    DamageScalar : Float = 1
    
    __annotations__.update({x.name : Float for x in DamageTypes})
        
    @staticmethod
    def line_parse(data, key, value):
        armor = value.split()
        if len(armor) == 2:
            data[armor[0].strip()] = armor[1]
        else:
            data[key] = value
        
    def get_damage_scalar(self, damagetype, flanked = False):
        value = getattr(self, damagetype.name, self.DEFAULT)
        
        if flanked:
            return value + (value * self.FlankedPenalty)
        
        return value * self.DamageScalar
        
class SpecialPower(IniObject):
    key = "specialpowers"
    
    Enum : SpecialPowerEnums
    ReloadTime : Int
    PublicTimer : Bool = False
    ObjectFilter : FilterList
    Flags : List(Flags)
    RequiredSciences : List("Sciences")
    # InitiateAtLocationSound : Sound
    ViewObjectDuration : Float
    ViewObjectRange : Float
    RadiusCursorRadius : Float
    MaxCastRange : Float
    ForbiddenObjectFilter : FilterList
    ForbiddenObjectRange : Float
    
class Science(IniObject):
    key = "sciences"
    
    PrerequisiteSciences : List("Science")
    SciencePurchasePoIntCost : Int = 0
    IsGrantable : Bool = False
    SciencePurchasePoIntCostMP : Int = 0
    
    @staticmethod
    def line_parse(data, key, value):
        if key == "PrerequisiteSciences":
            data[key] = [] if value.strip().lower() == "none" else value.split(" OR ")
        else:
            data[key] = value
    
    def is_unlocked(self, *sciences):
        return any(all(x in sciences for x in preq) for preq in self.PrerequisiteSciences)
        
class CreateObject(IniObject):
    key = None
    
    ObjectNames : List("Object")
    IgnoreCommandPoIntLimit : Bool
    Disposition : Dispositions
    Count : Int
    UseJustBuiltFlag : Bool
    JustBuiltDuration : Int
    StartingBusyTime : Int
    ClearRemovables : Bool
    FadeIn : Bool
    FadeTime : Int
    RequiredUpgrades : List(Upgrade)
    Offset : Coords
    DispositionAngle : Float
    SpreadFormation : Bool
    MinDistanceAFormation : Float
    MinDistanceBFormation : Float
    MaxDistanceFormation : Float
    OrientInSecondaryDirection : Bool
    OrientationOffset : Float
    IssueMoveAfterCreation : Bool
    IgnoreAllObjects : Bool
    
class ObjectCreationList(IniObject):
    def __init__(self, name, data, parser):
        parser.objectcreationlists[name] = data.pop("CreateObject")
        
    nested_attributes = {"CreateObject": [CreateObject]}
    
class CommandButton(IniObject):
    key = "commandbuttons"
    
    # ButtonBorderType : ButtonBorderTypes
    
    CommandTrigger : "CommandButton"
    ToggleButtonName : "CommandButton"
    
    Command : CommandTypes
    
    # CursorName : Cursor
    # InvalidCursorName : Cursor
    # RadiusCursorType : Cursor
    
    FlagsUsedForToggle : Flags
    # ButtonImage : Image
    AffectsKindOf : KindsOf
    Options : List(Options)
    # Stances : List(Stances)
    CreateAHeroUIAllowableUpgrades : List(Upgrade)
    
    AutoAbilityDisallowedOnModelCondition : ModelConditions
    DisableOnModelCondition : ModelConditions
    EnableOnModelCondition : ModelConditions
    
    Object : "Object"
    Science : Science
    
    # UnitSpecificSound : Sound
    # SetAutoAbilityUnitSound : Sound
    
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
    
    DoubleClick : Bool
    Radial : Bool
    InPalantir : Bool
    AutoAbility : Bool
    TriggerWhenReady : Bool
    ShowButton : Bool
    NeedDamagedTarget : Bool
    IsClickable : Bool
    ShowProductionCount : Bool
    NeededUpgradeAny : Bool
    RequiresValidContainer : Bool
    
    PresetRange : Float
    AutoDelay : Float
    
    CommandRangeStart : Int
    CommandRangeCount : Int
    CreateAHeroUIMinimumLevel : Int
    CreateAHeroUICostIfSelected : Int
    
class ExperienceLevel(IniObject):
    key = "levels"

    TargetNames : List("Object")
    RequiredExperience : Float
    ExperienceAward : Float
    Rank : Float
    ExperienceAwardOwnGuysDie : Float
    Upgrades : List(Upgrade)
    InformUpdateModule : Bool
    LevelUpTintColor : RGB
    LevelUpTintPreColorTime : Float
    LevelUpTintPostColorTime : Float
    LevelUpTintSustainColorTime : Float
    AttributeModifiers : "ModifierList"
    # LevelUpFx : FX
    ShowLevelUpTint : Bool
    EmotionType : EmotionTypes
    # SelectionDecal : SelectionDecal
    
    # nested_attributes = {"SelectionDecal": [SelectionDecal]}
    
class CommandSet(IniObject):
    key = "commandsets"
        
    InitialVisible : Int
            
    def __repr__(self):
        return f"<CommandSet {self.name} len={len(self.CommandButtons)}>"
        
    @property
    def CommandButtons(self):
        return {int(x) : CommandButton.convert(self.parser, y) for x, y in self.__dict__.items() if x.isdigit()}
        
    def as_list(self):
        size = max(list(self.CommandButtons.keys()))
        return [self.CommandButtons[index] if index in self.CommandButtons else None for index in range(1, size+1)] 
        
    def initial_visible(self):
        visible = sorted(list(self.CommandButtons.items()), key=lambda x: x[0])[:self.initial]
        return {x[0]: x[1] for x in visible}
    
    def get_button(self, index):
        try:
            return self.CommandButtons[index]
        except KeyError:
            raise KeyError(f"No CommandButton on slot {index}")
            
class ModifierList(IniObject):
    key = "modifiers"
    
    Category : ModifierCategories
    Duration : Int
    # FX : FX
    ReplaceInCategoryIfLongest : Bool
    IgnoreIfAnticategoryActive : Bool
    # FX2 : FX
    # FX3 : FX
    MultiLevelFX : Bool
    ModelCondition : ModelConditions
    ClearModelCondition : ModelConditions
    Upgrade : Upgrade
    # EndFX : FX
    
    __annotations__.update({x.name : Float for x in Modifier})
    INVULNERABLE : List(DamageTypes, index=1) = []
    ARMOR :  Tuple(Float, List(DamageTypes))
    
    @staticmethod
    def line_parse(data, key, value):
        if key == "Modifier":
            key, value = value.split(maxsplit=1)
        
        if key == "ARMOR":
            if key not in data:
                data[key] = []
                
            data[key].append(value)
        else:       
            data[key] = value
        
    
class Weapon(IniObject):
    key = "weapons"
    
    AttackRange : Float
    RangeBonusMinHeight : Float
    RangeBonus : Float
    RangeBonusPerFoot : Float
    WeaponSpeed : Float
    MinWeaponSpeed : Float
    MaxWeaponSpeed : Float
    # FireFX : FX
    ScaleWeaponSpeed : Bool
    HitPercentage : Float
    ScatterRadius : Float
    AcceptableAimDelta : Float
    DelayBetweenShots : Float
    PreAttackDelay : Float
    PreAttackType : Float
    FiringDuration : Float
    ClipSize : Float
    AutoReloadsClip : Bool
    AutoReloadWhenIdle : Float
    # ClipReloadTime : Max:1800
    ContinuousFireOne : Float
    ContinuousFireCoast : Float
    AntiAirborneVehicle : Bool
    AntiAirborneMonster : Bool
    CanFireWhileMoving : Bool
    ProjectileCollidesWith : Union(KindsOf, Relations)
    RadiusDamageAffects : List(Relations)
    HitStoredTarget : Bool
    # PreferredTargetBone : B_LLLID
    LeechRangeWeapon : Bool
    MeleeWeapon : Bool
    DamageDealtAtSelfPosition : Bool
    # PreAttackFX : FX
    ShouldPlayUnderAttackEvaEvent : Bool
    # FireFlankFX : FX
    InstantLoadClipOnActivate : Bool
    IdleAfterFiringDelay : Float
    MinimumAttackRange : Float
    ProjectileSelf : Bool
    PreAttackRandomAmount : Float
    HitPassengerPercentage : Float
    CanBeDodged : Bool
    NoVictimNeeded : Bool
    BombardType : Bool
    # OverrideVoiceAttackSound : Sound
    # OverrideVoiceEnterStateAttackSound : Sound
    RequireFollowThru : Bool
    FinishAttackOnceStarted : Bool
    HoldDuringReload : Bool
    IsAimingWeapon : Bool
    HoldAfterFiringDelay : Float
    ProjectileFilterInContainer : FilterList
    AntiStructure : Bool
    AntiGround : Bool
    ScatterRadiusVsInfantry : Float
    ScatterIndependently : Bool
    PlayFXWhenStealthed : Bool
    AimDirection : Float
    # FXTrigger : FX
    ShareTimers : Bool
    DisableScatterForTargetsOnWall : Bool
    DamageType : DamageTypes
    CanSwoop : Bool
    PassengerProportionalAttack : Bool
    MaxAttackPassengers : Float
    ChaseWeapon : Bool
    CanFireWhileCharging : Bool
    IgnoreLinearFirstTarget : Bool
    LinearTarget : Float
    ForceDisplayPercentReady : Bool
    AntiAirborneInfantry : Bool
    LockWhenUsing : Bool
    # ProjectileStreamName : ProjectileStream
    UseInnateAttributes : Bool
    
    nested_attributes = {
        "Nuggets": [
            AttributeModifierNugget, ClearNuggets, DOTNugget, DamageContainedNugget, DamageFieldNugget, 
            DamageNugget, EmotionWeaponNugget, FireLogicNugget, GrabNugget, HordeAttackNugget, LuaEventNugget, 
            MetaImpactNugget, OpenGateNugget, ParalyzeNugget, ProjectileNugget, SlaveAttackNugget, SpawnAndFadeNugget, 
            SpecialModelConditionNugget, StealMoneyNugget, WeaponOCLNugget
        ]
    }
    
    @property
    def attack_speed(self):
        return self.firing_duration + self.delay


class Object(IniObject):
    key = "objects"
    
    Side : Sides
    EditorSorting : KindsOf
    # ThingClass : CHARACTER_UNIT
    BuildCost : Int                
    BuildTime  : Int
    ShockwaveResistance : Int    
    DisplayMeleeDamage : Int      
    HeroSortOrder : Int
    CommandSet : CommandSet
    CommandPoints : Int
    DisplayName : String
    RecruitText : String
    ReviveText : String
    Hotkey : String
    
    default_attributes = {"Modules" : {}, "Upgrades": {}}
        
    def call_special_power(self, power):
        return [x for x in self.Modules if x.trigger.name == power.name]
        
    def add_upgrade(self, upgrade):
        self.Upgrades[upgrade.name] = upgrade
        
    def remove_upgrade(self, upgrade):
        del self.Upgrades[upgrade.name]

class ChildObject(Object):
    Parent : Object
    def __init__(self, name, data, parser):
        true_name, parent = name.split()
        
        self.Parent = parent
        super().__init__(true_name, data, parser)
        
    def __getattribute__(self, name):
        try:
            return Object.__getattribute__(self, name)
        except AttributeError:
            pass
        
        parent = Object.__getattribute__(self, "parent")
        return Object.__getattribute__(parent, name)
        
class PlayerTemplate(IniObject):
    key = "factions"
    
    Side : Sides
    PlayableSide : Bool
    StartMoney : Int
    PreferredColor : RGB
    IntrinsicSciences : List(Science)
    DisplayName : String
    # ScoreScreenImage : Image
    # LoadScreenMusic : Music
    IsObserver : Bool
    # LoadScreenImage : Image
    # BeaconName : Object
    # SideIconImage : Image
    Evil : Bool
    MaxLevelMP : Int
    MaxLevelSP : Int
    StartingUnit1 : Object
    StartingUnitOffset1 : Coords
    StartingUnit0 : Object
    StartingUnitOffset0 : Coords
    StartingUnit2 : Object
    StartingUnitOffset2 : Coords
    StartingUnitTacticalWOTR : Object
    IntrinsicSciencesMP : List(Science)
    SpellBook : Object
    SpellBookMp : Object
    PurchaseScienceCommandSet : CommandSet
    PurchaseScienceCommandSetMP : CommandSet
    # DefaultPlayerAIType : AI
    # LightPointsUpSound : Sounds
    # ObjectiveAddedSound : Sound
    # ObjectiveCompletedSound : Sound
    InitialUpgrades : List(Upgrade)
    BuildableHeroesMP : List(Object)
    BuildableRingHeroesMP : List(Object)
    SpellStoreCurrentPowerLabel : String
    SpellStoreMaximumPowerLabel : String
    ResourceModifierObjectFilter : FilterList
    ResourceModifierValues : List(Float)
    # MultiSelectionPortrait : Image
    StartingBuilding : Object
