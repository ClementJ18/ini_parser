# ini_parser
 python library for parsing BFME ini files
 
This library allows you to walk through BFME ini files in a programatical manner. Mostly everything is parsed and returned as python objects. This library is still in its early stages.

This library parses objects using python's type hint system. A subclass of IniObject is annotated and then the parser function runs through it. Objects are only converted when the user tries to get them, until then they are stored as strings.

## Parsed Objects
- [x] Upgrades
- [x] Armor
- [x] SpecialPower
- [x] Sciences
- [x] ObjectCreationLists
- [x] CommandButtons
- [x] CommandSets
- [x] ExperienceLevels
- [x] ModifierLists
- [x] Weapon
   - [x] Nuggets
- [x] PlayerTemplates

- [ ] Object
- [ ] ChildObject
- [ ] Behaviors 
