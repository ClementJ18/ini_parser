from .utils import is_comment, remove_comments, clean_raw, is_end, to_float
from .objects import String, FilterList, Operation
from .ini_objects import get_obj
from .enums import KindsOf, Descriptors

import re
import logging
from collections import defaultdict

class GameParser:
    def __init__(self):
        self.strings = {}
        self.macros = {}
        
        self.armorsets = {}
        self.commandbuttons = {}
        self.commandsets = {}
        self.upgrades = {}
        self.modifiers = {}
        self.levels = {}
        self.sciences = {}
        self.specialpowers = {}
        self.objectcreationlists = {}
        self.objects = {}
        self.weapons = {}
        
        self.cursors = {}
        self.images = {}
        
        self.test = []
            
    def __repr__(self):
        return f"<Parser>"
            
    def get_string(self, string):
        if string is None:
            return None
        
        if not string in self.strings:
            raise ValueError(f"No string called {string} exists")
            
        return self.strings[string]
        
    def get_button(self, button):
        if not button in self.commandbuttons:
            raise ValueError(f"No commandbutton called {button} exists")
            
        return self.commandbuttons[button]
        
    def get(self, dict_name, key):
        if key is None:
            return None
        
        attribute = getattr(self, dict_name, {})
        if not key in attribute:
            raise ValueError(f"{key} does not exist in {dict_name}")
            
        return attribute[key]
        
        
    def get_macro(self, macro):
        if macro is None or not isinstance(macro, str):
            return macro
        
        try:
            return self.macros[macro]
        except (TypeError, KeyError):
            return macro
        
    def parse(self, raw):
        lines = iter(clean_raw(raw))
        
        while True:
            try:
                line = next(lines)
            except StopIteration:
                break
                        
            logging.info(line)
            obj_name = line.split(maxsplit=1)
            if obj := get_obj(obj_name[0]):
                obj.parse(self, obj_name[1], lines)
            elif line.startswith("#define"):
                self.parse_macro(line)
                
    def compile(self, raw, obj_names):
        lines = clean_raw(raw)
        obj = []        
        objs = {x : defaultdict(set) for x in obj_names}
        obj_names = '|'.join(obj_names)
        
        for line in lines:
            if is_comment(line):
                continue

            
            line = remove_comments(line.strip())
            if re.match(fr"^({obj_names})\s*\w*$", line):
                logging.info(f"NEW OBJECT {line}")    
                obj.append(line.split()[0])
            elif is_end(line) and obj:
                logging.info(f"OBJECT DONE {line}")    
                obj.pop(-1)
            elif obj:
                logging.info(line)
                key, value = line.split("=")
                objs[obj[-1]][key.strip()].update(value.split())
            else:
                logging.info(f"NO MATCH {line}")
                
        return objs 
  
    def parse_strings(self, raw):
        lines = raw.splitlines()
        current_name = None
        current_string = ""
        
        for line in lines:
            if is_comment(line):
                continue
            
            logging.debug(line)    
            line = remove_comments(line.strip())
            
            if is_end(line):
                self.strings[current_name] = String(current_name, current_string)
                
                current_string = ""
                current_name = None
            elif line.startswith('"') or current_name is not None:
                current_string += line.replace('"', '')
            else:
                current_name = line.strip()
                
    def parse_macro(self, line):
        _, name, value = line.split(maxsplit=2)
        value = remove_comments(value, macro=True)
        name = name.strip()
        
        self.macros[name] = value
        return 
        
        try:
            self.macros[name] = to_float(value)
            return
        except ValueError:
            pass
            
        if value in ["Yes", "No"]:
            self.macros[name] = value == "Yes"
            return
        
        if match := re.match(r"#(\w*)\( (\w*) ([a-zA-Z0-9_.]*) \)", value):
            operation = match.group(1)
            args = match.group(2, 3)
            self.macros[name] = Operation(operation, args, self)
            return
            
        if value[0].isdigit():
            self.macros[name] = value
            return
        
        try:
            if value.split()[0] in Descriptors.__members__ or value.split()[0].startswith('-'):
                self.macros[name] = FilterList(name, value.split())
            elif value.split()[0] in KindsOf.__members__:
                self.macros[name] = [KindsOf[x] for x in value.split()]
            else:
                self.macros[name] = value.split()
            return
        except IndexError:
            self.macros[name] = value
        
    def parse_macros(self, raw):
        lines = clean_raw(raw)
        
        for line in lines:
            logging.debug(line)
            
            if line.startswith("#define"):
               self.parse_macro(line)
        
