from .utils import to_float

class Bool:
    @classmethod
    def convert(cls, parser, value):
        value = parser.get_macro(value)
        if isinstance(value, bool):
            return value
        
        if not value in ["Yes", "No"]:
            raise ValueError(f"Expected a MACRO or a BOOL but found {value}")
            
        return value == "Yes"

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
