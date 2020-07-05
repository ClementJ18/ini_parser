from .objects import IniObject

class Nugget(IniObject):
    pass
    
class DamageNugget(Nugget):
    """
    Damage : CREATE_A_HERO_CLEAR_GARRISON_DAMAGE
    Radius : CREATE_A_HERO_FIREBALL_RADIUS_LVL_2
    DelayTime : 0
    DamageType : MAGIC
    DamageFXType : UNDEFINED
    DeathType : NORMAL
    DamageScalar : FORGED_BLADES_PIKEMAN_VS_CAVALRY
    DamageArc : 45
    FlankingBonus : 100%
    ForbiddenUpgradeNames : Upgrade_MordorForgedBlades
    RequiredUpgradeNames : Upgrade_MordorForgedBlades
    AcceptDamageAdd : No
    SpecialObjectFilter : +MACHINE
    DamageTaperOff : 30
    DamageSpeed : 700.0
    DamageSubType : BECOME_UNDEAD
    DrainLife : Yes
    DrainLifeMultiplier : 0.75
    CylinderAOE : Yes
    DamageMaxHeight : 60
    DamageArcInverted : Yes
    ForceKillObjectFilter : +INFANTRY
    DamageMaxHeightAboveTerrain : 1
    """
    pass

class MetaImpactNugget(Nugget):
    """
    HeroResist : WEAK_SPELL_HERORESIST
    ShockWaveAmount : 5.0
    ShockWaveRadius : 5.0
    ShockWaveArc : 120
    ShockWaveTaperOff : 0.5
    SpecialObjectFilter : NONE
    ShockWaveSpeed : 0.0
    ShockWaveZMult : 1.0
    RequiredUpgradeNames : Upgrade_ThalKaserneLevel3
    ForbiddenUpgradeNames : Upgrade_OriSchicksal
    KillObjectFilter : INSTANT_DEATH_ON_METAIMPACT_OBJFILTER
    OnlyWhenJustDied : Yes
    DelayTime : 200
    """
    pass

class ProjectileNugget(Nugget):
    """
    WarheadTemplateName : CreateAHeroStachelderVergeltungWarhead_Level1_JotE
    ProjectileTemplateName : DwarvenCatapultRockProjectile2
    ForbiddenUpgradeNames : Upgrade_GoodFortressFlamingMunitions
    SpecialObjectFilter : -MACHINE
    RequiredUpgradeNames : Upgrade_GoodFortressFlamingMunitions
    WeaponLaunchBoneSlotOverride : SECONDARY
    AlwaysAttackHereOffset : Z:0
    UseAlwaysAttackOffset : Yes
    """
    pass

class WeaponOCLNugget(Nugget):
    """
    WeaponOCLName : OCL_OriDamagedPoison
    RequiredUpgradeNames : Upgrade_Held10RespawnLevel
    """
    pass

class AttributeModifierNugget(Nugget):
    """
    AttributeModifier : AttributeModCrippleStrike_Level3
    Radius : 10
    SpecialObjectFilter : -ARMY_OF_DEAD
    DamageFXType : GOOD_ARROW_PIERCE
    ForbiddenUpgradeNames : Upgrade_CHW07
    RequiredUpgradeNames : Upgrade_DwarvenFortressDwarvenStonework
    AffectHordeMembers : Yes
    """
    pass

class StealMoneyNugget(Nugget):
    """
    AmountStolenPerAttack : 5
    SpecialObjectFilter : ANY
    RequiredUpgradeNames : Upgrade_AngmarFortressSanctum
    """
    pass

class DOTNugget(Nugget):
    """
    Damage : 10
    Radius : 30.0
    DelayTime : 1
    DamageType : POISON
    DamageFXType : POISON
    DeathType : NORMAL
    DamageInterval : 1000
    DamageDuration : CREATE_A_HERO_ASSASSIN_DOT_DAMAGE_DURATION_L4
    RequiredUpgradeNames : Upgrade_Held10RespawnLevel
    DamageScalar : 0%
    AcceptDamageAdd : Yes
    SpecialObjectFilter : AFFECTED_BY_POISON_OBJECTFILTER
    DamageSubType : BECOME_UNDEAD_ONCE
    ForbiddenUpgradeNames : Upgrade_CreateAHeroPoisonAttack_Level3
    """
    pass

class ParalyzeNugget(Nugget):
    """
    Radius : 10
    Duration : 4500
    SpecialObjectFilter : ENEMIES
    FreezeAnimation : Yes
    AffectHordeMembers : Yes
    ParalyzeFX : FX_GenericDebuff
    RequiredUpgradeNames : Upgrade_CHW03
    ForbiddenUpgradeNames : Upgrade_CHW05
    """
    pass

class EmotionWeaponNugget(Nugget):
    """
    EmotionType : TERROR
    Radius : 0
    Duration : 5
    SpecialObjectFilter : ANY ENEMIES +MONSTER
    """
    pass

class FireLogicNugget(Nugget):
    """
    LogicType : INCREASE_BURN_RATE
    Radius : 40
    Damage : 10
    MinMaxBurnRate : 40
    MinDecay : 25
    MaxResistance : 1
    """
    pass

class SpecialModelConditionNugget(Nugget):
    """
    ModelConditionNames : USER_3
    ModelConditionDuration : 21000
    SpecialObjectFilter : NONE +MordorMountainTroll 
    """
    pass

class ClearNuggets(Nugget):
    """
    NOTHING
    """
    pass

class DamageFieldNugget(Nugget):
    """
    WeaponTemplateName : SmallFireFieldWeapon
    Duration : 3000
    """
    pass

class HordeAttackNugget(Nugget):
    """
    NOTHING
    """
    pass

class SpawnAndFadeNugget(Nugget):
    """
    ObjectTargetFilter : ANY +STRUCTURE +INFANTRY +CAVALRY +MONSTER -ROCK_VENDOR    ;where not to spawn?
    SpawnedObjectName : IsengardDeployedExplosiveMine    ;What to spawn?
    SpawnOffset : X:8 Y:1 Z:0    ;How far away from me to spawn?
    """
    pass

class GrabNugget(Nugget):
    """
    SpecialObjectFilter : ANY +GRAB_AND_DROP
    ContainTargetOnEffect : Yes
    ImpactTargetOnEffect : Yes
    ShockWaveAmount : 50.0
    ShockWaveRadius : 16.0
    ShockWaveTaperOff : 0.75
    ShockWaveZMult : 1.1
    """
    pass

class LuaEventNugget(Nugget):
    """
    LuaEvent : BeUncontrollablyAfraid
    Radius : 200
    SendToEnemies : Yes
    SendToAllies : No
    SendToNeutral : Yes
    """
    pass

class SlaveAttackNugget(Nugget):
    """
    NOTHING
    """
    pass

class DamageContainedNugget(Nugget):
    """
    KillCount : 5
    KillKindof : INFANTRY
    KillKindofNot : NONE
    DeathType : BURNED
    """
    pass

class OpenGateNugget(Nugget):
    """
    Radius : 0.0
    """
    pass
