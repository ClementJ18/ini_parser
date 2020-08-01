from .enums import Descriptors, Relations, KindsOf
from .utils import is_end

import re
import sys
import logging

def get_obj(name):
    obj = getattr(sys.modules["ini"], name, None)
    
    if hasattr(obj, "parse"):
        return obj
        
    return None
        
class IniObject:
    def __init__(self, name, data, parser):
        self.name = name
        self.parser = parser
        self.__dict__.update(data)
        
        if self.key is not None:
            getattr(self.parser, self.key)[name] = self
        
    @classmethod
    def convert(cls, parser, value):
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
        data[key] = value
        
    nested_attributes = {}
    default_attributes = {}
    __annotations__ = {}

    @classmethod
    def parse(cls, parser, name, lines):        
        data = {
            # **{x : y["default"]() for x, y in cls.special_attributes.items()}, 
            **{x : list() for x in cls.nested_attributes},
            **cls.default_attributes
        }
        
        line = next(lines)
        while not is_end(line):
            logging.debug(line)
            if line.startswith("Behavior"): #parse as a behavior
                _, _, behavior, bh_name = line.split()
                if obj := get_obj(behavior):
                    data["modules"][bh_name] = obj.parse(parser, bh_name, lines)
            elif line.startswith("Draw"):
                _, _, draw, draw_name = line.split()
                data["modules"][draw_name] = Draw.parse(parser, draw_name, lines)
            elif "=" in line: # parse as a regular attribute
                key, value = line.split("=", maxsplit=1)
                cls.line_parse(data, key.strip(), value.strip())
            elif False: #parse as a multiline attribute
                pass
            else: #parse as a NestedAttribute
                possible_name = line.split()
                if len(possible_name) == 2:
                    obj_name = possible_name[0]
                    new_name = possible_name[1]
                else:
                    obj_name = line.strip()
                    new_name = name
                        
                obj = get_obj(obj_name)
                for key, values in cls.nested_attributes.items():
                    if obj in values:
                        data[key].append(obj.parse(parser, new_name, lines)) 
            
            line = next(lines) 
            
        return cls(name, data, parser)
        
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
        raise NotImplementedError
        
class Draw(Module):
    key = None   
        