from .utils import to_float

import re
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
    indexes = ["X", "Y", "Z"]
    
    @classmethod
    def convert(cls, parser, value):
        coords = [0, 0, 0] #x y z 
        for coord in value.split():
            ref, value = value.split(":")
            coords[indexes.index(ref.strip())] = float(value.strip())
        
        return coords
        
class RGB:
    indexes = ["R", "G", "B"]
    
    @classmethod
    def convert(cls, parser, value):
        rgb = [0, 0, 0] #x y z 
        for coord in value.split():
            ref, value = value.split(":")
            rgb[indexes.index(ref.strip())] = float(value.strip())
        
        return rgb
        
class Int:
    @classmethod
    def convert(cls, parser, value):
        value = parser.get_macro(value)
        
        if isinstance(value, int):
            return value
            
        try:
            return int(value)
        except ValueError:
            raise ValueError(f"Expected a MACRO or INT but found {value}")
        
class List:
    def __init__(self, element_type, index=0):
        self.element_type = element_type
        self.index = index
        
    def convert(self, parser, value):
        if isinstance(self.element_type, str):
            annotation = getattr(sys.modules["ini"], self.element_type)
        else:
            annotation = self.element_type
            
        return [annotation.convert(parser, x) for x in value.split()[self.index:]]
        
class Dict:
    def __init__(self, key_type, value_type):
        self.element_type = element_type
        
    def convert(self, parser, value):
        if isinstance(self.element_type, str):
            annotation = getattr(sys.modules["ini"], self.element_type)
        else:
            annotation = self.element_type

        return {x : annotation.convert(parser, x) for x in value.split()}
        
class Tuple:
    def __init__(self, *element_types):
        self.element_types = element_types
        
    def convert(self, parser, value):
        annotations = [getattr(sys.modules["ini"], e_type) if isinstance(e_type, str) else e_type for e_type in self.element_types]
        em = []
        for t, e in zip(annotations, value.split(maxsplit=len(self.element_types) - 1)):
            em.append(t.convert(parser, e))
            
        return tuple(em)    
         
class Union:
    def __init__(self, *types):
        self.types = types
        
    def convert(self, parser, value):
        for t in self.types:
            try:
                return t.convert(parser, value)
            except:
                pass
                
        raise ValueError(f"Failed to convert to any of {self.types}")
        
class String:
    """
    
    type : str
    name : str
    value : str
    shortcut : Optional[str]
    
    """
    def __init__(self, name, value):
        self.type, self.name = name.rsplit(":", 1)
        self.value = value
        match = re.search(r"&([A-Za-z])", value)
        self.shortcut = match.group(1) if match else None
        
    def __str__(self):
        return self.value
        
    def __repr__(self):
        return f"<String {self.name}>"
        
    @classmethod
    def convert(cls, parser, value):
        return parser.strings[value]
        
    @property
    def full_name(self):
        return f"{self.type}:{self.name}"
        
class FilterList:
    def __init__(self, name, values):
        self.name = name
        
        self.descriptor = None
        self.relations = []
        self.inclusion = []
        self.exclusion = []
        
        for value in values:
            if value in Descriptors.__members__:
                self.descriptor = Descriptors[value]
            elif value in Relations.__members__:
                self.relations.append(Relations[value])
            elif value.startswith(('-', '+')):
                if value[1:] in KindsOf.__members__:
                    member = KindsOf[value[1:]]
                else:
                    member = value[1:]

                if value[0] == "-":
                    self.exclusion.append(member)
                else:
                    self.inclusion.append(member)
                    
    def __repr__(self):
        return f"<FilterList {self.name}>"
        
    def is_in(self, obj, relation = None):
        exclusions = (x == obj.name or x in obj.kindof for x in self.exclusion)
        if any(exclusions):
            return False
            
        if relation not in self.relations and relation is not None:
            return False
        
        inclusions = (x == obj.name or x in obj.kindof for x in self.inclusion)
        if self.descriptor == Descriptors.ALL:
            return all(inclusions)
        
        if self.descriptor == Descriptors.ANY:
            return any(inclusions)
        
        if self.descriptor == Descriptors.NONE:
            return not any(inclusions)
        
        return False
        
    @classmethod
    def convert(cls, parser, value):
        return value
                    
class Operation:
    operation_mapping = {
        "MULTIPLY": lambda x, y: x*y,
    }
    
    def __init__(self, operation, args, parser):
        self.parser = parser
        
        self.key = operation
        self.operation = self.operation_mapping[operation]
        self.args = args
        
    def __repr__(self):
        return f"<Operation {self.key}>"
    
    @property
    def value(self):
        return self.operation(*[self.parser.get_macro(x) for x in self.args])
        
    @classmethod
    def convert(cls, parser, value):
        return value
