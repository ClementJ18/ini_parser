from .objects import Behavior
from .types import *
from .enums import *

import sys

class SpecialPowerModuleBehavior(Behavior):
    SpecialPowerTemplate : "SpecialPower"
    UpdateModuleStartsAttack : Bool
    StartsPaused : Bool
    # InitiateSound : Audio
    ReEnableAntiCategory : Bool
    AntiCategory : ModifierCategories
    # AntiFX : FXList
    AttributeModifier : "ModifierList"
    AttributeModifierRange : Float
    AttributeModifierAffectsSelf : Bool
    AttributeModifierAffects : ObjectFilter
    # AttributeModifierFX : FXList
    AttributeModifierWeatherBased : Bool
    WeatherDuration : Int
    RequirementsFilterMPSkirmish : ObjectFilter
    RequirementsFilterStrategic : ObjectFilter
    TargetEnemy : Bool
    TargetAllSides : Bool
    # InitiateFX : FXList
    # TriggerFX : FXList
    # SetModelCondition : ContainCondition KeyValuePair
    SetModelConditionTime : Float
    GiveLevels : Int
    DisableDuringAnimDuration : Bool
    IdleWhenStartingPower : Bool
    AffectGood : Bool
    AffectEvil : Bool
    AffectAllies : Bool
    AvailableAtStart : Bool
    ChangeWeather : WeatherFlag
    AdjustVictim : Bool
    OnTriggerRechargeSpecialPower : "SpecialPower"
    BurnDecayModifier : Int
    UseDistanceFromCommandCenter : Bool
    DistanceFromCommandCenter : Float

class SpecialPowerModule(SpecialPowerModuleBehavior):
    pass
    
class UpgradeBehavior(Behavior):
    TriggeredBy : List["Upgrade"]
    ConflictsWith : List["Upgrade"]
    RequiresAllTriggers : Bool
    RequiresAllConflictingTriggers : Bool
    # CustomAnimAndDuration : AnimAndDuration
    Permanent : Bool
  
class AttributeModifierAuraUpdate(UpgradeBehavior):
    BonusName : String
    RefreshDelay : Int
    Range : Float
    TargetEnemy : Bool
    AllowPowerWhenAttacking : Bool
    ObjectFilter : ObjectFilter
    StartsActive : Bool
    RequiredConditions : AModAuraCondition
    AntiCategory : ModifierCategories
    # AntiFX : FXList
    AffectGood : Bool
    AffectEvil : Bool
    RunWhileDead : Bool
    AllowSelf : Bool
    AffectContainedOnly : Bool
    MaxActiveRank : Int
       
class OCLSpecialPower(SpecialPowerModuleBehavior):
    UpgradeOCL : "Upgrade"
    OCL : "ObjectCreationList"
    CreateLocation : CreateAtLocation
    UpgradeName : "Upgrade"
    NearestSecondaryObjectFilter : ObjectFilter
        
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
    # # PackSound : AudioEvent
    # # UnpackSound : AudioEvent
    # # PrepSoundLoop : AudioEvent
    # # TriggerSound : AudioEvent
    # # ActiveLoopSound : AudioEvent
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

class AutoHealBehavior(UpgradeBehavior):
    StartsActive : Bool
    ButtonTriggered : Bool
    SingleBurst : Bool
    HealingAmount : Int
    HealingDelay : Int
    Radius : Int
    KindOf : List[KindOf]
    # UnitHealPulseFX : FXList
    StartHealingDelay : Int
    AffectsWholePlayer : Bool
    AffectsContained : Bool
    HealOnlyIfNotUnderAttack : Bool
    HealOnlyIfNotInCombat : Bool
    HealOnlyOthers : Bool
    NonStackable : Bool
    RespawnNearbyHordeMembers : Bool
    # RespawnFXList : FXList
    RespawnMinimumDelay : Int

class WallHubBehavior(Behavior):
    SegmentTemplateName : List["Object"]
    DefaultSegmentTemplateName : "Object"
    HubCapTemplateName : "Object"
    CliffCapTemplateName : "Object"
    ShoreCapTemplateName : "Object"
    BorderCapTemplateName : "Object"
    ElevatedSegmentTemplateName : "Object"
    StaggeredBuildFactor : Int
    BuilderRadius : Float
    MaxBuildoutDistance : Float
    Options : List[Options]

class GettingBuiltBehavior(Behavior):
    WorkerName : "Object"
    EvilWorkerName : "Object"
    TestFaction : Bool
    SpawnTimer : Float
    RebuildWhenDead : Bool
    HealWeapon : "Weapon"
    RebuildTimeSeconds : Float
    # SelfBuildingLoop : Sound
    # SelfRepairFromDamageLoop : Sound
    # SelfRepairFromRubbleLoop : Sound
    PercentOfBuildCostToRebuildPristine : Float
    PercentOfBuildCostToRebuildDamaged : Float
    PercentOfBuildCostToRebuildReallyDamaged : Float
    PercentOfBuildCostToRebuildRubble : Float
    DisallowRebuildFilter : ObjectFilter
    DisallowRebuildRange : Float
    UseSpawnTimerWithoutWorker : Bool

class CastleBehavior(Behavior):
    RepairHealthPercentPerSecond : Float
    BuildVariation : Int
    # CastleToUnpackForFaction : UnpackBase
    FilterValidOwnedEntries : ObjectFilter
    FilterCrew : ObjectFilter
    # FactionDecal : UnpackDecal
    # PreBuiltList : PreBuiltObjectLocation
    # PreBuiltPlyr : String
    # DecalName : String
    # DecalSize : Float
    FadeTime : Float
    UnpackDelayTime : Float
    BuildTime : Float
    ScanDistance : Float
    MaxCastleRadius : Float
    CrewPrepareTime : Int
    InstantUnpack : Bool
    KeepDeathKillsEverything : Bool
    # CrewReleaseFX : FXList
    # CrewPrepareFX : FXList
    CrewPrepareInterval : Int
    DisableStructureRotation : Bool
    # EvaEnemyCastleSightedEvent : EvaEvent
    Summoned : Bool
    TransferFoundationHealthToCastleUponUnpack : Bool

class CastleMemberBehavior(Behavior):
    # CampDestroyedOwnerEvaEvent : EvaEvent
    # CampDestroyedAllyEvaEvent : EvaEvent
    # CampDestroyedAttackerEvaEvent : EvaEvent
    # BeingBuiltSound : Sound
    StoreUpgradePrice : Bool
    CountsForEvaCastleBreached : Bool

class BuildingBehavior(Behavior):
    NightWindowName : "SubObject"
    FireWindowName : "SubObject"
    GlowWindowName : "SubObject"
    FireName : "SubObject"

class BridgeScaffoldBehavior(Behavior):
    pass

class BridgeTowerBehavior(Behavior):
    pass

class RampageBehavior(Behavior):
    RampageHealthThreshold : Float
    RampageLifeTimer : Int
    RampageAngryLifeTimer : Int
    RampageResetTimer : Int
    RampageEnemyCheckRange : Float
    RampageEnemyThreshold : Int
    RequiredUpgrade : List["Upgrade"]

class EnragedBehavior(Behavior):
    EnragedLifeTimer : Float

class EntEnragedUpdate(Behavior):
    ScanDelayTime : Int
    EnragedTime : Int
    TimeUntilCanRageAgain : Int
    ScanDistance : Float
    HatedObjectFilter : ObjectFilter
    FriendlyDeadFilter : ObjectFilter
    EnragedTransitionTime : Int
    # EnragedTransitionFX : FXList
    # EnragedOnBuffFX : FXList
    # EnragedOffBuffFX : FXList

class AIGateUpdate(Behavior):
    TriggerWidthX : Float
    TriggerWidthY : Float

class HitReactionBehavior(Behavior):
    HitReactionLifeTimer1 : Int
    HitReactionLifeTimer2 : Int
    HitReactionLifeTimer3 : Int
    HitReactionThreshold1 : Float
    HitReactionThreshold2 : Float
    HitReactionThreshold3 : Float
    FastHitsResetReaction : Bool
    HitsParalyze : Bool

class ClickReactionBehavior(Behavior):
    ClickReactionTimer : Int
    ReactionFrames1 : Int
    ReactionFrames2 : Int
    ReactionFrames3 : Int
    ReactionFrames4 : Int
    ReactionFrames5 : Int

class SiegeDockingBehavior(Behavior):
    DUMMY : Int

class AutoAbilityBehavior(Behavior):
    SpecialAbility : String
    MaxScanRange : Float
    MinScanRange : Float
    WorkingRadius : Float
    StartsActive : Bool
    BaseMaxRangeFromStartPos : Bool
    AdjustAttackMeleePosition : Bool
    Query : Tuple[Int, ObjectFilter]
    AllowSelf : Bool
    IdleTimeSeconds : Float
    ForbiddenStatus : ObjectStatus

class DualWeaponBehavior(Behavior):
    SwitchWeaponOnCloseRangeDistance : Float
    UseCloseRangeWhileMounted : Bool
    MinimumSwitchTime : Int
    UseHordeRangeWeapon : Bool
    UseRealVictimRange : Bool

class AimWeaponBehavior(Behavior):
    AimLowThreshold : Float
    AimHighThreshold : Float
    AimNearDistance : Float
    AimFarDistance : Float

class BezierProjectileBehavior(Behavior):
    TumbleRandomly : Bool
    DetonateCallsKill : Bool
    OrientToFlightPath : Bool
    FirstHeight : Float
    SecondHeight : Float
    FirstPercentIndent : Float
    SecondPercentIndent : Float
    CrushStyle : Bool
    DieOnImpact : Bool
    FinalStuckTime : Int
    PreLandingStateTime : Int
    BounceCount : Int
    BounceDistance : Float
    BounceFirstHeight : Float
    BounceSecondHeight : Float
    BounceFirstPercentIndent : Float
    BounceSecondPercentIndent : Float
    GarrisonHitKillRequiredKindOf : List[KindOf]
    GarrisonHitKillForbiddenKindOf : List[KindOf]
    GarrisonHitKillCount : Int
    # GarrisonHitKillFX : FXList
    # GroundHitFX : FXList
    # GroundBounceFX : FXList
    GroundHitWeapon : "Weapon"
    GroundBounceWeapon : "Weapon"
    FlightPathAdjustDistPerSecond : Float
    IgnoreTerrainHeight : Bool
    FirstPercentHeight : Float
    SecondPercentHeight : Float
    CurveFlattenMinDist : Float
    PreLandingEmotion : EmotionTypes
    PreLandingEmotionRadius : Float
    InvisibleFrames : Int
    FadeInTime : Int
    PostLandingStateTime : Int
    PostLandingEmotion : EmotionTypes
    PostLandingEmotionRadius : Float

class MissileUpdate(Behavior):
    TumbleRandomly : Bool
    DetonateCallsKill : Bool
    OrientToFlightPath : Bool
    FirstHeight : Float
    SecondHeight : Float
    FirstPercentIndent : Float
    SecondPercentIndent : Float
    CrushStyle : Bool
    DieOnImpact : Bool
    FinalStuckTime : Int
    PreLandingStateTime : Int
    BounceCount : Int
    BounceDistance : Float
    BounceFirstHeight : Float
    BounceSecondHeight : Float
    BounceFirstPercentIndent : Float
    BounceSecondPercentIndent : Float
    GarrisonHitKillRequiredKindOf : List[KindOf]
    GarrisonHitKillForbiddenKindOf : List[KindOf]
    GarrisonHitKillCount : Int
    # GarrisonHitKillFX : FXList
    # GroundHitFX : FXList
    # GroundBounceFX : FXList
    GroundHitWeapon : "Weapon"
    GroundBounceWeapon : "Weapon"
    FlightPathAdjustDistPerSecond : Float
    IgnoreTerrainHeight : Bool
    FirstPercentHeight : Float
    SecondPercentHeight : Float
    CurveFlattenMinDist : Float
    PreLandingEmotion : EmotionTypes
    PreLandingEmotionRadius : Float
    InvisibleFrames : Int
    FadeInTime : Int
    PostLandingStateTime : Int
    PostLandingEmotion : EmotionTypes
    PostLandingEmotionRadius : Float
    FuelLifetime : Int
    IgnitionDelay : Int
    DistanceToTravelBeforeTurning : Float
    DistanceToTargetBeforeDiving : Float
    # IgnitionFX : FXList
    DetonateOnNoFuel : Bool
    ExhaustTemplate : String

class PhysicsBehavior(Behavior):
    TumbleRandomly : Bool
    AllowBouncing : Bool
    KillWhenRestingOnGround : Bool
    GravityMult : Float
    OrientToFlightPath : Bool
    ShockStunnedTimeLow : Int
    ShockStunnedTimeHigh : Int
    ShockStandingTime : Int
    FirstHeight : Float
    SecondHeight : Float
    FirstPercentIndent : Float
    SecondPercentIndent : Float
    BounceCount : Int
    BounceFirstHeight : Float
    BounceSecondHeight : Float
    BounceFirstPercentIndent : Float
    BounceSecondPercentIndent : Float
    # GroundHitFX : FXList
    # GroundBounceFX : FXList
    IgnoreTerrainHeight : Bool
    FirstPercentHeight : Float
    SecondPercentHeight : Float
    CurveFlattenMinDist : Float

class DieBehavior(Behavior):
    DeathType : DeathTypeFilter
    ExemptStatus : ObjectStatus
    RequiredStatus : ObjectStatus
    DamageAmountRequired : Float
    MinKillerAngle : Degrees
    MaxKillerAngle : Degrees

class InstantDeathBehavior(DieBehavior):
    # FX : FXList
    OCL : "ObjectCreationList"
    Weapon : "Weapon"
    # Sound : MomentSound

class SlowDeathBehavior(DieBehavior):
    SinkRate : Float
    ProbabilityModifier : Int
    ModifierBonusPerOverkillPercent : Float
    SinkDelay : Int
    SinkDelayVariance : Int
    DestructionDelay : Int
    DestructionDelayVariance : Int
    DecayBeginTime : Int
    # FX : MomentFXList
    OCL : Moment
    Weapon : Moment
    # Sound : MomentSound

class ShipSlowDeathBehavior(SlowDeathBehavior):
    pass

class SpawnBehavior(UpgradeBehavior):
    DeathType : DeathTypeFilter
    ExemptStatus : ObjectStatus
    RequiredStatus : ObjectStatus
    DamageAmountRequired : Float
    MinKillerAngle : Degrees
    MaxKillerAngle : Degrees
    SpawnNumber : Int
    SpawnReplaceDelay : Int
    OneShot : Bool
    CanReclaimOrphans : Bool
    AggregateHealth : Bool
    ExitByBudding : Bool
    SpawnTemplateName : List["Object"]
    SpawnedRequireSpawner : Bool
    PropagateDamageTypesToSlavesWhenExisting : DamageTypeFilter
    InitialBurst : Int
    RespectCommandLimit : Bool
    FadeInTime : Int
    KillSpawnsBasedOnModelConditionState : Bool
    ShareUpgrades : Bool
    SpawnInsideBuilding : Bool

class GiantBirdSlowDeathBehavior(SlowDeathBehavior):
    # FXHitGround : FXList
    OCLHitGround : "ObjectCreationList"
    DelayFromGroundToFinalDeath : Int
    CrashAvoidKindOfs : List[KindOf]
    CrashAvoidRadius : Float
    CrashAvoidStrength : Float
    NeedToMaintainFlailingHeight : Bool
    
class ContainBehavior(Behavior):
    ContainMax : Int
    # EnterSound : AudioEvent
    # ExitSound : AudioEvent
    DamagePercentToUnits : Float
    PassengerFilter : ObjectFilter
    ManualPickUpFilter : ObjectFilter
    PassengersTestCollisionHeight : Float
    PassengersInTurret : Bool
    NumberOfExitPaths : Int
    DoorOpenTime : Int
    AllowOwnPlayerInsideOverride : Bool
    AllowAlliesInside : Bool
    AllowEnemiesInside : Bool
    AllowNeutralInside : Bool
    ShowPips : Bool
    CollidePickup : Bool
    # PassengerBonePrefix : PassengerBoneKindof
    # BoneSpecificConditionState : IndexAnimationState
    EjectPassengersOnDeath : Bool
    KillPassengersOnDeath : Bool
    Enabled : Bool
    ObjectStatusOfContained : ObjectStatus
    ModifierToGiveOnExit : List["ModifierList"]
    ModifierRequiredTime : Int
    DeathType : DeathTypeFilter
    ExemptStatus : ObjectStatus
    RequiredStatus : ObjectStatus
    DamageAmountRequired : Float
    MinKillerAngle : Degrees
    MaxKillerAngle : Degrees
    

class CaveContain(ContainBehavior):
    CaveIndex : Int

class OpenContain(ContainBehavior):
    pass

class SpawnUnitBehavior(Behavior):
    UnitName : "Object"
    UnitCommand : "CommandButton"
    SpawnOnce : Bool

class WargBehavior(Behavior):
    pass

class DynamicPortalBehaviour(UpgradeBehavior):
    # BonePrefix : String
    NumberOfBones : Int
    # WayPoint : List[KeyValuePair]
    # Link : List[KeyValuePair]
    # WallBoundsMesh : String
    GenerateNow : Bool
    AboveWall : Int
    TopAttackPos : Coords
    TopAttackRadius : Float
    AllowEnemies : Bool
    ActivationDelaySeconds : Float
    ObjectFilter : ObjectFilter

class FakePathfindPortalBehaviour(UpgradeBehavior):
    AllowEnemies : Bool
    AllowNonSkirmishAIUnits : Bool

class MineshaftPortalBehaviour(UpgradeBehavior):
    AllowEnemies : Bool
    AllowNonSkirmishAIUnits : Bool

class CritterEmitterUpdate(Behavior):
    # FX : FXList
    ReloadTime : Int

class StancesBehavior(Behavior):
    StanceTemplate : "StanceTemplate"

class HealContain(ContainBehavior):
    TimeForFullHeal : Int
    
class AbstractHordeContainBehavior(ContainBehavior):
    Slots : Int
    ScatterNearbyOnExit : Bool
    OrientLikeContainerOnExit : Bool
    GoAggressiveOnExit : Bool
    ResetMoodCheckTimeOnExit : Bool
    DestroyRidersWhoAreNotFreeToExit : Bool
    ExitBone : String
    ExitPitchRate : Float
    InitialPayload : List[Tuple["Object", Int]]
    HealthRegen_PerSec : Float
    ExitDelay : Int
    TypeOneForWeaponSet : List[KindOf]
    TypeTwoForWeaponSet : List[KindOf]
    TypeOneForWeaponState : List[KindOf]
    TypeTwoForWeaponState : List[KindOf]
    TypeThreeForWeaponState : List[KindOf]
    ForceOrientationContainer : Bool
    CanGrabStructure : Bool
    GrabWeapon : "Weapon"
    FireGrabWeaponOnVictim : Bool
    # ConditionForEntry : ContainCondition
    ShouldThrowOutPassengers : Bool
    ThrowOutPassengersDelay : Int
    ThrowOutPassengersVelocity : Coords
    ThrowOutPassengersLandingWarhead : "Weapon"
    FadeFilter : ObjectFilter
    FadePassengerOnEnter : Bool
    FadePassengerOnExit : Bool
    EnterFadeTime : Float
    ExitFadeTime : Float
    FadeReverse : Bool
    ReleaseSnappyness : Float
    UpgradeCreationTrigger : Tuple["Upgrade", "Object", Int]
    
class HordeContainBehavior(AbstractHordeContainBehavior):
    ThisFormationIsTheMainFormation : Bool
    RankInfo : KeyValuePair[Int, "Object", Coords]
    RanksThatStopAdvance : Int
    RanksToReleaseWhenAttacking : List[Int]
    RanksToJustFreeWhenAttacking : List[Int]
    ComboHorde : "Object"
    AlternateFormation : String
    RandomOffset : Coords
    LeaderPosition : Coords
    LeadersAllowed : List["Object"]
    LeaderPosition : Coords
    BannerCarrierPosition : Coords
    BannerCarriersAllowed : List["Object"]
    BannerCarrierDestroyHordeOnDeath : Bool
    BannerCarrierHordeDeathType : DeathTypeFilter
    LeaderRank : Int
    BackUpMinDelayTime : Int
    BackUpMaxDelayTime : Int
    BackUpMinDistance : Float
    BackUpMaxDistance : Float
    BackupFloat : Float
    CowerRadius : Float
    AttributeModifiers : List["ModifierList"]
    IsPorcupineFormation : Bool
    # ForcedLocomotorSet : LocomotorSetType
    MachineAllowed : Bool
    MachineType : String
    UseSlowHordeMovement : Bool
    # SplitHorde : SplitHorde
    MeleeAttackLeashDistance : Float
    # EvaEventLastMemberDeath : EvaEvent
    RankSplit : Bool
    SplitHordeNumber : Int
    NotComboFormation : Bool
    UseMarchingAnims : Bool
    FrontAngle : Float
    FlankedDelay : Int
    FlankedDuration : Int
    # MeleeBehavior : MeleeBehavior
    MinimumHordeSize : Int
    VisionRearOverride : Float
    VisionSideOverride : Float
    BannerCarrierMinLevel : Int
    LivingWorldOverloadTemplate : String
    
class HordeContain(HordeContainBehavior):
    pass

class HorseHordeContain(HordeContainBehavior):
    pass

class GarrisonContain(ContainBehavior):
    MobileGarrison : Bool
    HealObjects : Bool
    TimeForFullHeal : Int
    InitialRoster : Tuple["Object", Int]
    ImmuneToClearBuildingAttacks : Bool

class TransportContain(AbstractHordeContainBehavior):
    pass

class SiegeEngineContain(AbstractHordeContainBehavior):
    CrewFilter : ObjectFilter
    CrewMax : Int
    InitialCrew : Tuple["Object", Int]
    SpeedPercentPerCrew : Float
    CrewAllowedToFire : Bool
    ObjectStatusOfCrew : ObjectStatus
    TransferSelection : Bool

class HordeSiegeEngineContain(AbstractHordeContainBehavior):
    CrewFilter : ObjectFilter
    CrewMax : Int
    InitialCrew : Tuple["Object", Int]
    SpeedPercentPerCrew : Float
    CrewAllowedToFire : Bool
    ObjectStatusOfCrew : ObjectStatus

class TunnelContain(ContainBehavior):
    MobileGarrison : Bool
    HealObjects : Bool
    TimeForFullHeal : Int
    InitialRoster : Tuple["Object", Int]
    ImmuneToClearBuildingAttacks : Bool
    ExitDelay : Int
    EntryOffset : Coords
    EntryPosition : Coords
    ExitOffset : Coords

class HordeTransportContain(AbstractHordeContainBehavior):
    pass

class HordeGarrisonContain(ContainBehavior):
    MobileGarrison : Bool
    HealObjects : Bool
    TimeForFullHeal : Int
    InitialRoster : Tuple["Object", Int]
    ImmuneToClearBuildingAttacks : Bool
    ExitDelay : Int
    EntryOffset : Coords
    EntryPosition : Coords
    ExitOffset : Coords

class RiderChangeContain(AbstractHordeContainBehavior):
    CrewFilter : ObjectFilter
    CrewMax : Int
    InitialCrew : Tuple["Object", Int]
    SpeedPercentPerCrew : Float
    CrewAllowedToFire : Bool
    ObjectStatusOfCrew : ObjectStatus
    TransferSelection : Bool

class SlaughterHordeContain(ContainBehavior):
    MobileGarrison : Bool
    HealObjects : Bool
    TimeForFullHeal : Int
    InitialRoster : Tuple["Object", Int]
    ImmuneToClearBuildingAttacks : Bool
    ExitDelay : Int
    EntryOffset : Coords
    EntryPosition : Coords
    ExitOffset : Coords
    CashBackPercent : Float
    CanAlwaysEnter : ObjectFilter
    StatusRequiredForCanAlwaysEnter : ObjectStatus

class CitadelSlaughterHordeContain(ContainBehavior):
    MobileGarrison : Bool
    HealObjects : Bool
    TimeForFullHeal : Int
    InitialRoster : Tuple["Object", Int]
    ImmuneToClearBuildingAttacks : Bool
    ExitDelay : Int
    EntryOffset : Coords
    EntryPosition : Coords
    ExitOffset : Coords
    CashBackPercent : Float
    CanAlwaysEnter : ObjectFilter
    StatusRequiredForCanAlwaysEnter : ObjectStatus
    StatusForRingEntry : ObjectStatus
    UpgradeForRingEntry : List["Upgrade"]
    ObjectToDestroyForRingEntry : ObjectFilter
    # FXForRingEntry : FXList

class ProductionQueueHordeContain(ContainBehavior):
    MobileGarrison : Bool
    HealObjects : Bool
    TimeForFullHeal : Int
    InitialRoster : Tuple["Object", Int]
    ImmuneToClearBuildingAttacks : Bool
    ExitDelay : Int
    EntryOffset : Coords
    EntryPosition : Coords
    ExitOffset : Coords
    DestinationTemplate : Tuple["Object", ObjectFilter]

class PropagandaTowerBehavior(Behavior):
    Radius : Float
    DelayBetweenUpdates : Int
    HealPercentEachSecond : Float
    UpgradedHealPercentEachSecond : Float
    # PulseFX : FXList
    UpgradeRequired : "Upgrade"
    # UpgradedPulseFX : FXList

class TerrainResourceBehavior(Behavior):
    Radius : Float
    MaxIncome : Int
    IncomeInterval : Int
    HighPriority : Bool
    Visible : Bool
    Upgrade : "Upgrade"
    UpgradeBonusPercent : Float
    UpgradeMustBePresent : ObjectFilter

class FireWeaponWhenDamagedBehavior(Behavior):
    StartsActive : Bool
    ReactionWeaponPristine : "Weapon"
    ReactionWeaponDamaged : "Weapon"
    ReactionWeaponReallyDamaged : "Weapon"
    ReactionWeaponRubble : "Weapon"
    ContinuousWeaponPristine : "Weapon"
    ContinuousWeaponDamaged : "Weapon"
    ContinuousWeaponReallyDamaged : "Weapon"
    ContinuousWeaponRubble : "Weapon"
    DamageTypes : DamageTypeFilter
    DamageAmount : Float
    TriggeredBy : List["Upgrade"]
    ConflictsWith : List["Upgrade"]
    RequiresAllTriggers : Bool
    RequiresAllConflictingTriggers : Bool
    # CustomAnimAndDuration : AnimAndDuration
    Permanent : Bool

class FireWeaponWhenDeadBehavior(Behavior):
    StartsActive : Bool
    ActiveDuringConstruction : Bool
    DelayTime : Int
    DeathWeapon : "Weapon"
    WeaponOffset : Coords
    TriggeredBy : List["Upgrade"]
    ConflictsWith : List["Upgrade"]
    RequiresAllTriggers : Bool
    RequiresAllConflictingTriggers : Bool
    # CustomAnimAndDuration : AnimAndDuration
    Permanent : Bool
    DeathType : DeathTypeFilter
    ExemptStatus : ObjectStatus
    RequiredStatus : ObjectStatus
    DamageAmountRequired : Float
    MinKillerAngle : Degrees
    MaxKillerAngle : Degrees

class PoisonedBehavior(Behavior):
    PoisonDamageInterval : Int

class RebuildHoleBehavior(Behavior):
    WorkerObjectName : "Object"
    WorkerRespawnDelay : Int
    HoleHealthRegen_PerSecond : Float

class SupplyWarehouseCripplingBehavior(Behavior):
    SelfHealSupression : Int
    SelfHealDelay : Int
    SelfHealAmount : Float

class ClearanceTestingSlowDeathBehavior(DieBehavior):
    SinkRate : Float
    ProbabilityModifier : Int
    ModifierBonusPerOverkillPercent : Float
    SinkDelay : Int
    SinkDelayVariance : Int
    DestructionDelay : Int
    DestructionDelayVariance : Int
    DecayBeginTime : Int
    # FX : MomentFXList
    OCL : Moment
    Weapon : Moment
    # Sound : MomentSound
    # ClearanceGeometry : Unknown
    ClearanceGeometryMajorRadius : Float
    ClearanceGeometryMinorRadius : Float
    ClearanceGeometryRotationAnchorOffset : Coords
    ClearanceGeometryHeight : Float
    ClearanceGeometryIsSmall : Bool
    ClearanceGeometryOffset : Coords
    ClearanceMaxHeight : Float
    ClearanceMaxHeightFraction : Float
    ClearanceMinHeight : Float
    ClearanceMinHeightFraction : Float

class RunOffMapBehavior(Behavior):
    RunToLocation : Coords
    RequiresSpecificTrigger : Bool
    RunOffMapWaypointName : String
    DieOnMap : Bool

class ReplenishUnitsBehavior(Behavior):
    StartsActive : Bool
    ReplenishDelay : Int
    ReplenishRadius : Float
    NoReplenishIfEnemyWithinRadius : Float
    # ReplenishFXList : FXList
    ReplenishStatii : ObjectStatus
    ReplenishHordeMembersOnly : Bool
    TriggeredBy : List["Upgrade"]
    ConflictsWith : List["Upgrade"]
    RequiresAllTriggers : Bool
    RequiresAllConflictingTriggers : Bool
    # CustomAnimAndDuration : AnimAndDuration
    Permanent : Bool

class SlaveWatcherBehavior(Behavior):
    RemoveUpgrade : "Upgrade"
    GrantUpgrade : "Upgrade"
    ShareUpgrades : Bool
    LetSlaveLive : Bool

class AnnounceBirthAndDeathBehavior(Behavior):
    pass

class DestroyDie(DieBehavior):
    pass

class FXListDie(DieBehavior):
    # DeathFX : FXList
    OrientToObject : Bool

class CrushDie(DieBehavior):
    # TotalCrushSound : AudioEvent
    # BackEndCrushSound : AudioEvent
    # FrontEndCrushSound : AudioEvent
    TotalCrushSoundPercent : Int
    BackEndCrushSoundPercent : Int
    FrontEndCrushSoundPercent : Int

class HeroDie(DieBehavior):
    SpecialPowerTemplate : "SpecialPower"

class CreateCrateDie(DieBehavior):
    CrateData : "CrateData"

class RefundDie(DieBehavior):
    UpgradeRequired : "Upgrade"
    BuildingRequired : ObjectFilter
    RefundPercent : Float
    
class CreateObjectDieBehavior(DieBehavior):
    CreationList : "ObjectCreationList"

class CreateObjectDie(CreateObjectDieBehavior):
    # DebrisPortionOfSelf : String
    UpgradeRequired : List["Upgrade"]

class CreateObjectDieIfEldestKindof(CreateObjectDie):
    ObjectFilter : ObjectFilter

class DamageFilteredCreateObjectDie(CreateObjectDieBehavior):
    DamageTypeTriggersInstantly : DamageType
    DamageTypeTriggersForDuration : DamageType
    PostFilterTriggeredDuration : Int

class SpecialPowerCompletionDie(DieBehavior):
    SpecialPowerTemplate : "SpecialPower"

class RebuildHoleExposeDie(DieBehavior):
    HoleName : "Object"
    HoleMaxHealth : Float
    TransferAttackers : Bool
    FadeInTimeSeconds : Float

class UpgradeDie(DieBehavior):
    UpgradeToRemove : "Upgrade"

class KeepObjectDie(DieBehavior):
    CollapsingTime : Int
    StayOnRadar : Bool

class AssistedTargetingUpdate(Behavior):
    AssistingClipSize : Int
    # AssistingWeaponSlot : SlotType
    LaserFromAssisted : "Object"
    LaserToTarget : "Object"

class AutoFindHealingUpdate(Behavior):
    ScanRate : Int
    ScanRange : Float
    NeverHeal : Float
    AlwaysHeal : Float

class StealthDetectorUpdate(Behavior):
    DetectionRate : Int
    DetectionRange : Float
    InitiallyDisabled : Bool
    # PingSound : AudioEvent
    # LoudPingSound : AudioEvent
    # IRBeaconParticleSysName : ParticleSystem
    # IRParticleSysName : ParticleSystem
    # IRBrightParticleSysName : ParticleSystem
    # IRGridParticleSysName : ParticleSystem
    IRParticleSysBone : String
    ExtraRequiredKindOf : List[KindOf]
    ExtraForbiddenKindOf : List[KindOf]
    CanDetectWhileGarrisoned : Bool
    CanDetectWhileContained : Bool
    CancelOneRingEffect : Bool
    RequiredUpgrade : "Upgrade"

class BroadcastStealthUpdate(UpgradeBehavior):
    AllowKindOf : List[KindOf]
    Radius : Float
    DelayBetweenUpdates : Int
    PersistantConditions : ModelCondition

class StealthUpdate(Behavior):
    StealthDelay : Int
    MoveThresholdSpeed : Float
    StealthForbiddenConditions : ModelCondition
    RemoveTerrainRestrictionOnUpgrade : List["Upgrade"]
    HintDetectableConditions : ObjectStatus
    FriendlyOpacityMin : Float
    FriendlyOpacityMax : Float
    PulseFrequency : Int
    DisguisesAsTeam : Bool
    RevealDistanceFromTarget : Float
    OrderIdleEnemiesToAttackMeUponReveal : Bool
    # DisguiseFX : FXList
    # DisguiseRevealFX : FXList
    DisguiseTransitionTime : Int
    DisguiseRevealTransitionTime : Int
    StartsActive : Bool
    InnateStealth : Bool
    DetectedByFriendliesOnly : Bool
    DetectedByAnyoneRange : Float
    # BecomeStealthedFX : FXList
    # ExitStealthFX : FXList
    RevealWeaponSets : WeaponsetFlags
    # VoiceMoveToStealthyArea : Sound
    # VoiceEnterStateMoveToStealthyArea : Sound
    OneRingDelayOn : Int
    OneRingDelayOff : Int
    RingAnimTimeOn : Int
    RingAnimTimeOff : Int
    RingDelayAfterRemoving : Int
    # BecomeStealthedOneRingFX : FXList
    # ExitStealthOneRingFX : FXList
    # EvaEventDetectedEnemy : EvaEvent
    # EvaEventDetectedAlly : EvaEvent
    # EvaEventDetectedOwner : EvaEvent
    RequiredUpgradeNames : List["Upgrade"]
    RequiredUpgradeNames : List["Upgrade"]

class EvaAnnounceClientCreate(Behavior):
    # AnnouncementEventEnemy : EvaEvent
    # AnnouncementEventAlly : EvaEvent
    # AnnouncementEventOwner : EvaEvent
    DelayBeforeAnnouncementMS : Int
    OnlyIfVisible : Bool
    CountAsFirstSightedAnnoucement : Bool
    UseObjectsPosition : Bool
    CreateFakeRadarEvent : Bool

class TerrainResourceClientBehavior(Behavior):
    pass

class ModelConditionAudioLoopClientBehavior(Behavior):
    # ModelCondition : ModelConditionAudio
    pass

class RandomSoundSelectorClientBehavior(Behavior):
    Chance : Float
    RerollOnEveryFrame : Bool
    # UnitSpecificSounds : UnitSpecificSounds
    # VoicePriority : Int
    # VoiceSelect : Sound
    # VoiceSelectUnderConstruction : Sound
    # VoiceSelectBattle : Sound
    # VoiceMove : Sound
    # VoiceMoveToHigherGround : Sound
    # VoiceMoveOverWalls : Sound
    # VoiceAttack : Sound
    # VoiceAttackCharge : Sound
    # VoiceFear : Sound
    # VoiceCreated : Sound
    # VoiceTaskComplete : Sound
    # VoiceDefect : Sound
    # VoiceAttackAir : Sound
    # VoiceGuard : Sound
    # VoiceAlert : Sound
    # VoiceFullyCreated : Sound
    # VoiceRetreatToCastle : Sound
    # VoiceMoveToCamp : Sound
    # VoiceAttackStructure : Sound
    # VoiceAttackMachine : Sound
    # VoiceMoveWhileAttacking : Sound
    # VoiceCombineWithHorde : Sound
    # VoiceEnterStateAttack : Sound
    # VoiceEnterStateAttackCharge : Sound
    # VoiceEnterStateAttackAir : Sound
    # VoiceEnterStateAttackStructure : Sound
    # VoiceEnterStateAttackMachine : Sound
    # VoiceEnterStateMove : Sound
    # VoiceEnterStateMoveToHigherGround : Sound
    # VoiceEnterStateMoveOverWalls : Sound
    # VoiceEnterStateRetreatToCastle : Sound
    # VoiceEnterStateMoveToCamp : Sound
    # VoiceEnterStateMoveWhileAttacking : Sound
    # SoundMoveStart : Sound
    # SoundMoveStartDamaged : Sound
    # SoundMoveLoop : Sound
    # SoundMoveLoopDamaged : Sound
    # SoundAmbient : Sound
    # SoundAmbientDamaged : Sound
    # SoundAmbientReallyDamaged : Sound
    # SoundAmbientRubble : Sound
    # SoundAmbientBattle : Sound
    # SoundStealthOn : Sound
    # SoundStealthOff : Sound
    # SoundCreated : Sound
    # SoundOnDamaged : Sound
    # SoundOnReallyDamaged : Sound
    # SoundEnter : Sound
    # SoundExit : Sound
    # SoundPromotedVeteran : Sound
    # SoundPromotedElite : Sound
    # SoundPromotedHero : Sound
    # SoundFallingFromPlane : Sound
    # SoundImpact : Sound
    # SoundImpactCyclonic : Sound
    # SoundCrushing : Sound

class ListUpgradeoundSelectorClientBehavior(Behavior):
    pass

class ModelConditionSoundSelectorClientBehavior(Behavior):
    pass

class AnimationSoundClientBehavior(Behavior):
    MaxUpdateRangeCap : Int

class RadarMarkerClientUpdate(Behavior):
    MarkerType : MarkerType

class BeaconClientUpdate(Behavior):
    RadarPulseFrequency : Int
    RadarPulseDuration : Int

class SwayClientUpdate(Behavior):
    pass

class AnimatedParticleSysBoneClientUpdate(Behavior):
    pass

class HordeDispatchSpecialPower(SpecialPowerModuleBehavior):
    pass

class CombineHordeSpecialPower(SpecialPowerModuleBehavior):
    ScanRange : Float

class RepairSpecialPower(SpecialPowerModuleBehavior):
    pass

class SplitHordeSpecialPower(SpecialPowerModuleBehavior):
    pass

class DevastateSpecialPower(SpecialPowerModuleBehavior):
    TreeValueMultiplier : Float
    TreeValueTotalCap : Float
    FireWeapon : String

class PlayerHealSpecialPower(SpecialPowerModuleBehavior):
    HealAmount : Float
    HealAsPercent : Bool
    HealAffects : List[KindOf]
    HealRadius : Float
    # HealFX : FXList
    HealOCL : "ObjectCreationList"

class PlayerUpgradeSpecialPower(SpecialPowerModuleBehavior):
    UpgradeName : "Upgrade"

class UntamedAllegianceSpecialPower(SpecialPowerModuleBehavior):
    pass

class ManTheWallsSpecialPower(SpecialPowerModuleBehavior):
    pass
    
class SpecialPowerBehavior(Behavior):
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
    SpecialObjectAttachToBone : "Object"
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
    # PackSound : Sound
    # UnpackSound : Sound
    # PrepSoundLoop : Sound
    # TriggerSound : Sound
    # ActiveLoopSound : Sound
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
    # ContactPointOverride : ???
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

class FellBeastSwoopPower(SpecialPowerBehavior):
    SpecialWeapon : "Weapon"
    WhichSpecialWeapon : Int

class WoundArrowUpdate(SpecialPowerBehavior):
    FleeDistance : Float
    ForbiddenConditions : SpecialPowerForbiddenUnpackConditions

class StopSpecialPower(SpecialPowerModuleBehavior):
    StopPowerTemplate : "SpecialPower"

class SiegeDeployHordeSpecialPower(Behavior):
    SpecialPowerTemplate : "SpecialPower"
    # InitiateSound : Sound
    StartsPaused : Bool
    HordeDeploy : Bool

class SiegeDeploySpecialPower(Behavior):
    SpecialPowerTemplate : "SpecialPower"
    # InitiateSound : Sound
    StartsPaused : Bool
    LowerDelay : Int
    RaiseDelay : Int
    EvacuatePassengersOnDeploy : Bool
    EvacuateCrewOnDeploy : Bool
    SkipAdjustPosition : Bool
    WallSearchDistance : Float
    AwayFromWallWaitDist : Float
    ExtraWallDistance : Float

class DeflectSpecialPower(Behavior):
    SpecialPowerTemplate : "SpecialPower"
    # InitiateSound : Sound
    StartsPaused : Bool

class GrabPassengerSpecialPower(SpecialPowerModuleBehavior):
    GrabRadius : Float
    AllowTree : Bool

class DarknessSpecialPower(SpecialPowerModuleBehavior):
    DarknessRadius : Float
    # DarknessFX : FXList

class FreezingRainSpecialPower(SpecialPowerModuleBehavior):
    FreezingRainRadius : Float
    # FreezingRainFX : FXList
    BurnRateModifier : Int

class TaintSpecialPower(SpecialPowerModuleBehavior):
    TaintObject : "Object"
    TaintRadius : Float
    # TaintFX : FXList
    TaintOCL : "ObjectCreationList"

class CloudBreakSpecialPower(SpecialPowerModuleBehavior):
    CloudBreakRadius : Float
    # CloudBreakFX : FXList
    SunbeamObject : "Object"
    ObjectSpacing : Float

class ScavengerSpecialPower(SpecialPowerModuleBehavior):
    BountyPercent : Float

class WeaponChangeSpecialPowerModule(SpecialPowerModuleBehavior):
    FlagsUsedForToggle : WeaponsetFlags
    ToggleOnSleepFrames : Int
    ToggleOffSleepFrames : Int
    ToggleOnAttributeModifier : "ModifierList"
    ToggleOffAttributeModifier : "ModifierList"

class ElvenWoodSpecialPower(SpecialPowerModuleBehavior):
    ElvenGroveObject : "Object"
    ElvenNumObjects : Int
    ElvenWoodObject : "Object"
    ElvenWoodRadius : Float
    # ElvenWoodFX : FXList
    ElvenWoodOCL : "ObjectCreationList"

class SpecialPowerTimerRefreshSpecialPower(SpecialPowerModuleBehavior):
    pass

class ProductionSpeedBonus(SpecialPowerModuleBehavior):
    NumberOfFrames : Int
    SpeedMulitplier : Float
    Type : List["Object"]

class LevelGrantSpecialPower(SpecialPowerBehavior):
    Experience : Int
    RadiusEffect : Float
    # LevelFX : FXList
    AcceptanceFilter : ObjectFilter

class DefectorSpecialPower(SpecialPowerModuleBehavior):
    FatCursorRadius : Float

class CashHackSpecialPower(SpecialPowerModuleBehavior):
    UpgradeMoneyAmount : Tuple["Science", Int]
    MoneyAmount : Int

class InvisibilitySpecialPower(SpecialPowerModuleBehavior):
    InvisibilityNugget : "InvisibilityNugget"
    BroadcastRadius : Float
    ObjectFilter : ObjectFilter
    Duration : Int
    
class Body(Behavior):
    MaxHealth : Float
    MaxHealthDamaged : Float
    MaxHealthReallyDamaged : Float
    InitialHealth : Float
    RecoveryTime : Int
    DodgePercent : Float
    EnteringDamagedTransitionTime : Int
    EnteringReallyDamagedTransitionTime : Int
    GrabObject : "Object"
    # GrabFX : FXList
    GrabDamage : Float
    GrabOffset : Coords
    UseDefaultDamageSettings : Bool
    DamageCreationList : Tuple["ObjectCreationList", FakeEnum, FakeEnum]
    # HealingBuffFx : FXList
    DamagedAttributeModifier : "ModifierList"
    ReallyDamagedAttributeModifier : "ModifierList"
    CheerRadius : Float
    RemoveUpgradesOnDeath : Bool
    BurningDeathBehavior : Bool
    # BurningDeathFX : FXList

class RespawnBody(Body):
    PermanentlyKilledByFilter : ObjectFilter
    CanRespawn : Bool

class PorcupineFormationBodyModule(Body):
    DamageWeaponTemplate : "Weapon"
    CrushDamageWeaponTemplate : "Weapon"
    CrusherLevelResisted : Int

class OathbreakerBody(Body):
    pass

class DetachableRiderBody(Body):
    TriggeredBy : List["Upgrade"]
    ConflictsWith : List["Upgrade"]
    RequiresAllTriggers : Bool
    RequiresAllConflictingTriggers : Bool
    # CustomAnimAndDuration : AnimAndDuration
    Permanent : Bool
    HealthFloatWhenRiderDies : Float
    StartsActive : Bool
    RiderlessDeathChance : Float

class FreeLifeBody(Behavior):
    PermanentlyKilledByFilter : ObjectFilter
    CanRespawn : Bool
    FreeLifeHealthPercent : Float
    FreeLifeTime : Int
    FreeLifeInvincible : Bool
    FreeLifePrerequisiteUpgrade : "Upgrade"
    # FreeLifeAnimAndDuration : AnimAndDuration

class DelayedDeathBody(Behavior):
    PermanentlyKilledByFilter : ObjectFilter
    CanRespawn : Bool
    DelayedDeathTime : Int
    ImmortalUntilDeathTime : Bool
    DoHealthCheck : Bool
    # InvulnerableFX : FXList
    DelayedDeathPrerequisiteUpgrade : "Upgrade"

class SymbioticStructuresBody(Body):
    Symbiote : "Object"

class StructureBody(Body):
    #I'll let you guess
    pass

class ImmortalBody(Body):
    #Can't take damage or die
    pass

class HighlanderBody(Body):
    #Can take damage, but won't die.  Can only die from ::kill() or other unresistable damage
    pass

class ActiveBody(Body):
    #unit body? I guess
    pass

class InactiveBody(Behavior):
    #nothing
    pass

class CivilianSpawnCollide(Behavior):
    DeleteObjectFilter : ObjectFilter
    
class CrateCollide(Behavior):
    RequiredKindOf : List[KindOf]
    ForbiddenKindOf : List[KindOf]
    ForbidOwnerPlayer : Bool
    BuildingPickup : Bool
    HumanOnly : Bool
    PickupScience : "Science" #Forces the player owning the unit trying to get the crate to have a certain science.
    # ExecuteFX : FXList
    # ExecuteAnimation : Animation
    ExecuteAnimationTime : Float
    ExecuteAnimationZRise : Float
    ExecuteAnimationFades : Bool

class SalvageCrateCollide(CrateCollide):
    PorterChance : Float
    BannerChance : Float
    LevelUpChance : Float
    LevelUpRadius : Float
    ResourceChance : Float
    Upgrade : "Upgrade"
    MinResource : Int
    MaxResource : Int
    AllowAIPickup : Bool

class VeterancyCrateCollide(CrateCollide):
    EffectRange : Int
    AddsOwnerVeterancy : Bool
    IsPilot : Bool
    AffectsUpToLevel : Int

class UnitCrateCollide(CrateCollide):
    UnitCount : Int
    UnitName : String

class ShroudCrateCollide(Behavior):
    pass

class MoneyCrateCollide(CrateCollide):
    MoneyProvided : Int

class HealCrateCollide(CrateCollide):
    pass

class HordeMemberCollide(Behavior):
    pass

class AODCrushCollide(Behavior):
    # SmallFXList : FXList
    SmallObjectCreationList : "ObjectCreationList"
    # MediumFXList : FXList
    MediumObjectCreationList : "ObjectCreationList"
    # LargeFXList : FXList
    LargeObjectCreationList : "ObjectCreationList"
    Damage : Float
    DamageType : DamageType
    DeathType : DeathType
    SpecialDamage : Float
    SpecialDamageType : DamageType
    SpecialDeathType : DeathType
    SelfDamage : Float
    SelfDamageType : DamageType
    SelfDeathType : DeathType
    SpecialObject : "Object"

class SquishCollide(Behavior):
    pass

class FireWeaponCollide(Behavior):
    CollideWeapon : "Weapon"
    FireOnce : Bool
    RequiredStatus : ObjectStatus
    ForbiddenStatus : ObjectStatus

class CallHelpOnDamage(Behavior):
    DamageTypes : DamageTypeFilter
    CallRadius : Float
    CallDelay : Int
    MoveToAttacker : Bool
    ValidObjects : ObjectFilter

class HordeTransportContainDamage(Behavior):
    pass

class EvacuateDamage(Behavior):
    WeaponThatCausesEvacuation : "Weapon"
    DamageTypeToTrack : DamageType
    DamageToPanicThreshold : Float
    TrackingTimeSpan : Int

class ReflectDamage(Behavior):
    DamageTypesToReflect : DamageTypeFilter
    ReflectDamageFloat : Float
    MinimumDamageToReflect : Float

class TransitionDamageFX(Behavior):
    DamageFXTypes : DamageTypeFilter
    DamageOCLTypes : DamageTypeFilter
    DamageParticleTypes : DamageTypeFilter
    # DamagedFXList1 : FXList
    # DamagedFXList2 : FXList
    # DamagedFXList3 : FXList
    # DamagedFXList4 : FXList
    # DamagedFXList5 : FXList
    # DamagedFXList6 : FXList
    # DamagedFXList7 : FXList
    # DamagedFXList8 : FXList
    # DamagedFXList9 : FXList
    # DamagedFXList10 : FXList
    # DamagedFXList11 : FXList
    # DamagedFXList12 : FXList
    # ReallyDamagedFXList1 : FXList
    # ReallyDamagedFXList2 : FXList
    # ReallyDamagedFXList3 : FXList
    # ReallyDamagedFXList4 : FXList
    # ReallyDamagedFXList5 : FXList
    # ReallyDamagedFXList6 : FXList
    # ReallyDamagedFXList7 : FXList
    # ReallyDamagedFXList8 : FXList
    # ReallyDamagedFXList9 : FXList
    # ReallyDamagedFXList10 : FXList
    # ReallyDamagedFXList11 : FXList
    # ReallyDamagedFXList12 : FXList
    # RubbleFXList1 : FXList
    # RubbleFXList2 : FXList
    # RubbleFXList3 : FXList
    # RubbleFXList4 : FXList
    # RubbleFXList5 : FXList
    # RubbleFXList6 : FXList
    # RubbleFXList7 : FXList
    # RubbleFXList8 : FXList
    # RubbleFXList9 : FXList
    # RubbleFXList10 : FXList
    # RubbleFXList11 : FXList
    # RubbleFXList12 : FXList
    DamagedOCL1 : "ObjectCreationList"
    DamagedOCL2 : "ObjectCreationList"
    DamagedOCL3 : "ObjectCreationList"
    DamagedOCL4 : "ObjectCreationList"
    DamagedOCL5 : "ObjectCreationList"
    DamagedOCL6 : "ObjectCreationList"
    DamagedOCL7 : "ObjectCreationList"
    DamagedOCL8 : "ObjectCreationList"
    DamagedOCL9 : "ObjectCreationList"
    DamagedOCL10 : "ObjectCreationList"
    DamagedOCL11 : "ObjectCreationList"
    DamagedOCL12 : "ObjectCreationList"
    ReallyDamagedOCL1 : "ObjectCreationList"
    ReallyDamagedOCL2 : "ObjectCreationList"
    ReallyDamagedOCL3 : "ObjectCreationList"
    ReallyDamagedOCL4 : "ObjectCreationList"
    ReallyDamagedOCL5 : "ObjectCreationList"
    ReallyDamagedOCL6 : "ObjectCreationList"
    ReallyDamagedOCL7 : "ObjectCreationList"
    ReallyDamagedOCL8 : "ObjectCreationList"
    ReallyDamagedOCL9 : "ObjectCreationList"
    ReallyDamagedOCL10 : "ObjectCreationList"
    ReallyDamagedOCL11 : "ObjectCreationList"
    ReallyDamagedOCL12 : "ObjectCreationList"
    RubbleOCL1 : "ObjectCreationList"
    RubbleOCL2 : "ObjectCreationList"
    RubbleOCL3 : "ObjectCreationList"
    RubbleOCL4 : "ObjectCreationList"
    RubbleOCL5 : "ObjectCreationList"
    RubbleOCL6 : "ObjectCreationList"
    RubbleOCL7 : "ObjectCreationList"
    RubbleOCL8 : "ObjectCreationList"
    RubbleOCL9 : "ObjectCreationList"
    RubbleOCL10 : "ObjectCreationList"
    RubbleOCL11 : "ObjectCreationList"
    RubbleOCL12 : "ObjectCreationList"
    # DamagedParticleSystem1 : ParticleSystem
    # DamagedParticleSystem2 : ParticleSystem
    # DamagedParticleSystem3 : ParticleSystem
    # DamagedParticleSystem4 : ParticleSystem
    # DamagedParticleSystem5 : ParticleSystem
    # DamagedParticleSystem6 : ParticleSystem
    # DamagedParticleSystem7 : ParticleSystem
    # DamagedParticleSystem8 : ParticleSystem
    # DamagedParticleSystem9 : ParticleSystem
    # DamagedParticleSystem10 : ParticleSystem
    # DamagedParticleSystem11 : ParticleSystem
    # DamagedParticleSystem12 : ParticleSystem
    # ReallyDamagedParticleSystem1 : ParticleSystem
    # ReallyDamagedParticleSystem2 : ParticleSystem
    # ReallyDamagedParticleSystem3 : ParticleSystem
    # ReallyDamagedParticleSystem4 : ParticleSystem
    # ReallyDamagedParticleSystem5 : ParticleSystem
    # ReallyDamagedParticleSystem6 : ParticleSystem
    # ReallyDamagedParticleSystem7 : ParticleSystem
    # ReallyDamagedParticleSystem8 : ParticleSystem
    # ReallyDamagedParticleSystem9 : ParticleSystem
    # ReallyDamagedParticleSystem10 : ParticleSystem
    # ReallyDamagedParticleSystem11 : ParticleSystem
    # ReallyDamagedParticleSystem12 : ParticleSystem
    # RubbleParticleSystem1 : ParticleSystem
    # RubbleParticleSystem2 : ParticleSystem
    # RubbleParticleSystem3 : ParticleSystem
    # RubbleParticleSystem4 : ParticleSystem
    # RubbleParticleSystem5 : ParticleSystem
    # RubbleParticleSystem6 : ParticleSystem
    # RubbleParticleSystem7 : ParticleSystem
    # RubbleParticleSystem8 : ParticleSystem
    # RubbleParticleSystem9 : ParticleSystem
    # RubbleParticleSystem10 : ParticleSystem
    # RubbleParticleSystem11 : ParticleSystem
    # RubbleParticleSystem12 : ParticleSystem
    # RubbleNeighbor : ???
    PristineShowSubObject : List["SubObject"]
    PristineHideSubObject : List["SubObject"]
    DamagedShowSubObject : List["SubObject"]
    DamagedHideSubObject : List["SubObject"]
    ReallyDamagedShowSubObject : List["SubObject"]
    ReallyDamagedHideSubObject : List["SubObject"]
    RubbleShowSubObject : List["SubObject"]
    RubbleHideSubObject : List["SubObject"]

class BoneFXDamage(Behavior):
    pass

class InheritUpgradeCreate(Behavior):
    Radius : Float
    Upgrade : List["Upgrade"]
    ObjectFilter : ObjectFilter

class ExperienceLevelCreate(Behavior):
    LevelToGrant : Int
    MPOnly : Bool

class GrantUpgradeCreate(Behavior):
    UpgradeToGrant : "Upgrade"
    ExemptStatus : ObjectStatus
    GiveOnBuildComplete : Bool

class SpecialPowerCreate(Behavior):
    pass

class SupplyWarehouseCreate(Behavior):
    pass

class SupplyCenterCreate(Behavior):
    pass

class SpawnedModelConditionCreate(Behavior):
    # SpawnerTrigger : ???
    pass

class PreorderCreate(Behavior):
    pass

class LockWeaponCreate(Behavior):
    SlotToLock : SlotTypes

class ActivateModuleSpecialPower(SpecialPowerBehavior):
    TriggerSpecialPower : "SpecialPower"

class PillageModule(Behavior):
    PillageAmount : Int
    NumDamageEventsPerPillage : Int
    PillageFilter : ObjectFilter

class GiveOrRestoreUpgradeSpecialPower(SpecialPowerBehavior):
    CommandButton : "CommandButton"
    UpgradeToGive : "Upgrade"
    FlagsUsedForToggle : WeaponsetFlags

class CurseSpecialPower(SpecialPowerBehavior):
    # TriggerFX : FXList
    # CursedFX : FXList
    CurseFloat : Float

class EvacuateGarrisonSpecialPower(SpecialPowerBehavior):
    pass

class UnleashSpecialPower(SpecialPowerBehavior):
    pass

class StoreObjectsSpecialPower(SpecialPowerBehavior):
    Radius : Float

class TemporarilyDefectUpdate(Behavior):
    DefectDuration : Int

class TeleportToCasterSpecialPower(SpecialPowerBehavior):
    Radius : Float
    MinDestinationRadius : Float
    MaxDestinationRadius : Float
    # TriggerFX : FXList
    # TargetFX : FXList

class DominateEnemySpecialPower(SpecialPowerBehavior):
    DominateRadius : Float
    # TriggerFX : FXList
    # DominatedFX : FXList
    PermanentlyConvert : Bool
    AttributeModifierAffects : ObjectFilter

class PassiveAreaEffectBehavior(Behavior):
    EffectRadius : Float
    PingDelay : Int
    HealPercentPerSecond : Float
    ModifierName : List["ModifierList"]
    AllowFilter : ObjectFilter
    UpgradeRequired : "Upgrade"
    NonStackable : Bool
    AntiCategories : ModifierCategories
    # AntiFX : FXList
    # HealFX : FXList

class CommandPointsUpgrade(UpgradeBehavior):
    CommandPoints : Int
    RequiredObject : ObjectFilter

class AllowBannerSpawnUpgrade(UpgradeBehavior):
    pass

class BuildableHeroListUpgrade(UpgradeBehavior):
    pass

class RemoveUpgradeUpgrade(UpgradeBehavior):
    UpgradeToRemove : List["Upgrade"]
    # UpgradeGroupsToRemove : Strings #TODO
    SuppressEvaEventForRemoval : Bool
    RemoveFromAllPlayerObjects : Bool

class AudioLoopUpgrade(UpgradeBehavior):
    DeathType : DeathTypeFilter
    ExemptStatus : ObjectStatus
    RequiredStatus : ObjectStatus
    DamageAmountRequired : Float
    MinKillerAngle : Degrees
    MaxKillerAngle : Degrees
    # SoundToPlay : Sound
    KillAfterMS : Int
    KillOnDeath : Bool

class TooltipUpgrade(UpgradeBehavior):
    DisplayName : String
    Description : String

class GarrisonUpgrade(UpgradeBehavior):
    pass

class ReplaceSelfUpgrade(UpgradeBehavior):
    ReplaceWith : List["Upgrade"]
    AndThenAddA : List["Upgrade"]

class GeometryUpgrade(UpgradeBehavior):
    # ShowGeometry : Strings
    # HideGeometry : Strings
    # WallBoundsMesh : String
    # RampMesh1 : String
    # RampMesh2 : String
    pass

class CastleUpgrade(UpgradeBehavior):
    Upgrade : "Upgrade"
    WallUpgradeRadius : Float

class AttributeModifierUpgrade(UpgradeBehavior):
    AttributeModifier : "ModifierList"

class ModelConditionUpgrade(UpgradeBehavior):
    AddConditionFlags : List[ModelCondition]
    RemoveConditionFlags : List[ModelCondition]
    RemoveConditionFlagsInRange : Tuple[ModelCondition, ModelCondition]
    # AddTempConditionFlag : KeyValuePair
    TempConditionTime : Float

class MaxHealthUpgrade(UpgradeBehavior):
    AddMaxHealth : Float
    ChangeType : HealthOperation

class ExperienceScalarUpgrade(UpgradeBehavior):
    AddXPScalar : Float

class WeaponSetUpgrade(UpgradeBehavior):
    WeaponCondition : WeaponsetFlags

class WeaponBonusUpgrade(UpgradeBehavior):
    pass

class UnpauseSpecialPowerUpgrade(UpgradeBehavior):
    SpecialPowerTemplate : "SpecialPower"
    ObeyRechageOnTrigger : Bool

class ObjectCreationUpgrade(UpgradeBehavior):
    UpgradeObject : "ObjectCreationList"
    Delay : Int
    RemoveUpgrade : "Upgrade"
    GrantUpgrade : "Upgrade"
    ThingToSpawn : "Upgrade"
    Offset : Coords
    Angle : Degrees
    DestroyWhenSold : Bool
    # DeathAnimAndDuration : AnimAndDuration
    FadeInTime : Int
    UseBuildingProduction : Bool

class LocomotorSetUpgrade(UpgradeBehavior):
    KillLocomotorUpgrade : Bool

class RadarUpgrade(UpgradeBehavior):
    DisableProof : Bool

class StealthUpgrade(UpgradeBehavior):
    pass

class SubObjectsUpgrade(UpgradeBehavior):
    # ShowSubObjects : Strings
    # HideSubObjects : Strings
    # UpgradeTexture : TextureReplacement
    FadeTimeInSeconds : Float
    WaitBeforeFadeInSeconds : Float
    RecolorHouse : Bool
    # ExcludeSubobjects : Strings
    SkipFadeOnCreate : Bool
    HideSubObjectsOnRemove : Bool
    UnHideSubObjectsOnRemove : Bool

class ArmorUpgrade(UpgradeBehavior):
    ArmorSetFlag : ArmorSetFlags

class DoCommandUpgrade(UpgradeBehavior):
    GetUpgradeCommandButtonName : String
    RemoveUpgradeCommandButtonName : String

class StatusBitsUpgradeIfEldestKindof(UpgradeBehavior):
    StatusToSet : ObjectStatus
    StatusToClear : ObjectStatus
    ObjectFilter : ObjectFilter

class StatusBitsUpgrade(UpgradeBehavior):
    StatusToSet : ObjectStatus
    StatusToClear : ObjectStatus

class LevelUpUpgrade(UpgradeBehavior):
    LevelsToGain : Int
    LevelCap : Int

class DelayedUpgrade(UpgradeBehavior):
    DelayTime : Int

class CommandSetUpgrade(UpgradeBehavior):
    CommandSet : String

class BaseUpgrade(UpgradeBehavior):
    BuildingTemplateName : String
    PlacementPrefix : String
    PlacementIndex : Int

class SpellRechargeModifierUpgrade(UpgradeBehavior):
    Float : Float
    StartsActive : Bool
    LabelForPalantirString : String
    ObjectFilter : ObjectFilter
    UpgradeDiscount : Bool
    ApplyToTheseUpgrades : List["Upgrade"]
    Slaughter : Bool

class AISpecialPowerUpdate(Behavior):
    CommandButtonName : "CommandButton"
    # SpecialPowerAIType : ???
    SpecialPowerRadius : Float
    SpecialPowerRange : Float
    RandomizeTargetLocation : Bool
    SpellMakesAStructure : Bool

class ReplaceObjectUpdate(SpecialPowerBehavior):
    ReplaceRadius : Float
    # ReplaceFX : FXList
    Scatter : Bool
    
    # ReplaceObject : List["ReplaceObject"]
    nested_attributes = {"ReplaceObject":["ReplaceObject"]}

class ProjectileStreamUpdate(Behavior):
    pass

class ThreatFinderUpdate(Behavior):
    DefaultRadius : Float

class EmotionTrackerUpdate(Behavior):
    TauntAndPointDistance : Float
    TauntAndPointUpdateDelay : Int
    TauntAndPointExcluded : ObjectFilter
    AfraidOf : ObjectFilter
    AlwaysAfraidOf : ObjectFilter
    PointAt : ObjectFilter
    HeroScanDistance : Float
    FearScanDistance : Float
    QuarrelProbability : Float
    IgnoreVeterancy : Bool
    ImmuneToFearLevel : Int
    AddEmotion : List["Emotion"]

class SpecialDisguiseUpdate(SpecialPowerBehavior):
    OpacityTarget : Float
    TriggerInstantlyOnCreate : Bool
    DisguiseAsTemplate : "Object"
    DisguisedAsTemplate_EnemyPerspec : "Object"
    # DisguiseFX : FXList
    ForceMountedWhenDisguising : Bool

class AttributeModifierPoolUpdate(Behavior):
    pass

class BloodthirstyUpdate(Behavior):
    SacrificeFilter : ObjectFilter
    ExperienceModifier : Float
    # InitiateVoice : Sound

class RespawnUpdate(Behavior):
    DeathAnim : ModelCondition
    # DeathFX : FXList
    DeathAnimationTime : Int
    InitialSpawnAnim : ModelCondition
    # InitialSpawnFX : FXList
    InitialSpawnAnimationTime : Int
    RespawnAnim : ModelCondition
    # RespawnFX : FXList
    RespawnAnimationTime : Int
    AutoRespawnAtObjectFilter : ObjectFilter
    # RespawnRules : None #TODO
    # RespawnEntry : None
    # ButtonImage : Image
    RespawnAsTemplate : "Object"

class DetachableRiderUpdate(Behavior):
    RiderSubObjects : List["Object"]
    RiderlessWeaponSlot : SlotTypes
    RiderlessHordeFlees : Bool
    # DeathEntry : None #TODO
    RemoveRiderlessFromHorde : Bool

class WallUpgradeUpdate(Behavior):
    pass
    
class AIUpdateBehavior(Behavior):
    # AttackPriority : String
    # AutoAcquireEnemiesWhenIdle : AllowedWhenConditions
    StopChaseDistance : Float
    StandGround : Bool
    MoodAttackCheckRate : Int
    CanAttackWhileContained : Bool
    HoldGroundCloseRangeDistance : Float
    # AILuaEventsList : String
    MinCowerTime : Int
    MaxCowerTime : Int
    RampageTime : Int
    RampageRequiresAflame : Bool
    BurningDeathTime : Int
    TimeToEjectPassengersOnRampage : Int
    # ComboLocomotorSet : LocomotorSetType
    ComboLocoAttackDistance : Float
    # SpecialContactPoints : Strings
    FadeOnPortals : Bool
    
    nested_attributes = {"Turret": ["TurretModule"]}

class WorkerAIUpdate(AIUpdateBehavior):
    MaxBoxes : Int
    RepairHealthPercentPerSecond : Float
    BoredTime : Int
    BoredRange : Float
    SupplyCenterActionDelay : Int
    SupplyWarehouseActionDelay : Int
    SupplyWarehouseScanDistance : Float
    HarvestTrees : Bool
    # SuppliesDepletedVoice : Sound
    HarvestActivationRange : Float
    HarvestPreparationTime : Int
    HarvestActionTime : Int

class FoundationAIUpdate(Behavior):
    RepairHealthPercentPerSecond : Float
    BuildVariation : Int

class AnimalAIUpdate(AIUpdateBehavior):
    FleeRange : Int
    FleeDistance : Int
    WanderFloat : Int
    MaxWanderDistance : Int
    MaxWanderRadius : Int
    UpdateTimer : Int
    AfraidOfCastles : Bool

class WanderAIUpdate(AIUpdateBehavior):
    WildBeast : Bool
    # ConditionForEntry : ContainCondition
    Selectable : Bool
    WanderDistance : Int

class TransportAIUpdate(AIUpdateBehavior):
    pass

class RadarUpdate(Behavior):
    RadarExtendTime : Int

class BoneFXUpdate(Behavior):
    DamageFXTypes : DamageTypeFilter
    DamageOCLTypes : DamageTypeFilter
    DamageParticleTypes : DamageTypeFilter
    # PristineFXList1 : FXList
    # PristineFXList2 : FXList
    # PristineFXList3 : FXList
    # PristineFXList4 : FXList
    # PristineFXList5 : FXList
    # PristineFXList6 : FXList
    # PristineFXList7 : FXList
    # PristineFXList8 : FXList
    # DamagedFXList1 : FXList
    # DamagedFXList2 : FXList
    # DamagedFXList3 : FXList
    # DamagedFXList4 : FXList
    # DamagedFXList5 : FXList
    # DamagedFXList6 : FXList
    # DamagedFXList7 : FXList
    # DamagedFXList8 : FXList
    # ReallyDamagedFXList1 : FXList
    # ReallyDamagedFXList2 : FXList
    # ReallyDamagedFXList3 : FXList
    # ReallyDamagedFXList4 : FXList
    # ReallyDamagedFXList5 : FXList
    # ReallyDamagedFXList6 : FXList
    # ReallyDamagedFXList7 : FXList
    # ReallyDamagedFXList8 : FXList
    # RubbleFXList1 : FXList
    # RubbleFXList2 : FXList
    # RubbleFXList3 : FXList
    # RubbleFXList4 : FXList
    # RubbleFXList5 : FXList
    # RubbleFXList6 : FXList
    # RubbleFXList7 : FXList
    # RubbleFXList8 : FXList
    PristineOCL1 : "ObjectCreationList"
    PristineOCL2 : "ObjectCreationList"
    PristineOCL3 : "ObjectCreationList"
    PristineOCL4 : "ObjectCreationList"
    PristineOCL5 : "ObjectCreationList"
    PristineOCL6 : "ObjectCreationList"
    PristineOCL7 : "ObjectCreationList"
    PristineOCL8 : "ObjectCreationList"
    DamagedOCL1 : "ObjectCreationList"
    DamagedOCL2 : "ObjectCreationList"
    DamagedOCL3 : "ObjectCreationList"
    DamagedOCL4 : "ObjectCreationList"
    DamagedOCL5 : "ObjectCreationList"
    DamagedOCL6 : "ObjectCreationList"
    DamagedOCL7 : "ObjectCreationList"
    DamagedOCL8 : "ObjectCreationList"
    ReallyDamagedOCL1 : "ObjectCreationList"
    ReallyDamagedOCL2 : "ObjectCreationList"
    ReallyDamagedOCL3 : "ObjectCreationList"
    ReallyDamagedOCL4 : "ObjectCreationList"
    ReallyDamagedOCL5 : "ObjectCreationList"
    ReallyDamagedOCL6 : "ObjectCreationList"
    ReallyDamagedOCL7 : "ObjectCreationList"
    ReallyDamagedOCL8 : "ObjectCreationList"
    RubbleOCL1 : "ObjectCreationList"
    RubbleOCL2 : "ObjectCreationList"
    RubbleOCL3 : "ObjectCreationList"
    RubbleOCL4 : "ObjectCreationList"
    RubbleOCL5 : "ObjectCreationList"
    RubbleOCL6 : "ObjectCreationList"
    RubbleOCL7 : "ObjectCreationList"
    RubbleOCL8 : "ObjectCreationList"
    # PristineParticleSystem1 : ParticleSystem
    # PristineParticleSystem2 : ParticleSystem
    # PristineParticleSystem3 : ParticleSystem
    # PristineParticleSystem4 : ParticleSystem
    # PristineParticleSystem5 : ParticleSystem
    # PristineParticleSystem6 : ParticleSystem
    # PristineParticleSystem7 : ParticleSystem
    # PristineParticleSystem8 : ParticleSystem
    # DamagedParticleSystem1 : ParticleSystem
    # DamagedParticleSystem2 : ParticleSystem
    # DamagedParticleSystem3 : ParticleSystem
    # DamagedParticleSystem4 : ParticleSystem
    # DamagedParticleSystem5 : ParticleSystem
    # DamagedParticleSystem6 : ParticleSystem
    # DamagedParticleSystem7 : ParticleSystem
    # DamagedParticleSystem8 : ParticleSystem
    # ReallyDamagedParticleSystem1 : ParticleSystem
    # ReallyDamagedParticleSystem2 : ParticleSystem
    # ReallyDamagedParticleSystem3 : ParticleSystem
    # ReallyDamagedParticleSystem4 : ParticleSystem
    # ReallyDamagedParticleSystem5 : ParticleSystem
    # ReallyDamagedParticleSystem6 : ParticleSystem
    # ReallyDamagedParticleSystem7 : ParticleSystem
    # ReallyDamagedParticleSystem8 : ParticleSystem
    # RubbleParticleSystem1 : ParticleSystem
    # RubbleParticleSystem2 : ParticleSystem
    # RubbleParticleSystem3 : ParticleSystem
    # RubbleParticleSystem4 : ParticleSystem
    # RubbleParticleSystem5 : ParticleSystem
    # RubbleParticleSystem6 : ParticleSystem
    # RubbleParticleSystem7 : ParticleSystem
    # RubbleParticleSystem8 : ParticleSystem

class RubbleRiseUpdate(Behavior):
    MinRubbleRiseDelay : Int
    MaxRubbleRiseDelay : Int
    MinBurstDelay : Int
    MaxBurstDelay : Int
    RubbleRiseDamping : Float
    RubbleHeight : Float
    MaxShudder : Float
    BigBurstFrequency : Int
    OCL : "ObjectCreationList"
    # FXList : FXList
    DeathType : DeathTypeFilter
    ExemptStatus : ObjectStatus
    RequiredStatus : ObjectStatus
    DamageAmountRequired : Float
    MinKillerAngle : Degrees
    MaxKillerAngle : Degrees

class StructureCollapseUpdate(Behavior):
    MinCollapseDelay : Int
    MaxCollapseDelay : Int
    MinBurstDelay : Int
    MaxBurstDelay : Int
    CollapseDamping : Float
    MaxShudder : Float
    BigBurstFrequency : Int
    OCL : "ObjectCreationList"
    # FXList : FXList
    DestroyObjectWhenDone : Bool
    CollapseHeight : Float
    DeathType : DeathTypeFilter
    ExemptStatus : ObjectStatus
    RequiredStatus : ObjectStatus
    DamageAmountRequired : Float
    MinKillerAngle : Degrees
    MaxKillerAngle : Degrees

class StructureToppleUpdate(Behavior):
    MinToppleDelay : Int
    MaxToppleDelay : Int
    MinToppleBurstDelay : Int
    MaxToppleBurstDelay : Int
    ToppleAccelerationFactor : Float
    StructuralIntegrity : Float
    StructuralDecay : Float
    DamageFXTypes : DamageTypeFilter
    # TopplingFX : FXList
    # ToppleDelayFX : FXList
    # ToppleStartFX : FXList
    # ToppleDoneFX : FXList
    # CrushingFX : FXList
    CrushingWeaponName : "Weapon"
    ForceToppleAngle : Float
    OCL : "ObjectCreationList"
    # AngleFX : FXList
    DeathType : DeathTypeFilter
    ExemptStatus : ObjectStatus
    RequiredStatus : ObjectStatus
    DamageAmountRequired : Float
    MinKillerAngle : Degrees
    MaxKillerAngle : Degrees

class FadeAndDieOrnamentUpdate(Behavior):
    # AttachToTargetBone : String
    # Envelope : None
    # FollowTarget : None
    pass

class HijackerUpdate(Behavior):
    # AttachToTargetBone : Bone
    pass

class ProneUpdate(Behavior):
    DamageToFramesRatio : Float

class ProductionUpdate(Behavior):
    MaxQueueEntries : Int
    NumDoorAnimations : Int
    DoorOpeningTime : Int
    DoorWaitOpenTime : Int
    DoorCloseTime : Int
    ConstructionCompleteDuration : Int
    GiveNoXP : Bool
    UnitInvulnerableTime : Int
    SpecialPrepModelconditionTime : Int
    VeteranUnitsFromVeteranFactory : Bool
    SetBonusModelConditionOnSpeedBon : Bool
    BonusForType : List["Object"] #list of object affected by Production speed increases, if not defined then everything produced by this object is affected by the production bonus
    # SpeedBonusAudioLoop : Sound
    SecondaryQueue : Bool

class GloriousChargeUpdate(SpecialPowerBehavior):
    BonusRadius : Float
    SpeechDuration : Int
    UpdateInterval : Int

class RousingSpeechUpdate(SpecialPowerBehavior):
    BonusRadius : Float
    SpeechDuration : Int
    UpdateInterval : Int
    # LeaderFX : FXList
    # FollowerFX : FXList
    CreateWave : Bool
    WaveWidth : Float
    ModifierName : List["AttributeModifier"]
    LevelUp : Bool
    ObjectFilter : ObjectFilter

class DozerAIUpdate(AIUpdateBehavior):
    RepairHealthPercentPerSecond : Float
    BoredTime : Int
    BoredRange : Float

class MonsterDockUpdate(Behavior):
    NumberApproachPositions : Int
    AllowsPassthrough : Bool
    DockableObjectFilter : ObjectFilter
    DockedAnimationTime : Int

class SupplyWarehouseDockUpdate(Behavior):
    NumberApproachPositions : Int
    AllowsPassthrough : Bool
    StartingBoxes : Int
    DeleteWhenEmpty : Bool

class SupplyCenterDockUpdate(Behavior):
    NumberApproachPositions : Int
    AllowsPassthrough : Bool
    ValueMultiplier : Float
    BonusScience : "Science"
    BonusScienceMultiplier : Float

class SupplyCenterProductionExitUpdate(Behavior):
    UnitCreatePoint : Coords
    NaturalRallyPoint : Coords

class SpecialAbilityUpdate(SpecialPowerBehavior):
    pass

class RadiateFearUpdate(UpgradeBehavior):
    InitiallyActive : Bool
    WhichSpecialPower : Int
    GenerateTerror : Bool
    GenerateFear : Bool
    GenerateUncontrollableFear : Bool
    EmotionPulseRadiusl : Float
    EmotionPulseInterval : Int
    VictimFilter : ObjectFilter

class OCLUpdate(Behavior):
    OCL : "ObjectCreationList"
    MinDelay : Int
    MaxDelay : Int
    CreateAtEdge : Bool
    Amount : Int

class SlavedUpdate(Behavior):
    LeashRange : Int
    GuardMaxRange : Int
    GuardWanderRange : Int
    AttackRange : Int
    AttackWanderRange : Int
    ScoutRange : Int
    ScoutWanderRange : Int
    RepairRange : Int
    RepairMinAltitude : Float
    RepairMaxAltitude : Float
    DistToTargetToGrantRangeBonus : Int
    RepairRatePerSecond : Float
    RepairWhenBelowHealth_ : Int
    RepairMinReadyTime : Int
    RepairMaxReadyTime : Int
    RepairMinWeldTime : Int
    RepairMaxWeldTime : Int
    # RepairWeldingSys : String
    # RepairWeldingFXBone : String
    StayOnSameLayerAsMaster : Bool
    UseSlaverAsControlForEvaObjectSightedEvents : Bool
    DieOnMastersDeath : Bool
    GuardPositionOffset : Coords
    FadeOutRange : Int
    FadeTime : Int
    MarkUnselectable : Bool

class SpawnPointProductionExitUpdate(Behavior):
    # SpawnPointBoneName : String
    pass

class DefaultProductionExitUpdate(Behavior):
    UnitCreatePoint : Coords
    NaturalRallyPoint : Coords

class SummonReplacementSpecialAbilityUpdate(SpecialPowerBehavior):
    WhichSpecialPower : Int
    GenerateTerror : Bool
    GenerateUncontrollableFear : Bool
    EmotionPulseRadius : Float
    ObjectFilter : ObjectFilter
    OpacityTarget : Float
    TriggerInstantlyOnCreate : Bool
    CancelDisguiseWhenDismounting : Bool
    MountedTemplate : "Object"
    SynchronizeTimerOnSpecialPower : List["SpecialPower"]

class PickupStuffUpdate(Behavior):
    SkirmishAIOnly : Bool
    ScanRange : Float
    StuffToPickUp : ObjectFilter
    ScanIntervalSeconds : Float

class AttachUpdate(Behavior):
    ObjectFilter : ObjectFilter
    ScanRange : Float
    ParentStatus : ObjectStatus
    AlwaysTeleport : Bool
    AnchorToTopOfGeometry : Bool
    # ParentOwnerAttachmentEvaEvent : EvaEvent
    # ParentAllyAttachmentEvaEvent : EvaEvent
    # ParentEnemyAttachmentEvaEvent : EvaEvent
    # AttachFX : FXList
    # ParentOwnerDiedEvaEvent : EvaEvent
    # ParentAllyDiedEvaEvent : EvaEvent
    # ParentEnemyDiedtEvaEvent : EvaEvent

class HordeNotifyTargetsOfImminentProbableCrushingUpdate(Behavior):
    TimeBetweenUpdatesMS : Int
    ScanAheadTimeMS : Int
    ScanHeight : Float
    ScanWidth : Float

class NotifyTargetsOfImminentProbableCrushingUpdate(Behavior):
    TimeBetweenUpdatesMS : Int
    ScanAheadTimeMS : Int
    ScanHeight : Float
    ScanWidth : Float

class LargeGroupAudioUpdate(Behavior):
    TimeBetweenUpdatesMin : Int
    TimeBetweenUpdatesVariation : Int
    UnitWeight : Int
    # Key : List["???"]

class GiveUpgradeUpdate(SpecialPowerBehavior):
    # GiveUpgradeEffect : FXList
    # SpawnOutFX : FXList
    FadeOutSpeed : Float
    DeliverUpgrade : Bool

class FlingPassengerSpecialAbilityUpdate(SpecialPowerBehavior):
    FlingPassengerVelocity : Coords
    FlingPassengerLandingWarhead : "Weapon"

class ScaleWallSpecialAbilityUpdate(SpecialPowerBehavior):
    DelayAtFootOfWall : Int

class WeaponSetSpecialAbilityUpdate(SpecialPowerBehavior):
    WeaponsetEffectDuration : Int
    WhichWeaponSet : Int

class TeleportSpecialAbilityUpdate(SpecialPowerBehavior):
    HeroAttributeModifier : "ModifierList"
    HeroEffectDuration : Int
    UseUSERModelcondition : Bool
    StopUnitBeforeActivating : Bool

class WeaponFireSpecialAbilityUpdate(SpecialPowerBehavior):
    SpecialWeapon : "Weapon"
    WhichSpecialWeapon : Int
    SkipContinue : Bool
    BusyForDuration : Int
    NeedLivingTargets : Bool
    PlayWeaponPreFireFX : Bool

class ToggleDeploySpecialAbilityUpdate(SpecialPowerBehavior):
    # SoundDeploy : Sound
    # SoundUndeploy : Sound
    pass

class ToggleHiddenSpecialAbilityUpdate(SpecialPowerBehavior):
    ShowPalantirTimer : Bool

class ToggleMountedSpecialAbilityUpdate(SpecialPowerBehavior):
    OpacityTarget : Float
    TriggerInstantlyOnCreate : Bool
    CancelDisguiseWhenDismounting : Bool
    MountedTemplate : "Object"
    SynchronizeTimerOnSpecialPower : List["SpecialPower"]

class StrafeAreaUpdate(Behavior):
    WeaponName : "Weapon"
    StrafeAreaRadius : Float
    Sweepfrequency : Float
    SweepAmplitude : Float
    Slope : Float
    InitialSweepPhase : Float

class ModelConditionSpecialAbilityUpdate(SpecialPowerBehavior):
    WhichSpecialPower : Int
    GenerateTerror : Bool
    GenerateUncontrollableFear : Bool
    EmotionPulseRadius : Float
    ObjectFilter : ObjectFilter

class WeaponModeSpecialPowerUpdate(Behavior):
    SpecialPowerTemplate : "SpecialPower"
    # InitiateSound : Sound
    StartsPaused : Bool
    Duration : Int
    AttributeModifier : "ModifierList"
    LockWeaponSlot : SlotTypes
    WeaponSetFlags : WeaponsetFlags

class ArrowStormUpdate(SpecialPowerBehavior):
    WeaponTemplate : "Weapon"
    TargetRadius : Float
    ShotsPerTarget : Int
    ShotsPerBurst : Int
    MaxShots : Int
    CanShootEmptyGround : Bool

class RepairDockUpdate(Behavior):
    NumberApproachPositions : Int
    AllowsPassthrough : Bool
    TimeForFullHeal : Int

class QueueProductionExitUpdate(Behavior):
    UnitCreatePoint : Coords
    PlacementViewAngle : Degrees
    NaturalRallyPoint : Coords
    ExitDelay : Int
    AllowAirborneCreation : Bool
    InitialBurst : Int
    NoExitPath : Bool
    CanRallyToSlaughter : Bool
    UseReturnToFormation : Bool

class GateBehavior(Behavior):
    OpenByDefault : Bool
    ResetTimeInMilliseconds : Int
    PercentOpenForPathing : Int
    # Proxy : String
    RepelCollidingUnits : Bool
    # GeometryForOpen : Strings
    # GeometryForClosed : Strings
    # SoundOpeningGateLoop : Sound
    # SoundFinishedOpeningGate : Sound
    # SoundClosingGateLoop : Sound
    # SoundFinishedClosingGate : Sound
    TimeBeforePlayingOpenSound : Int
    TimeBeforePlayingClosedSound : Int

class GateProxyBehavior(GateBehavior):
    pass

class GateOpenAndCloseBehavior(GateBehavior):
    pass

class BattlePlanUpdate(Behavior):
    SpecialPowerTemplate : "SpecialPower"
    BombardmentPlanAnimationTime : Int
    HoldTheLinePlanAnimationTime : Int
    SearchAndDestroyPlanAnimationTime : Int
    TransitionIdleTime : Int
    # BombardmentPlanUnpackSoundName : Sound
    # BombardmentPlanPackSoundName : Sound
    # BombardmentMessageLabel : String
    # BombardmentAnnouncementName : None
    # SearchAndDestroyPlanUnpackSoundName : None
    # SearchAndDestroyPlanIdleLoopSoundName : None
    # SearchAndDestroyPlanPackSoundName : None
    # SearchAndDestroyMessageLabel : String
    # SearchAndDestroyAnnouncementName : None
    # HoldTheLinePlanUnpackSoundName : None
    # HoldTheLinePlanPackSoundName : None
    # HoldTheLineMessageLabel : String
    # HoldTheLineAnnouncementName : None
    ValidMemberKindOf : List[KindOf]
    InvalidMemberKindOf : List[KindOf]
    BattlePlanChangeParalyzeTime : Int
    HoldTheLinePlanArmorDamageScalar : Float
    SearchAndDestroyPlanSightRangeScalar : Float
    StrategyCenterSearchAndDestroySightRangeScalar : Float
    StrategyCenterSearchAndDestroyDetectsStealth : Bool
    StrategyCenterHoldTheLineMaxHealthScalar : Float
    StrategyCenterHoldTheLineMaxHealthChangeType : HealthRatioType
    VisionObjectName : "Object"

class BannerCarrierUpdate(Behavior):
    IdleSpawnRate : Int
    MeleeFreeUnitSpawnTime : Int
    DiedRespawnTime : Int
    MeleeFreeBannerReSpawnTime : Int
    # MorphCondition : KeyValuePair
    # ExpLevelDraw : KeyValuePair
    # BannerMorphFX : FXList
    # UnitSpawnFX : FXList
    ReplenishNearbyHorde : Bool
    ReplenishAllNearbyHordes : Bool
    ScanHordeDistance : Float
    UpgradeRequired : "Upgrade"

class ShareExperienceBehavior(Behavior):
    Radius : Float
    DropOff : Float
    Float : Float
    ObjectFilter : ObjectFilter

class CivilianSpawnUpdate(Behavior):
    SpawnDelayTime : Int
    MaximumDistance : Int
    RunToFilter : ObjectFilter
    Civilian : List["Object"]

class BoredUpdate(Behavior):
    ScanDelayTime : Int
    ScanDistance : Float
    BoredFilter : ObjectFilter
    CanScanWhileAttackingOrMoving : Bool
    SpecialPowerTemplate : "SpecialPower"

class AutoPickUpUpdate(Behavior):
    ScanDelayTime : Int
    PickUpFilter : ObjectFilter
    ScanDistance : Float
    # EatObjectEntry : KeyValuePair
    AutoThrowObject : Bool
    RunFromButton : Bool
    RunFromButtonNumber : Int
    CanScanWhileAttackingOrMoving : Bool

class DemoTrapUpdate(Behavior):
    DefaultProximityMode : Bool
    DetonationWeaponSlot : SlotTypes
    ProximityModeWeaponSlot : SlotTypes
    ManualModeWeaponSlot : SlotTypes
    TriggerDetonationRange : Float
    IgnoreTargetTypes : List[KindOf]
    ScanRate : Int
    AutoDetonationWithFriendsInvolve : Bool
    DetonationWeapon : "Weapon"
    DetonateWhenKilled : Bool

class CommandButtonHuntUpdate(Behavior):
    ScanRate : Int
    ScanRange : Float

class LaserUpdate(Behavior):
    # MuzzleParticleSystem : ParticleSystem
    # TargetParticleSystem : ParticleSystem
    # ParentFireBoneName : Bone
    ParentFireBoneOnTurret : Bool
    LaserLifetime : Float

class SupplyTruckAIUpdate(AIUpdateBehavior):
    MaxBoxes : Int
    SupplyCenterActionDelay : Int
    SupplyWarehouseActionDelay : Int
    SupplyWarehouseScanDistance : Float
    HarvestTrees : Bool
    HarvestActivationRange : Float
    HarvestPreparationTime : Int
    HarvestActionTime : Int

class HordeWorkerAIUpdate(AIUpdateBehavior):
    pass

class HordeAIUpdate(AIUpdateBehavior):
    pass

class AIUpdateInterface(AIUpdateBehavior):
    pass

class SiegeAIUpdate(AIUpdateBehavior):
    pass

class HeightDieUpdate(Behavior):
    TargetHeight : Float
    TargetHeightIncludesStructures : Bool
    OnlyWhenMovingDown : Bool
    DestroyAttachedParticlesAtHeight : Float
    SnapToGroundOnDeath : Bool
    InitialDelay : Int

class FloodUpdate(Behavior):
    AngleOfFlow : Degrees
    DirectionIsRelative : Bool
    
    # FloodMember : List[FloodMember]
    nested_attributes = {"FloodMember": ["FloodMember"]}

class FloatUpdate(Behavior):
    Enabled : Bool

class FlammableUpdate(Behavior):
    BurnedDelay : Int
    AflameDuration : Int
    AflameDamageDelay : Int
    AflameDamageAmount : Int
    # BurningSoundName : Sound
    FlameDamageLimit : Float
    FlameDamageExpiration : Int
    # FireFXList : FXList
    SetBurnedStatus : Bool
    SwapModelWhenAflame : Bool
    SwapModelWhenQuenched : Bool
    SwapTextureWhenAflame : Bool
    SwapTextureWhenQuenhed : Bool
    BurnContained : Bool
    RunToWater : Bool
    RunToWaterDepth : Float
    RunToWaterSearchRadius : Float
    RunToWaterSearchIncrement : Float
    PanicLocomotorWhileAflame : Bool
    # CustomAnimAndDuration : AnimAndDuration
    DamageType : DamageType

class MonitorConditionUpdate(Behavior):
    # ModelConditionFlags : ConditionFlags
    ModelConditionCommandSet : String
    WeaponSetFlags : WeaponsetFlags
    WeaponToggleCommandSet : "CommandSet"

class DamageFieldUpdate(Behavior):
    HeroModeTrigger : Bool
    ChargingModeTrigger : Bool
    AliveOnly : Bool
    Radius : Int
    ObjectFilter : ObjectFilter
    RequiredUpgrade : "Upgrade"
    
    # FireWeaponNugget : List["FireWeaponNugget"]
    nested_attributes = {"FireWeaponNugget": ["FireWeaponNugget"]}
    

class OilSpillUpdate(Behavior):
    HeroModeTrigger : Bool
    ChargingModeTrigger : Bool
    AliveOnly : Bool
    BreadcrumbName : String
    IgnitionWeaponName : String
    IgnitionWeaponSpacing : Float
    # OilSpillFX : FXList
    
    # FireWeaponNugget : List["FireWeaponNugget"]
    nested_attributes = {"FireWeaponNugget": ["FireWeaponNugget"]}

class FireWeaponUpdate(Behavior):
    HeroModeTrigger : Bool
    ChargingModeTrigger : Bool
    AliveOnly : Bool
    
    # FireWeaponNugget : List["FireWeaponNugget"]
    nested_attributes = {"FireWeaponNugget": ["FireWeaponNugget"]}

class FireSpreadUpdate(Behavior):
    OCLEmbers : "ObjectCreationList"
    MinSpreadDelay : Int
    MaxSpreadDelay : Int
    SpreadTryRange : Float

class AutoDepositUpdate(Behavior):
    DepositTiming : Int
    Upgrade : "Upgrade"
    DepositAmount : Int
    InitialCaptureBonus : Int
    UpgradeBonusPercent : Float
    UpgradeMustBePresent : ObjectFilter
    GiveNoXP : Bool
    OnlyWhenGarrisoned : Bool

class PartTheHeavensUpdate(Behavior):
    # Texture : String
    # Radius : None
    # Color : None
    # Opacity : None
    # Angle : None
    pass

class DestroyEnvironmentUpdate(Behavior):
    StartTime : Int
    DestructionTime : Int

class RainOfFireUpdate(Behavior):
    StartRainTime : Int
    DarknessFadeTime : Int
    RainEmitterHeight : Float
    DarknessLevel : Float
    JitterRadius : Float
    DPSMin : Float
    DPSMax : Float
    DPSRampupTime : Int
    RainOffset : Coords

class RadiusDecalUpdate(Behavior):
    pass

class SpecialEnemySenseUpdate(Behavior):
    SpecialEnemyFilter : "ObjectFilter"
    ScanRange : Float
    ScanInterval : Int

class OneRingPenaltyUpdate(Behavior):
    SpecialObjectName : "Object"
    RingTimeBeforeSpawning : Int
    TimeSpentRoamingAround : Int
    TimeRingPowerSuppressed : Int
    StartingDistanceFromMe : Float
    TimeFrozenFromPenalty : Int
    # DiscoveredSound : Sound

class LifetimeUpdate(Behavior):
    MinLifetime : Int
    MaxLifetime : Int
    WaitForWakeUp : Bool
    ScoreKill : Bool
    DeathType : DeathType

class DelayedLuaEventUpdate(Behavior):
    pass

class ToppleUpdate(Behavior):
    # ToppleFX : FXList
    # BounceFX : FXList
    StumpName : "Object"
    KillWhenStartToppling : Bool
    KillWhenFinishedToppling : Bool
    KillStumpWhenToppled : Bool
    ToppleLeftOrRightOnly : Bool
    ReorientToppledRubble : Bool
    InitialVelocityPercent : Float
    InitialAccelPercent : Float
    BounceVelocityPercent : Float
    MinimumToppleSpeed : Float

class LargeGroupBonusUpdate(Behavior):
    UpdateRate : Int
    HordeMemberFilter : ObjectFilter
    Count : Int
    Radius : Float
    RubOffRadius : Float
    AlliesOnly : Bool
    # FlagSubObjectNames : Strings
    AttributeModifier : "ModifierList"

class GiantBirdAIUpdate(AIUpdateBehavior):
    # AttackLocomotorType : LocomotorSetType
    # ReturnForAmmoLocomotorType : LocomotorSetType
    GrabTossTimeTrigger : Float
    GrabTossHeightTrigger : Float
    FollowThroughDistance : Float
    FollowThroughCheckStep : Float
    FollowThroughGradient : Float
    # TossFX : FXList

class AssaultTransportAIUpdate(AIUpdateBehavior):
    pass

class DeployStyleAIUpdate(AIUpdateBehavior):
    UnpackTime : Int
    PackTime : Int
    ResetTurretBeforePacking : Bool
    TurretsFunctionOnlyWhenDeployed : Bool
    TurretsMustCenterBeforePacking : Bool
    MustDeployToAttack : Bool
    DeployedAttributeModifier : "ModifierList"

class DynamicShroudClearingRangeUpdate(Behavior):
    ChangeInterval : Int
    GrowInterval : Int
    ShrinkDelay : Int
    ShrinkTime : Int
    GrowDelay : Int
    GrowTime : Int
    FinalVision : Float
    # GridDecalTemplate : None

class DeletionUpdate(Behavior):
    MinLifetime : Int
    MaxLifetime : Int

class DelayedWeaponSetUpgradeUpdate(Behavior):
    # defining this causes a weaponset upgrade to be delayed by the amount specified in the DelayedUpgrade
    # module with the same upgrade as the weaponset upgrade module
    pass

class InvisibilityUpdate(Behavior):
    UpdatePeriod : Int
    RequiredUpgrades : List["Upgrade"]
    ForbiddenUpgrades : List["Upgrade"]
    Broadcast : Bool
    BroadcastObjectFilter : ObjectFilter
    BroadcastRange : Float
    StartsActive : Bool
    # UnitSpecificSoundNameToUseAsVoiceMoveToStealthyArea : Sound
    # UnitSpecificSoundNameToUseAsVoiceEnterStateMoveToStealthyArea : Sound
    
    # InvisibilityNugget : "InvisibilityNugget"
    nested_attributes = {"InvisibilityNugget": ["InvisibilityNugget"]}
