from .objects import IniObject, FilterList
from .types import Float, Bool, Coords
from .enums import * 

class Nugget(IniObject):
    def __init__(self, name, data, parser):
        self.name = name
        self.parser = parser
    
class DamageNugget(Nugget):
    """
    Damage : float
    Radius : float
    DelayTime : float
    DamageType : DamageTypes
    DamageFXType : DamageFXTypes
    DeathType : DeathTypes
    DamageScalar : float
    DamageArc : float
    FlankingBonus : float
    ForbiddenUpgradeNames : List[Upgrade]
    RequiredUpgradeNames : List[Upgrade]
    AcceptDamageAdd : bool
    SpecialObjectFilter : FilterList
    DamageTaperOff : float
    DamageSpeed : float
    DamageSubType : DamageTypes
    DrainLife : bool
    DrainLifeMultiplier : float
    CylinderAOE : bool
    DamageMaxHeight : float
    DamageArcInverted : bool
    ForceKillObjectFilter : FilterList
    DamageMaxHeightAboveTerrain : float
    """
    def __init__(self, name, data, parser):
        self.parser = parser
        self.name = name
        
        self.value("damage", data.pop("Damage", None), Float)
        self.value("radius", data.pop("Radius", None), Float)
        self.value("delay_time", data.pop("DelayTime", None), Float)
        self.enum("damage_type", data.pop("DamageType", None), DamageTypes)
        self.enum("damage_type_fx", data.pop("DamageFXType", None), DamageFXTypes)
        self.enum("damage_sub_type", data.pop("DamageSubType", None), DamageTypes)
        self.enum("death_type", data.pop("DeathType", None), DeathTypes)
        self.value("damage_scalar", data.pop("DamageScalar", None), Float)
        self.value("damage_arc", data.pop("DamageArc", None), Float)
        self.value("flanking_bonus", data.pop("FlankingBonus", None), Float)
        self.value("accept_damage_add", data.pop("AcceptDamageAdd", None), Bool)
        self.value("damage_taper_off", data.pop("DamageTaperOff", None), Float)
        self.value("damage_speed", data.pop("DamageSpeed", None), Float)
        self.special_filter = FilterList(None, data.pop("SpecialObjectFilter", ""))    
        self.kill_filter = FilterList(None, data.pop("KillObjectFilter", ""))
        self.reference("required_upgrades", data.pop("RequiredUpgradeNames", []), "upgrades")
        self.reference("forbidden_upgrades", data.pop("ForbiddenUpgradeNames", []), "upgrades")
        self.value("drain_life", data.pop("DrainLife", None), Bool)
        self.value("drain_life_multiplier", data.pop("DrainLifeMultiplier", None), Float)
    
    special_attributes = {
        "RequiredUpgradeNames": {"default": list, "func": lambda data, value: value.split()},
        "ForbiddenUpgradeNames": {"default": list, "func": lambda data, value: value.split()}
    }

class MetaImpactNugget(Nugget):
    """
    HeroResist : float
    ShockWaveAmount : float
    ShockWaveRadius : float
    ShockWaveArc : float
    ShockWaveTaperOff : float
    SpecialObjectFilter : FilterList
    ShockWaveSpeed : float
    ShockWaveZMult : float
    RequiredUpgradeNames : List[Upgrade]
    ForbiddenUpgradeNames : List[Upgrade]
    KillObjectFilter : FilterList
    OnlyWhenJustDied : bool
    DelayTime : float
    """
    def __init__(self, name, data, parser):
        self.parser = parser
        self.name = name
    
        self.value("resist", data.pop("HeroResist", None), Float)
        self.value("sw_amount", data.pop("ShockWaveAmount", None), Float)
        self.value("sw_radius", data.pop("ShockWaveRadius", None), Float)
        self.value("sw_arc", data.pop("ShockWaveArc", None), Float)
        self.value("sw_taper_off", data.pop("ShockWaveTaperOff", None), Float)
        self.value("sw_speed", data.pop("ShockWaveSpeed", None), Float)
        self.value("sw_zmult", data.pop("ShockWaveZMult", None), Float)
        self.special_filter = FilterList(None, data.pop("SpecialObjectFilter", ""))    
        self.kill_filter = FilterList(None, data.pop("KillObjectFilter", ""))
        self.reference("required_upgrades", data.pop("RequiredUpgradeNames", []), "upgrades")
        self.reference("forbidden_upgrades", data.pop("ForbiddenUpgradeNames", []), "upgrades")
        self.value("only_when_just_died", data.pop("OnlyWhenJustDied", None), Bool)
        self.value("delay_time",data.pop("DelayTime", None), Float)
    
    
    special_attributes = {
        "RequiredUpgradeNames": {"default": list, "func": lambda data, value: value.split()},
        "ForbiddenUpgradeNames": {"default": list, "func": lambda data, value: value.split()}
    }

class ProjectileNugget(Nugget):
    """
    WarheadTemplateName : Weapon
    ProjectileTemplateName : Object
    ForbiddenUpgradeNames : List[Upgrade]
    SpecialObjectFilter : FilterList
    RequiredUpgradeNames : List[Upgrade]
    WeaponLaunchBoneSlotOverride : SECONDARY
    AlwaysAttackHereOffset : Coords
    UseAlwaysAttackOffset : Bool
    """
    def __init__(self, name, data, parser):
        self.parser = parser
        self.name = name
        
        self.reference("warhead", data.pop("WarheadTemplateName", None), "weapons")
        self.reference("projectile", data.pop("ProjectileTemplateName", None), "objects")
        self.value("attack_here_offset", data.pop("AlwaysAttackHereOffset", None), Coords)
        self.value("use_offset", data.pop("UseAlwaysAttackOffset", None), Bool)
        #weapon bone
        self.special_filter = FilterList(None, data.pop("SpecialObjectFilter", ""))
        self.reference("required_upgrades", data.pop("RequiredUpgradeNames", []), "upgrades")
        self.reference("forbidden_upgrades", data.pop("ForbiddenUpgradeNames", []), "upgrades")
    
    special_attributes = {
        "RequiredUpgradeNames": {"default": list, "func": lambda data, value: value.split()},
        "ForbiddenUpgradeNames": {"default": list, "func": lambda data, value: value.split()}
    }
        

class WeaponOCLNugget(Nugget):
    """
    WeaponOCLName : List[ObjectCreate]
    RequiredUpgradeNames : List[Upgrade]
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
        self.special_filter = FilterList(None, data.pop("SpecialObjectFilter", ""))
        self.enum("damage_type_fx", data.pop("DamageFXType", None), DamageFXTypes)
        self.reference("required_upgrades", data.pop("RequiredUpgradeNames", []), "upgrades")
        self.reference("forbidden_upgrades", data.pop("ForbiddenUpgradeNames", []), "upgrades")
        self.value("affect_horde_members", data.pop("AffectHordeMembers", None), Bool)
        
    
    special_attributes = {
        "RequiredUpgradeNames": {"default": list, "func": lambda data, value: value.split()},
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
        self.special_filter = FilterList(None, data.pop("SpecialObjectFilter", ""))
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
        self.special_filter = FilterList(None, data.pop("SpecialObjectFilter", ""))
        self.enum("damage_sub_type", data.pop("DamageSubType", None), DamageTypes)
    
    special_attributes = {
        "RequiredUpgradeNames": {"default": list, "func": lambda data, value: value.split()},
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
        self.special_filter = FilterList(None, data.pop("SpecialObjectFilter", ""))
        self.value("freeze", data.pop("FreezeAnimation", None), Bool)
        self.reference("fx", data.pop("ParalyzeFX", None), "fxs")
        self.reference("required_upgrades", data.pop("RequiredUpgradeNames", []), "upgrades")
        self.reference("forbidden_upgrades", data.pop("ForbiddenUpgradeNames", []), "upgrades")
    
    special_attributes = {
        "RequiredUpgradeNames": {"default": list, "func": lambda data, value: value.split()},
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
        self.special_filter = FilterList(None, data.pop("SpecialObjectFilter", ""))

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
        self.special_filter = FilterList(None, data.pop("SpecialObjectFilter", ""))
        
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
        
    special_attributes = {
        "KillKindof": {"default": list, "func": lambda data, value: value.split()},
        "KillKindofNot": {"default": list, "func": lambda data, value: value.split()}
    }

class OpenGateNugget(Nugget):
    """
    Radius : float
    """
    def __init__(self, name, data, parser):
        self.parser = parser
        self.name = name
        
        self.value("radius", data.pop("Radius", None), Float)
