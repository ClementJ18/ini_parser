from .objects import Nugget
from .types import *
from .enums import * 

class DamageNugget(Nugget):
    Damage : Float
    Radius : Float
    DelayTime : Float
    DamageType : DamageTypes
    # DamageFXType : DamageFXTypes
    DeathType : DeathTypes
    DamageScalar : Float
    DamageArc : Float
    FlankingBonus : Float
    ForbiddenUpgradeNames : List("Upgrade") = []
    RequiredUpgradeNames : List("Upgrade") = []
    AcceptDamageAdd : Bool
    SpecialObjectFilter : FilterList
    DamageTaperOff : Float
    DamageSpeed : Float
    DamageSubType : DamageTypes
    DrainLife : Bool
    DrainLifeMultiplier : Float
    CylinderAOE : Bool
    DamageMaxHeight : Float
    DamageArcInverted : Bool
    ForceKillObjectFilter : FilterList
    DamageMaxHeightAboveTerrain : Float

class MetaImpactNugget(Nugget):
    HeroResist : Float
    ShockWaveAmount : Float
    ShockWaveRadius : Float
    ShockWaveArc : Float
    ShockWaveTaperOff : Float
    SpecialObjectFilter : FilterList
    ShockWaveSpeed : Float
    ShockWaveZMult : Float
    RequiredUpgradeNames : List("Upgrade") = []
    ForbiddenUpgradeNames : List("Upgrade") = []
    KillObjectFilter : FilterList
    OnlyWhenJustDied : Bool
    DelayTime : Float

class ProjectileNugget(Nugget):
    WarheadTemplateName : "Weapon"
    ProjectileTemplateName : "Object"
    ForbiddenUpgradeNames : List("Upgrade") = []
    SpecialObjectFilter : FilterList
    RequiredUpgradeNames : List("Upgrade") = []
    # WeaponLaunchBoneSlotOverride : SECONDARY
    AlwaysAttackHereOffset : Coords
    UseAlwaysAttackOffset : Bool
        

class WeaponOCLNugget(Nugget):
    WeaponOCLName : List("ObjectCreate") = []
    RequiredUpgradeNames : List("Upgrade") = []

class AttributeModifierNugget(Nugget):
    AttributeModifier : "ModifierList"
    Radius : Float
    SpecialObjectFilter : FilterList
    DamageFXType : DamageFXTypes
    ForbiddenUpgradeNames : List("Upgrade") = []
    RequiredUpgradeNames : List("Upgrade") = []
    AffectHordeMembers : Bool

class StealMoneyNugget(Nugget):
    AmountStolenPerAttack : Float
    SpecialObjectFilter : FilterList
    RequiredUpgradeNames : List("Upgrade") = []
        

class DOTNugget(Nugget):        
    Damage : Float
    Radius : Float
    DelayTime : Float
    DamageType : DamageTypes
    DamageFXType : DamageFXTypes
    DeathType : DeathTypes
    DamageInterval : Float
    DamageDuration : Float
    RequiredUpgradeNames : List("Upgrade") = []
    DamageScalar : Float
    AcceptDamageAdd : Bool
    SpecialObjectFilter : FilterList
    DamageSubType : DamageTypes
    ForbiddenUpgradeNames : List("Upgrade") = []

class ParalyzeNugget(Nugget):        
    Radius : Float
    Duration : Float
    SpecialObjectFilter : FilterList
    FreezeAnimation : Bool
    AffectHordeMembers : Bool
    # ParalyzeFX : FX
    RequiredUpgradeNames : List("Upgrade") = []
    ForbiddenUpgradeNames : List("Upgrade") = []

class EmotionWeaponNugget(Nugget):        
    EmotionType : EmotionTypes
    Radius : Float
    Duration : Float
    SpecialObjectFilter : FilterList

class FireLogicNugget(Nugget):        
    LogicType : LogicTypes
    Radius : Float
    Damage : Float
    MinMaxBurnRate : Float
    MinDecay : Float
    MaxResistance : Float

class SpecialModelConditionNugget(Nugget):        
    ModelConditionNames : List(ModelConditions) = []
    ModelConditionDuration : Float
    SpecialObjectFilter : FilterList

class ClearNuggets(Nugget):
    pass    
    
class DamageFieldNugget(Nugget):        
    WeaponTemplateName : "Weapon"
    Duration : Float

class HordeAttackNugget(Nugget):
    pass
    
class SpawnAndFadeNugget(Nugget):        
    ObjectTargetFilter : FilterList
    SpawnedObjectName : "Object"
    SpawnOffset : Coords

class GrabNugget(Nugget):        
    SpecialObjectFilter : FilterList
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
    KillKindof : List(KindsOf) = []
    KillKindofNot : List(KindsOf) = []
    DeathType : DeathTypes

class OpenGateNugget(Nugget):            
    Radius : Float
