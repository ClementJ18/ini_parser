from typing import List

class Unit:
    def __init__(self, obj : "Object"):
        self.object = obj

    def get_armorset(self, conditions : List["ArmorSetFlags"]):
        for armorset in self.object.ArmorSet:
            if armorset.Conditions in conditions:
                return armorset.Armor

            if armorset.Conditions is None and not conditions:
                return armorset.Armor

        return None

    def get_weapon(self, conditions : List["ModelConditionState"]):
        for weaponset in self.object.WeaponSet:
            if weaponset.Conditions in conditions:
                return weaponset.Weapon

            if weaponset.Conditions is None and not conditions:
                return weaponset.Weapon

        return None

    def get_damage(self, *, conditions : List["ModelConditionState"] = ()):
        #WIP       
        weapon = self.get_weapon(conditions)
        if weapon is None:
            return 0

    def get_health(self):
        return self.object.Body.MaxHealth

    def deal_damage(self, dmg_value : int, dmg_type : "DamageType", *, flanked : bool = False, conditions : List["ModelConditionState"] = ()):
        armorset = self.get_armorset(conditions)
        scalar = armorset.get_damage_scalar(dmg_type, flanked)

        return int(dmg_value * scalar)
