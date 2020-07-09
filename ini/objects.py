from .enums import Descriptors, Relations, KindsOf
from .utils import is_end

import re
import logging

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
        
class IniObject:
    def recursive(self, func, values):
        values = self.parser.get_macro(values)
        if isinstance(values, list):
            return [self.recursive(func, value) for value in values]
        
        if isinstance(values, dict):
            return {x : self.recursive(func, y) for x, y in values.items()}
            
        return func(self, values)
        
    def string(other, name, value):
        setattr(other, f"_{name}", value)
        setattr(other.__class__, name, property(lambda self: self.parser.get_string(getattr(self, f"_{name}"))))

    def value(other, name, value, value_type):
        def func(self, v):
            return value_type.convert(self.parser, v)
            
        setattr(other, f"_{name}", value)
        setattr(other.__class__, name, property(lambda self: self.recursive(func, getattr(self, f"_{name}"))))
        
    def enum(other, name, value, value_enum):
        def func(self, v):
            if v is not None:
                return value_enum[v]
            
            return None

        setattr(other, f"_{name}", value)
        setattr(other.__class__, name, property(lambda self: self.recursive(func, getattr(self, f"_{name}"))))
    
    def reference(other, name, values, dict_name):
        def func(self, v):
            return self.parser.get(dict_name, v)
        
        setattr(other, f"_{name}", values)
        setattr(other.__class__, name, property(lambda self: self.recursive(func, getattr(self, f"_{name}")) ))

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.name}>"
        
    special_attributes = {}
    nested_attributes = {}
    
    @staticmethod
    def default_line_parse(data, value):
        return value.strip()

    @classmethod
    def parse(cls, parser, name, lines):
        line = next(lines)
        data = {
            **{x : y["default"]() for x, y in cls.special_attributes.items()}, 
            **{x : list() for x in cls.nested_attributes.keys()}
        }
        
        while not is_end(line):
            logging.debug(line)
            if "=" in line:
                key, value = line.split("=", maxsplit=1)
                key = key.strip()
                
                for special, func in cls.special_attributes.items():
                    if key == special:
                        returned = func["func"](data, value)
                        if returned is not None:
                            data[key] = returned
                        break
                else:
                    data[key] = cls.default_line_parse(data, value)
            else:
                possible_name = line.split()
                if len(possible_name) == 2:
                    obj_name = possible_name[0]
                    new_name = possible_name[1]
                else:
                    obj_name = line.strip()
                    new_name = name
                        
                for key, values in cls.nested_attributes.items():
                    try:
                        index = [x.__name__ for x in values].index(obj_name)
                        data[key].append(values[index].parse(parser, new_name, lines)) 
                    except ValueError:
                        pass
            
            line = next(lines) 
            
        return cls(name, data, parser)
        