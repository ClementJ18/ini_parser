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
    def __init__(self, name, data, parser):
        self.parser = parser
        self.name = name
        
        self.reference("required_upgrades", data.pop("RequiredUpgradeNames", []), "upgrades")
        self.reference("ocl", data.pop("WeaponOCLName", None), "objectcreationlists")
        
        
    special_attributes = {
        "RequiredUpgradeNames": {"default": list, "func": lambda data, value: value.split()}
    }

class AttributeModifierNugget(Nugget):
    """
    AttributeModifier : ModifierList
    Radius : float
    SpecialObjectFilter : FilterList
    DamageFXType : DamageFXTypes
    ForbiddenUpgradeNames : List[Upgrade]
    RequiredUpgradeNames : List[Upgrade]
    AffectHordeMembers : bool
    """
    def __init__(self, name, data, parser):
        self.parser = parser
        self.name = name
        
        self.reference("modifier", data.pop("AttributeModifier", None), "modifiers")
        self.value("radius", data.pop("Radius", None), Float)
        self.special_filter = FilterList(None, data.pop("SpecialObjectFilter"))
        self.enum("damage_type_fx", data.pop("DamageFXType", None), DamageFXTypes)
        self.reference("required_upgrades", data.pop("RequiredUpgradeNames", []), "upgrades")
        self.reference("forbidden_upgrades", data.pop("ForbiddenUpgradeNames", []), "upgrades")
        self.value("affect_horde_members", data.pop("AffectHordeMembers", None), Bool)
        
    
    special_attributes = {
        "RequiredUpgradeNames": {"default": list, "func": lambda data, value: value.split()}
        "ForbiddenUpgradeNames": {"default": list, "func": lambda data, value: value.split()}
    }

class StealMoneyNugget(Nugget):
    """
    AmountStolenPerAttack : float
    SpecialObjectFilter : FilterList
    RequiredUpgradeNames : List[Upgrade]
    """
    def __init__(self, name, data, parser):
        self.parser = parser
        self.name = name
        
        self.value("amount_stolen", data.pop("AmountStolenPerAttack", None), Float)
        self.special_filter = FilterList(None, data.pop("SpecialObjectFilter"))
        self.reference("required_upgrades", data.pop("RequiredUpgradeNames", []), "upgrades")
        
    special_attributes = {
        "RequiredUpgradeNames": {"default": list, "func": lambda data, value: value.split()}
    }
        

class DOTNugget(Nugget):
    """
    Damage : float
    Radius : float
    DelayTime : float
    DamageType : DamageTypes
    DamageFXType : DamageFXTypes
    DeathType : DeathTypes
    DamageInterval : float
    DamageDuration : float
    RequiredUpgradeNames : List[Upgrade]
    DamageScalar : float
    AcceptDamageAdd : bool
    SpecialObjectFilter : FilterList
    DamageSubType : DamageTypes
    ForbiddenUpgradeNames : List[Upgrade]
    """
    def __init__(self, name, data, parser):
        self.parser = parser
        self.name = name
        
        self.value("damage", data.pop("Damage", None), Float)
        self.value("radius", data.pop("Radius", None), Float)
        self.value("delay", data.pop("DelayTime", None), Float)
        self.enum("damage_type", data.pop("DamageType", None), DamageTypes)
        self.enum("damage_type_fx", data.pop("DamageFXType", None), DamageFXTypes)
        self.enum("death_type", data.pop("DeathType", None), DeathTypes)
        self.value("interval", data.pop("DamageInterval", None), Float)
        self.value("duration", data.pop("DamageDuration", None), Float)
        self.reference("required_upgrades", data.pop("RequiredUpgradeNames", []), "upgrades")
        self.reference("forbidden_upgrades", data.pop("ForbiddenUpgradeNames", []), "upgrades")
        self.value("scalar", data.pop("DamageScalar", None), float)
        self.value("accept_damage_add", data.pop("AcceptDamageAdd", None), Bool)
        self.special_filter = FilterList(None, data.pop("SpecialObjectFilter"))
        self.enum("damage_sub_type", data.pop("DamageSubType", None), DamageTypes)
    
    special_attributes = {
        "RequiredUpgradeNames": {"default": list, "func": lambda data, value: value.split()}
        "ForbiddenUpgradeNames": {"default": list, "func": lambda data, value: value.split()}
    }

class ParalyzeNugget(Nugget):
    """
    Radius : float
    Duration : float
    SpecialObjectFilter : FilterList
    FreezeAnimation : bool
    AffectHordeMembers : bool
    ParalyzeFX : FX
    RequiredUpgradeNames : List[Upgrades]
    ForbiddenUpgradeNames : List[Upgrades]
    """
    def __init__(self, name, data, parser):
        self.parser = parser
        self.name = name
        
        self.value("radius", data.pop("Radius", None), Float)
        self.value("duration", data.pop("Duration", None), Float)
        self.special_filter = FilterList(None, data.pop("SpecialObjectFilter"))
        self.value("freeze", data.pop("FreezeAnimation", None), Bool)
        self.reference("fx", data.pop("ParalyzeFX", None), "fxs")
        self.reference("required_upgrades", data.pop("RequiredUpgradeNames", []), "upgrades")
        self.reference("forbidden_upgrades", data.pop("ForbiddenUpgradeNames", []), "upgrades")
    
    special_attributes = {
        "RequiredUpgradeNames": {"default": list, "func": lambda data, value: value.split()}
        "ForbiddenUpgradeNames": {"default": list, "func": lambda data, value: value.split()}
    }

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
