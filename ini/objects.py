from .enums import Descriptors, Relations, KindsOf
from .utils import is_end

import re
import sys
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
        
class IniObject:
    def recursive(self, func, values):
        values = self.parser.get_macro(values)
        if isinstance(values, list):
            return [self.recursive(func, value) for value in values]
        
        if isinstance(values, dict):
            return {x : self.recursive(func, y) for x, y in values.items()}
            
        return func(self.parser, values)
        
    def __init__(self, name, data, parser):
        self.name = name
        self.parser = parser
        self.__dict__.update(data)
        
        getattr(self.parser, self.key)[name] = self
        
    @classmethod
    def convert(cls, parser, value):
        return getattr(parser, cls.key)[value]
        
    def __getattribute__(self, name):
        annotations = object.__getattribute__(self, "__annotations__")
        if not name in annotations:
            return object.__getattribute__(self, name)
            
        if not name in object.__getattribute__(self, "__dict__"):
            return None
        
        annotation = annotations[name]
        if isinstance(annotation, str):
            annotation = getattr(sys.modules["ini"], annotation)
            
        parser = object.__getattribute__(self, "parser")
        value = parser.get_macro(object.__getattribute__(self, name))
        
        recursive = object.__getattribute__(self, "recursive")
        return recursive(annotation.convert, value)
    
    def __repr__(self):
        return f"<{self.__class__.__name__} {self.name}>"
    
    @staticmethod
    def default_line_parse(data, key, value):
        data[key] = value

    @classmethod
    def parse(cls, parser, name, lines):
        from .behaviors import get_behavior
        line = next(lines)
        data = {
            "modules": {},
            # **{x : y["default"]() for x, y in cls.special_attributes.items()}, 
            # **{x : list() for x in cls.nested_attributes}
        }
        
        while not is_end(line):
            logging.debug(line)
            if line.startswith("Behavior"):
                _, _, behavior, bh_name = line.split()
                if obj := get_behavior(behavior):
                    data["modules"][bh_name] = obj.parse(parser, bh_name, lines)
            elif "=" in line:
                key, value = line.split("=", maxsplit=1)
                cls.default_line_parse(data, key.strip(), value.strip())
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
        