from .enums import *
from .objects import FilterList, IniObject, String
from .types import *
from .nuggets import *

import sys

def get_obj(name):
    return getattr(sys.modules[__name__], name, None)
    
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
    SciencePurchasePointCost : Int = 0
    IsGrantable : Bool = False
    SciencePurchasePointCostMP : Int = 0
    
    @staticmethod
    def line_parse(data, key, value):
        if key == "PrerequisiteSciences":
            data[key] = [] if value.strip().lower() == "none" else value.split(" OR ")
        else:
            data[key] = value
    
    def is_unlocked(self, *sciences):
        return any(all(x in sciences for x in preq) for preq in self.PrerequisiteSciences)

class Object(IniObject):
    def __init__(self, name, data, parser):
        self.name = name
        self.parser = parser
        self.modules = data.pop("modules")
        
        self.__dict__.update(data)
        
        
        self.upgades = {}
        self.parser.objects[name] = self
        
    def call_special_power(self, power):
        return [x for x in self.modules if x.trigger.name == power.name]
        
    def give_upgrade(self, upgrade):
        self.upgrades[upgrade.name] = upgrade

class ChildObject(Object):
    def __init__(self, name, data, parser):
        parent, true_name = name.split()
        
        self.reference("parent", parent, "objects")
        super().__init__(true_name, data, parser)
        
    def __getattribute__(self, name):
        try:
            return Object.__getattribute__(self, name)
        except AttributeError:
            pass
            
        return Object.__getattribute__(self.parent, name)
