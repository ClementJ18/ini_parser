from .objects import Nugget
from .types import *
from .enums import * 

class DamageNugget(Nugget):
    Damage : Float
    Radius : Float
    DelayTime : Float
    DamageType : DamageType
    # DamageFXType : DamageFXTypes
    DeathType : DeathType
    DamageScalar : Float
    DamageArc : Float
    FlankingBonus : Float
    ForbiddenUpgradeNames : List["Upgrade"] = []
    RequiredUpgradeNames : List["Upgrade"] = []
    AcceptDamageAdd : Bool
    SpecialObjectFilter : ObjectFilter
    DamageTaperOff : Float
    DamageSpeed : Float
    DamageSubType : DamageType
    DrainLife : Bool
    DrainLifeMultiplier : Float
    CylinderAOE : Bool
    DamageMaxHeight : Float
    DamageArcInverted : Bool
    ForceKillObjectFilter : ObjectFilter
    DamageMaxHeightAboveTerrain : Float

class MetaImpactNugget(Nugget):
    HeroResist : Float
    ShockWaveAmount : Float
    ShockWaveRadius : Float
    ShockWaveArc : Float
    ShockWaveTaperOff : Float
    SpecialObjectFilter : ObjectFilter
    ShockWaveSpeed : Float
    ShockWaveZMult : Float
    RequiredUpgradeNames : List["Upgrade"] = []
    ForbiddenUpgradeNames : List["Upgrade"] = []
    KillObjectFilter : ObjectFilter
    OnlyWhenJustDied : Bool
    DelayTime : Float

class ProjectileNugget(Nugget):
    WarheadTemplateName : "Weapon"
    ProjectileTemplateName : "Object"
    ForbiddenUpgradeNames : List["Upgrade"] = []
    SpecialObjectFilter : ObjectFilter
    RequiredUpgradeNames : List["Upgrade"] = []
    # WeaponLaunchBoneSlotOverride : SECONDARY
    AlwaysAttackHereOffset : Coords
    UseAlwaysAttackOffset : Bool
        

class WeaponOCLNugget(Nugget):
    WeaponOCLName : List["ObjectCreate"] = []
    RequiredUpgradeNames : List["Upgrade"] = []

class AttributeModifierNugget(Nugget):
    AttributeModifier : "ModifierList"
    Radius : Float
    SpecialObjectFilter : ObjectFilter
    DamageFXType : DamageFXTypes
    ForbiddenUpgradeNames : List["Upgrade"] = []
    RequiredUpgradeNames : List["Upgrade"] = []
    AffectHordeMembers : Bool

class StealMoneyNugget(Nugget):
    AmountStolenPerAttack : Float
    SpecialObjectFilter : ObjectFilter
    RequiredUpgradeNames : List["Upgrade"] = []
        

class DOTNugget(Nugget):        
    Damage : Float
    Radius : Float
    DelayTime : Float
    DamageType : DamageType
    DamageFXType : DamageFXTypes
    DeathType : DeathType
    DamageInterval : Float
    DamageDuration : Float
    RequiredUpgradeNames : List["Upgrade"] = []
    DamageScalar : Float
    AcceptDamageAdd : Bool
    SpecialObjectFilter : ObjectFilter
    DamageSubType : DamageType
    ForbiddenUpgradeNames : List["Upgrade"] = []

class ParalyzeNugget(Nugget):        
    Radius : Float
    Duration : Float
    SpecialObjectFilter : ObjectFilter
    FreezeAnimation : Bool
    AffectHordeMembers : Bool
    # ParalyzeFX : FX
    RequiredUpgradeNames : List["Upgrade"] = []
    ForbiddenUpgradeNames : List["Upgrade"] = []

class EmotionWeaponNugget(Nugget):        
    EmotionType : EmotionTypes
    Radius : Float
    Duration : Float
    SpecialObjectFilter : ObjectFilter

class FireLogicNugget(Nugget):        
    LogicType : LogicTypes
    Radius : Float
    Damage : Float
    MinMaxBurnRate : Float
    MinDecay : Float
    MaxResistance : Float

class SpecialModelConditionNugget(Nugget):        
    ModelConditionNames : List[ModelCondition] = []
    ModelConditionDuration : Float
    SpecialObjectFilter : ObjectFilter

class ClearNuggets(Nugget):
    pass    
    
class DamageFieldNugget(Nugget):        
    WeaponTemplateName : "Weapon"
    Duration : Float

class HordeAttackNugget(Nugget):
    pass
    
class SpawnAndFadeNugget(Nugget):        
    ObjectTargetFilter : ObjectFilter
    SpawnedObjectName : "Object"
    SpawnOffset : Coords

class GrabNugget(Nugget):        
    SpecialObjectFilter : ObjectFilter
    ContainTargetOnEffect : Bool
    ImpactTargetOnEffect : Bool
    ShockWaveAmount : Float
    ShockWaveRadius : Float
    ShockWaveTaperOff : Float
    ShockWaveZMult : Float

class LuaEventNugget(Nugget):        
    # LuaEvent : LuaEvent
    Radius : Float
    SendToEnemies : Bool
    SendToAllies : Bool
    SendToNeutral : Bool

class SlaveAttackNugget(Nugget):
    pass

class DamageContainedNugget(Nugget):        
    KillCount : Float
    KillKindof : List[KindOf] = []
    KillKindofNot : List[KindOf] = []
    DeathType : DeathType

class OpenGateNugget(Nugget):            
    Radius : Float

WEAPON_NUGGETS = [
    AttributeModifierNugget, ClearNuggets, DOTNugget, DamageContainedNugget, DamageFieldNugget, 
    DamageNugget, EmotionWeaponNugget, FireLogicNugget, GrabNugget, HordeAttackNugget, LuaEventNugget, 
    MetaImpactNugget, OpenGateNugget, ParalyzeNugget, ProjectileNugget, SlaveAttackNugget, SpawnAndFadeNugget, 
    SpecialModelConditionNugget, StealMoneyNugget, WeaponOCLNugget
]

class InvisibilityNugget(Nugget):
    ForbiddenWeaponConditions : WeaponsetFlags
    DetectionRange : Float
    IgnoreTreeCheckUpgrades : List["Upgrade"]
    # BecomeStealthedFX : FXList
    # ExitStealthFX : FXList
    HintDetectableConditions : ObjectStatus
    
class FireWeaponNugget(Nugget):
    WeaponName : "Weapon"
    FireDelay : Int
    OneShot : Bool
