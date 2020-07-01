from .utils import is_comment, remove_comments, clean_raw, is_end
from .objects import get_obj, String, FilterList, Operation
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
        attribute = getattr(self, dict_name, {})
        
        if not key in attribute:
            raise ValueError(f"{key} does not exist in {dict_name}")
            
        return attribute[key]
        
        
    def get_macro(self, macro):
        if isinstance(macro, float) or macro is None:
            return macro
            
        try:
            return float(macro)
        except ValueError:
            pass
            
        if not macro in self.macros:
            raise ValueError(f"No macro called {macro} exists")
            
        return self.macros[macro]

        
    def parse(self, raw):
        lines = iter(clean_raw(raw))
        
        while True:
            try:
                line = next(lines)
            except StopIteration:
                break
                        
            logging.info(line)
            class_name, obj_name = line.split(maxsplit=1)
            if obj := get_obj(class_name):
                obj.parse(self, obj_name, lines)
            elif line.startswith("#define"):
                self.parse_macro(line)
                
    def compile(self, raw, obj_name):
        lines = clean_raw(raw)
        data = defaultdict(list)
        
        for line in lines:
            if is_comment(line):
                continue
            
            logging.info(line)    
            line = remove_comments(line.strip())
            
            if not line.startswith(obj_name) and not is_end(line):
                key, value = line.split("=")
                data[key.strip()].extend(value.split())
                
        return data 
  
        
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
        
        try:
            number = float(value.replace("%", ""))
            self.macros[name] = number if not "%" in value else number / 100
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
            else:
                self.macros[name] = [KindsOf[x] for x in value.split()]
            return
        except IndexError:
            self.macros[name] = value
        
    def parse_macros(self, raw):
        lines = clean_raw(raw)
        
        for line in lines:
            logging.debug(line)
            
            if line.startswith("#define"):
               self.parse_macro(line)
        
