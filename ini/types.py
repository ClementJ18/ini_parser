from .utils import to_float

import sys

class Bool:
    @classmethod
    def convert(cls, parser, value):
        value = parser.get_macro(value)
        if isinstance(value, bool):
            return value
        
        if not value.lower() in ["yes", "no"]:
            raise ValueError(f"Expected a MACRO or a BOOL but found {value}")
            
        return value.lower() == "yes"

class Float:
    @classmethod
    def convert(cls, parser, value):
        value = parser.get_macro(value)
        
        if isinstance(value, float):
            return value
        
        if isinstance(value, int):
            return float(value)
        
        try:
            return to_float(value)
        except ValueError:
            raise ValueError(f"Expected a MACRO or FLOAT but found {value}")
            
class Coords:
    @classmethod
    def convert(cls, parser, value):
        return value
        
class List:
    def __init__(self, element_type):
        self.element_type = element_type
        
    def convert(self, parser, value):
        if isinstance(self.element_type, str):
            annotation = getattr(sys.modules["ini"], self.element_type)
        else:
            annotation = self.element_type
            
        return [annotation.convert(parser, x) for x in value.split()]
        
class Dict:
    def __init__(self, element_type):
        self.element_type = element_type
        
    def convert(self, parser, value):
        if isinstance(self.element_type, str):
            annotation = getattr(sys.modules["ini"], self.element_type)
        else:
            annotation = self.element_type

        return {x : self.element_type.convert(parser, x) for x in value.split()}
