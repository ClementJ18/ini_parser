from .objects import IniObject
from .types import Float, Bool

class Nugget(IniObject):
    def __init__(self, name, data, parser):
        self.parser = parser
        self.name = name
    
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
    EmotionType : EmotionTypes
    Radius : float
    Duration : float
    SpecialObjectFilter : FilterList
    """
    def __init__(self, name, data, parser):
        self.parser = parser
        self.name = name
        
        self.enum("emotion", data.pop("EmotionType", None), EmotionTypes)
        self.value("radius", data.pop("Radius", None), Float)
        self.value("duration", data.pop("Duration", None), Float)
        self.special_filter = FilterList(None, data.pop("SpecialObjectFilter"))

class FireLogicNugget(Nugget):
    """
    LogicType : LogicTypes
    Radius : float
    Damage : float
    MinMaxBurnRate : float
    MinDecay : float
    MaxResistance : float
    """
    def __init__(self, name, data, parser):
        self.parser = parser
        self.name = name
        
        self.enum("logic_type", data.pop("LogicType", None), LogicTypes)
        self.value("radius", data.pop("Radius", None), Float)
        self.value("damage", data.pop("Damage", None), Float)
        self.value("burn_rate", data.pop("MinMaxBurnRate", None), Float)
        self.value("decay", data.pop("MinDecay", None), Float)
        self.value("resistance", data.pop("MaxResistance", None), Float)

class SpecialModelConditionNugget(Nugget):
    """
    ModelConditionNames : List[ModelConditions]
    ModelConditionDuration : float
    SpecialObjectFilter : FilterList
    """
    def __init__(self, name, data, parser):
        self.parser = parser
        self.name = name
        
        self.enum("conditions", data.pop("ModelConditionNames", []), ModelConditions)
        self.value("conditions_duration", data.pop("ModelConditionDuration", None), Float)
        self.special_filter = FilterList(None, data.pop("SpecialObjectFilter"))
        
    special_attributes = {
        "ModelConditionNames": {"default": list, "func": lambda data, value: value.split()}
    }

class ClearNuggets(Nugget):
    """
    NOTHING
    """
    pass

class DamageFieldNugget(Nugget):
    """
    WeaponTemplateName : Weapon
    Duration : float
    """
    def __init__(self, name, data, parser):
        self.parser = parser
        self.name = name
        
        self.reference("weapon", data.pop("WeaponTemplateName", None), "weapons")
        self.value("duration", data.pop("Duration", None), Float)

class HordeAttackNugget(Nugget):
    """
    NOTHING
    """
    pass

class SpawnAndFadeNugget(Nugget):
    """
    ObjectTargetFilter : FilterList
    SpawnedObjectName : Object
    SpawnOffset : Coords
    """
    def __init__(self, name, data, parser):
        self.parser = parser
        self.name = name
        
        self.target_filter = FilterList(None, data.pop("ObjectTargetFilter", ""))
        self.reference("object", data.pop("SpawnedObjectName", None), "objects")
        self.value("offset", data.pop("SpawnOffset", None), Coords)

class GrabNugget(Nugget):
    """
    SpecialObjectFilter : FilterList
    ContainTargetOnEffect : bool
    ImpactTargetOnEffect : bool
    ShockWaveAmount : float
    ShockWaveRadius : float
    ShockWaveTaperOff : float
    ShockWaveZMult : float
    """
    def __init__(self, name, data, parser):
        self.parser = parser
        self.name = name
        
        self.special_filter = FilterList(None, data.pop("SpecialObjectFilter", ""))
        self.value("contain_target", data.pop("ContainTargetOnEffect", "No"), Bool)
        self.value("impact_target", data.pop("ImpactTargetOnEffect", "No"), Bool)
        self.value("sw_amount", data.pop("ShockWaveAmount", None), Float)
        self.value("sw_radius", data.pop("ShockWaveRadius", None), Float)
        self.value("sw_taper_off", data.pop("ShockWaveTaperOff", None), Float)
        self.value("sw_zmult", data.pop("ShockWaveZMult", None), Float)

class LuaEventNugget(Nugget):
    """
    LuaEvent : LuaEvent
    Radius : float
    SendToEnemies : bool
    SendToAllies : bool
    SendToNeutral : bool
    """
    def __init__(self, name, data, parser):
        self.parser = parser
        self.name = name
        
        self.reference("event", data.pop("LuaEvent", None), "events")
        self.value("radius", data.pop("Radius", None), Float)
        self.value("to_enemies", data.pop("SendToEnemies", "No"), Bool)
        self.value("to_allies", data.pop("SendToAllies", "No"), Bool)
        self.value("to_neutral", data.pop("SendToNeutral", "No"), Bool)

class SlaveAttackNugget(Nugget):
    """
    NOTHING
    """
    pass

class DamageContainedNugget(Nugget):
    """
    KillCount : float
    KillKindof : List[KindsOf]
    KillKindofNot : List[KindsOf]
    DeathType : DeathTypes
    """
    def __init__(self, name, data, parser):
        self.parser = parser
        self.name = name
        
        self.value("kill_count", data.pop("KillCount", 0), Float)
        self.enum("kill", data.pop("KillKindof", []), KindsOf)
        self.enum("no_kill", data.pop("KillKindofNot", []), KindsOf)
        self.enum("death_type", data.pop("DeathType", None), DeathTypes)
        
    special_attributes {
        "KillKindof": {"default": list, "func": lambda data, value: value.split()},
        "KillKindofNot": {"default": list, "func": lambda data, value: value.split()},
    }

class OpenGateNugget(Nugget):
    """
    Radius : float
    """
    def __init__(self, name, data, parser):
        self.parser = parser
        self.name = name
        
        self.value("radius", data.pop("Radius", None), Float)
