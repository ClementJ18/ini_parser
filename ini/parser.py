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
            class_name, obj_name = line.split()
            if obj := get_obj(class_name):
                obj.parse(self, obj_name, lines)
                
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
                
    def parse_macros(self, raw):
        lines = raw.splitlines()
        
        for line in lines:
            logging.debug(line)
            
            if line.startswith("#"):
                _, name, value = line.split(maxsplit=2)
                value = remove_comments(value, macro=True)
                
                try:
                    number = float(value.replace("%", ""))
                    self.macros[name.strip()] = number if not "%" in value else number / 100
                    continue
                except ValueError:
                    pass
                    
                if value in ["Yes", "No"]:
                    self.macros[name.strip()] = value == "Yes"
                    continue
                
                if match := re.match(r"#(\w*)\( (\w*) ([a-zA-Z0-9_.]*) \)", value):
                    operation = match.group(1)
                    args = match.group(2, 3)
                    self.macros[name.strip()] = Operation(operation, args, self)
                    continue
                    
                if value[0].isdigit():
                    self.macros[name.strip()] = value
                    continue
                
                try:
                    if value.split()[0] in Descriptors.__members__ or value.split()[0].startswith('-'):
                        self.macros[name.strip()] = FilterList(name.strip(), value.split())
                    else:
                        self.macros[name.strip()] = [KindsOf[x] for x in value.split()]
                    continue
                except IndexError:
                    self.macros[name.strip()] = value
        
