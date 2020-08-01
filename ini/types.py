from .utils import to_float
from .enums import *

import regex
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
        
class Number:
    operation_mapping = {
        "MULTIPLY": lambda x, y: x*y,
        "DIVIDE": lambda x, y: x/y
    }
    
    pattern = regex.compile(r"#(MULTIPLY|DIVIDE)\(\s*((?R)|[0-9]*)\s*((?R)|[0-9]*)\s*\)", regex.VERSION1)
    
    @classmethod
    def do_operation(cls, parser, value):
        match = cls.pattern.match(value)
        if match is None:
            return cls.get_value(parser, value)
        
        return cls.operation_mapping[match.group(1)](
            cls.do_operation(parser, match.group(2)),
            cls.do_operation(parser, match.group(3))
        )
        
    @classmethod
    def convert(cls, parser, value):
        return cls.get_value(parser, cls.do_operation(parser, value))
        
    @classmethod
    def get_value(cls, parser, values):
        raise NotImplementedError       

class Float(Number):
    @classmethod
    def get_value(cls, parser, value):
        value = parser.get_macro(value)
        
        try:
            return to_float(value)
        except ValueError:
            raise ValueError(f"Expected a MACRO or FLOAT but found {value}")
            
class Int(Number):
    @classmethod
    def get_value(cls, parser, value):
        value = parser.get_macro(value)
            
        try:
            return int(value)
        except ValueError:
            raise ValueError(f"Expected a MACRO or INT but found {value}")
                  
class Complex:
    @classmethod
    def convert(cls, parser, value):
        values = [0, 0, 0] #x y z 
        for em in value.split():
            ref, code = em.split(":")
            values[cls.indexes.index(ref.strip())] = float(code.strip())
        
        return values

class Coords(Complex):
    indexes = ["X", "Y", "Z"]
        
class RGB(Complex):
    indexes = ["R", "G", "B"]

class Sequence:
    @staticmethod
    def get_annotation(annotation):
        if isinstance(annotation, str):
            return getattr(sys.modules["ini"], annotation)
                
        return annotation
    
class List(Sequence):
    def __init__(self, element_type, index=0):
        self.element_type = element_type
        self.index = index
        
    def convert(self, parser, value):
        annotation = self.get_annotation(self.element_type)
        return [annotation.convert(parser, x) for x in value.split()[self.index:]]
        
class Dict(Sequence):
    def __init__(self, key_type, value_type):
        self.key_type = key_type
        self.value_type = value_type
        
    def convert(self, parser, value):
        key = self.get_annotation(self.key_type)
        value = self.get_annotation(self.value_type)
        
        return {key.convert(parser, x) : value.convert(parser, x) for x in value.split()}
        
class Tuple(Sequence):
    def __init__(self, *element_types):
        self.element_types = element_types
        
    def convert(self, parser, value):
        annotations = [self.get_annotation(e_type) for e_type in self.element_types]
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
        match = regex.search(r"&([A-Za-z])", value)
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
