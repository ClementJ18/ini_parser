from .objects import IniObject

import sys

def get_behavior(name):
    return getattr(sys.modules[__name__], name, None)
    
class Behavior(IniObject):
    @property
    def trigger(self):
        raise NotImplementedError
    
    
class SpecialPowerModule(Behavior):
    """
    SpecialPowerTemplate : SpecialPower
    UpdateModuleStartsAttack : bool
    StartsPaused : bool
    InitiateSound : Audio
    ReEnableAntiCategory : bool
    AntiCategory : AttributeModifierCategory
    AntiFX : FXList
    AttributeModifier : String
    AttributeModifierRange : FloatingPoint
    AttributeModifierAffectsSelf : Boolean
    AttributeModifierAffects : ObjectFilter
    AttributeModifierFX : FXList
    AttributeModifierWeatherBased : Boolean
    WeatherDuration : UnsignedInteger
    RequirementsFilterMPSkirmish : ObjectFilter
    RequirementsFilterStrategic : ObjectFilter
    TargetEnemy : Boolean
    TargetAllSides : Boolean
    InitiateFX : FXList
    TriggerFX : FXList
    SetModelCondition : ContainCondition
    SetModelConditionTime : FloatingPoint
    GiveLevels : SignedInteger
    DisableDuringAnimDuration : Boolean
    IdleWhenStartingPower : Boolean
    AffectGood : Boolean
    AffectEvil : Boolean
    AffectAllies : Boolean
    AvailableAtStart : Boolean
    ChangeWeather : WeatherFlag
    AdjustVictim : Boolean
    OnTriggerRechargeSpecialPower : String
    BurnDecayModifier : UnsignedInteger
    UseDistanceFromCommandCenter : Boolean
    DistanceFromCommandCenter : FloatingPoint
    """
    def __init__(self, name, data, parser):
        self.name = name
        self.parser = parser
        
        self.reference("special_power", data.pop("SpecialPowerTemplate"), "specialpowers")
        
        self.__dict__.update(data)

    @property
    def trigger(self):
        return self.special_power
    