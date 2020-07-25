from dataclasses import dataclass, field
from typing import List

class IniObject:
    def __init__(self, name, data, parser):
        self.name : name
        self.parser : parser
        self.__dict__.update(data)
        
    @classmethod
    def convert(cls, parser, value):
        raise NotImplementedError

    @classmethod
    def parse(cls):
        pass
        
    def __getattribute__(self, name):
        annotation = self.__annotations__[name]
        value = self.parser.get_macro(object.__getattribute__(self, name))
        return annotation.convert(self.parser, value)
        

@dataclass
class Upgrade(IniObject):
    Type : UpgradeTypes
    DisplayName : String
    BuildTime : Float
    BuildCost : Float
    ButtonImage : Image
    Tooltip : String
    Cursor : Cursor
    PersistsInCampaign : Bool
    LocalPlayerGainsUpgradeEvaEvent : EvaEvent
    AlliedPlayerGainsUpgradeEvaEvent : EvaEvent
    EnemyPlayerGainsUpgradeEvaEvent : EvaEvent
    AlliedPlayerLosesUpgradeEvaEvent : EvaEvent
    EnemyPlayerLosesUpgradeEvaEvent : EvaEvent
    NoUpgradeDiscount : Bool
    UseObjectTemplateForCostDiscount : Object
    SkirmishAIHeuristic : AI
    ResearchCompleteEvaEvent : EvaEvent
    ResearchSound : Sound
    RequiredObjectFilter : FilterList
    StrategicIcon : Image
    SubUpgradeTemplateNames : Upgrades
