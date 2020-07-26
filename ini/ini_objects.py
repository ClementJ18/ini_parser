from .enums import *
from .utils import to_float
from .objects import FilterList, IniObject, String
from .types import Float, Bool, Coords, List, Dict
from .nuggets import *

import sys

def get_obj(name):
    return getattr(sys.modules[__name__], name, None)
    
class Upgrade(IniObject):
    key = "upgrades"
    
    Type : UpgradeTypes
    DisplayName : String
    BuildTime : Float
    BuildCost : Float
    # ButtonImage : Image
    Tooltip : String
    # Cursor : Cursor
    PersistsInCampaign : Bool
    # LocalPlayerGainsUpgradeEvaEvent : EvaEvent
    # AlliedPlayerGainsUpgradeEvaEvent : EvaEvent
    # EnemyPlayerGainsUpgradeEvaEvent : EvaEvent
    # AlliedPlayerLosesUpgradeEvaEvent : EvaEvent
    # EnemyPlayerLosesUpgradeEvaEvent : EvaEvent
    NoUpgradeDiscount : Bool
    UseObjectTemplateForCostDiscount : "Object"
    # SkirmishAIHeuristic : AI
    # ResearchCompleteEvaEvent : EvaEvent
    # ResearchSound : Sound
    RequiredObjectFilter : FilterList
    # StrategicIcon : Image
    SubUpgradeTemplateNames : List("Upgrade")

class Armor(IniObject):
    key = "armorsets"
    
    DEFAULT : Float
    FlankedPenalty : Float
    DamageScalar : Float
    
    __annotations__.update({x : Float for x in DamageTypes})
        
    @staticmethod
    def default_line_parse(data, key, value):
        armor = value.split()
        if len(armor) == 2:
            data[armor[0].strip()] = armor[1]
        else:
            data[key] = value
        
    def get_damage_scalar(self, damagetype, flanked = False):
        default = self.default or 1
        value = getattr(self, damagetype.name, default) * self.scalar
        
        if flanked:
            return value + (value * flanked)
        
        return value * (self.scalar or 1)

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
            item = super().__getattribute__(name)
        except AttributeError:
            pass
        else:
            return item
            
        return object.__getattribute__(self.parent, name)