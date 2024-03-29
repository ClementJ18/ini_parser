from .utils import is_end
from .types import String

import sys
import logging

def get_obj(name):
    obj = getattr(sys.modules["ini"], name, None)
    
    if hasattr(obj, "parse"):
        return obj
        
    return None
    
class UpdateClassDictMeta(type):
    def __new__(cls, name, bases, attrs):
        new_class = super(UpdateClassDictMeta, cls).__new__(cls, name, bases, attrs)
                
        nested = [bc.nested_attributes for bc in bases if hasattr(bc, 'nested_attributes')]
        if hasattr(new_class, 'nested_attributes'):
            nested.append(new_class.nested_attributes)
            
        new_class.nested_attributes = {}
        for d in nested:
            new_class.nested_attributes.update(d)
            
        return new_class
        
class IniObject(metaclass=UpdateClassDictMeta):
    def __init__(self, name, data, parser):
        self.name = name
        self.parser = parser
        self.__dict__.update(data)
        
        if self.key is not None:
            getattr(self.parser, self.key)[name] = self
            
    def check_strings(self):
        missing = []
        strings = [x for x, y in self.__annotations__.items() if y is String]
        for string in strings:
            try:
                getattr(self, string)
            except AttributeError:
                missing.append(string)
                
        return missing
        
    @classmethod
    def convert(cls, parser, value):
        if isinstance(value, cls):
            return value

        try:
            return getattr(parser, cls.key)[value]
        except KeyError:
            raise KeyError(f"Expected MACRO or {cls.__name__} but found {value}")
        
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
        
        return annotation.convert(parser, value)
    
    def __repr__(self):
        return f"<{self.__class__.__name__} {self.name}>"
    
    @staticmethod
    def line_parse(data, key, value):
        if key in data:
            if not isinstance(data[key], list):
                data[key] = [data[key]]
            
            data[key].append(value)
        else:
            data[key] = value
    
    nested_attributes = {} 
    default_attributes = {}
    __annotations__ = {}

    @classmethod
    def parse(cls, parser, name, lines):        
        data = {
            **{x : list() for x in cls.nested_attributes},
            **cls.default_attributes,
            "modules": {},
        }
        
        line = next(lines)
        while not is_end(line):
            if line.startswith(("Behavior", "ClientBehavior")): #parse as a behavior
                logging.debug(f"Behavior: {line}")
                _, _, behavior, bh_name = line.split()
                if obj := get_obj(behavior):
                    data["modules"][bh_name] = obj.parse(parser, bh_name, lines)
            elif line.startswith(("Body",)): #parse as a Body
                logging.debug(f"Body: {line}")
                _, _, behavior, bh_name = line.split()
                if obj := get_obj(behavior):
                    data["Body"] = obj.parse(parser, bh_name, lines)
            elif line.startswith("Draw"):
                logging.debug(f"Draw: {line}")
                _, _, _, draw_name = line.split()
                # data["modules"][draw_name] = Draw.parse(parser, draw_name, lines)
                Draw.parse(parser, draw_name, lines)
            elif "=" in line: # parse as a regular attribute
                logging.debug(f"Attribute: {line}")
                key, value = line.split("=", maxsplit=1)
                cls.line_parse(data, key.strip(), value.strip())
            else: #parse as a NestedAttribute
                logging.debug(f"Nested Attribute: {line}")
                possible_name = line.split()
                if len(possible_name) == 2:
                    obj_name = possible_name[0]
                    new_name = possible_name[1]
                else:
                    obj_name = line.strip()
                    new_name = name
                        
                obj = get_obj(obj_name)
                for key, values in cls.nested_attributes.items():
                    if obj in values or obj_name in values:
                        data[key].append(obj.parse(parser, new_name, lines)) 
            
            line = next(lines) 
            
        return cls(name, data, parser)
        
    def copy(self):
        return self.__class__(self.name, self.__dict__, self.parser)
        
class Module(IniObject):
    pass
    
class NestedAttribute(IniObject):
    pass
    
class MultilineAttribute(IniObject):
    pass
    
class Nugget(NestedAttribute):
    key = None
    
class Behavior(Module):
    key = None
    
    @property
    def trigger(self):
        if hasattr(self, "SpecialPowerTemplate"):
            return self.SpecialPowerTemplate
        
        if hasattr(self, "TriggeredBy"):
            return self.TriggeredBy
        
        return None
        
class Draw(Module):
    key = None 
    module_names = [
        "DefaultModelConditionState", "ModelConditionState", "AnimationState", "Animation", 
        "IdleAnimationState", "TransitionState", 
    ]

    @classmethod
    def parse(cls, parser, name, lines):
        counter = 0
        while True:
            line = next(lines)
            if is_end(line):
                counter -= 1

            if counter < 0:
                return

            if any(x for x in line.strip().split() if x in cls.module_names):
                counter += 1
        