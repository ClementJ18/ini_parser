from .objects import Behavior
from .types import *
from .enums import *

import sys

class SpecialPowerModule(Behavior):
    SpecialPowerTemplate : "SpecialPower"
    UpdateModuleStartsAttack : Bool
    StartsPaused : Bool
    # InitiateSound : Audio
    ReEnableAntiCategory : Bool
    AntiCategory : ModifierCategories
    # AntiFX : FXList
    AttributeModifier : String
    AttributeModifierRange : Float
    AttributeModifierAffectsSelf : Bool
    AttributeModifierAffects : FilterList
    # AttributeModifierFX : FXList
    AttributeModifierWeatherBased : Bool
    WeatherDuration : Int
    RequirementsFilterMPSkirmish : FilterList
    RequirementsFilterStrategic : FilterList
    TargetEnemy : Bool
    TargetAllSides : Bool
    # InitiateFX : FXList
    # TriggerFX : FXList
    # SetModelCondition : ContainCondition
    SetModelConditionTime : Float
    GiveLevels : Int
    DisableDuringAnimDuration : Bool
    IdleWhenStartingPower : Bool
    AffectGood : Bool
    AffectEvil : Bool
    AffectAllies : Bool
    AvailableAtStart : Bool
    # ChangeWeather : WeatherFlag
    AdjustVictim : Bool
    OnTriggerRechargeSpecialPower : String
    BurnDecayModifier : Int
    UseDistanceFromCommandCenter : Bool
    DistanceFromCommandCenter : Float

    @property
    def trigger(self):
        return self.SpecialPowerTemplate
        
class AttributeModifierAuraUpdate(Behavior):
    TriggeredBy : List("Upgrade")
    ConflictsWith : List("Upgrade")
    RequiresAllTriggers : Bool
    RequiresAllConflictingTriggers : Bool
    # CustomAnimAndDuration : AnimAndDuration
    Permanent : Bool
    BonusName : String
    RefreshDelay : Int
    Range : Float
    TargetEnemy : Bool
    AllowPowerWhenAttacking : Bool
    ObjectFilter : FilterList
    StartsActive : Bool
    RequiredConditions : AModAuraConditions
    AntiCategory : ModifierCategories
    # AntiFX : FXList
    AffectGood : Bool
    AffectEvil : Bool
    RunWhileDead : Bool
    AllowSelf : Bool
    AffectContainedOnly : Bool
    MaxActiveRank : Int
    
    @property
    def trigger(self):
        return self.TriggeredBy
        
class OCLSpecialPower(Behavior):
    SpecialPowerTemplate : "SpecialPower"
    UpdateModuleStartsAttack : Bool
    StartsPaused : Bool
    # InitiateSound : AudioEvent
    ReEnableAntiCategory : Bool
    AntiCategory : ModifierCategories
    # AntiFX : FXList
    AttributeModifier : String
    AttributeModifierRange : Float
    AttributeModifierAffectsSelf : Bool
    AttributeModifierAffects : FilterList
    # AttributeModifierFX : FXList
    AttributeModifierWeatherBased : Bool
    WeatherDuration : Int
    RequirementsFilterMPSkirmish : FilterList
    RequirementsFilterStrategic : FilterList
    TargetEnemy : Bool
    TargetAllSides : Bool
    # InitiateFX : FXList
    # TriggerFX : FXList
    # SetModelCondition : ContainCondition
    SetModelConditionTime : Float
    GiveLevels : Int
    DisableDuringAnimDuration : Bool
    IdleWhenStartingPower : Bool
    AffectGood : Bool
    AffectEvil : Bool
    AffectAllies : Bool
    AvailableAtStart : Bool
    # ChangeWeather : WeatherFlag
    AdjustVictim : Bool
    OnTriggerRechargeSpecialPower : String
    BurnDecayModifier : Int
    UseDistanceFromCommandCenter : Bool
    DistanceFromCommandCenter : Float
    UpgradeOCL : "Upgrade"
    OCL : "ObjectCreationList"
    CreateLocation : CreateAtLocations
    UpgradeName : "Upgrade"
    NearestSecondaryObjectFilter : FilterList
    
    @property
    def trigger(self):
        return self.SpecialPowerTemplate
        
class HeroModeSpecialAbilityUpdate(Behavior):
    SpecialPowerTemplate : "SpecialPower"
    StartAbilityRange : Float
    AbilityAbortRange : Float
    PreparationTime : Int
    PersistentPrepTime : Int
    PersistentCount : Int
    PackTime : Int
    UnpackTime : Int
    PreTriggerUnstealthTime : Int
    SkipPackingWithNoTarget : Bool
    PackUnpackVariationFactor : Float
    ParalyzeDurationWhenCompleted : Int
    ParalyzeDurationWhenAborted : Int
    SpecialObject : "Object"
    # SpecialObjectAttachToBone : Bone
    MaxSpecialObjects : Int
    SpecialObjectsPersistent : Bool
    EffectDuration : Int
    EffectValue : Int
    EffectRange : Float
    UniqueSpecialObjectTargets : Bool
    SpecialObjectsPersistWhenOwnerDies : Bool
    AlwaysValidateSpecialObjects : Bool
    FlipOwnerAfterPacking : Bool
    FlipOwnerAfterUnpacking : Bool
    FleeRangeAfterCompletion : Float
    # DisableFXParticleSystem : ParticleSystem
    DoCaptureFX : Bool
    # PackSound : AudioEvent
    # UnpackSound : AudioEvent
    # PrepSoundLoop : AudioEvent
    # TriggerSound : AudioEvent
    # ActiveLoopSound : AudioEvent
    LoseStealthOnTrigger : Bool
    AwardXPForTriggering : Int
    SkillPointsForTriggering : Int
    ApproachRequiresLOS : Bool
    ChargeAttackSpeedBoost : Bool
    # CustomAnimAndDuration : AnimAndDuration
    # GrabPassengerAnimAndDuration : AnimAndDuration
    GrabPassengerHealGainPercent : Float
    UnpackingVariation : Int
    MustFinishAbility : Bool
    FreezeAfterTriggerDuration : Int
    DisableWhenWearingTheRing : Bool
    RequiredConditions : SpecialPowerUnpackConditions
    RejectedConditions : SpecialPowerUnpackConditions
    # ContactPointOverride : Bone
    TriggerAttributeModifier : "ModifierList"
    AttributeModifierDuration : Int
    KillAttributeModifierOnExit : Bool
    KillAttributeModifierOnRejected : Bool
    Instant : Bool
    NeedCollisionBeforeTrigger : Bool
    ChainedButton : "CommandButton"
    SuppressForHordes : Bool
    ApproachUntilMembersInRange : Bool
    IgnoreFacingCheck : Bool
    # TriggerModelCondition : ContainCondition
    TriggerModelConditionDuration : Float
    HeroAttributeModifier : "ModifierList"
    HeroEffectDuration : Int
    UseUSERModelcondition : Bool
    StopUnitBeforeActivating : Bool
    
    @property
    def trigger(self):
        return self.SpecialPowerTemplate
    
