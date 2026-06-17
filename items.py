from enum import StrEnum

def load_items():
    return [{"name": "Sword", "type": Type.WEAPON, "value": 50},{"name": "Chestplate", "type": Type.ARMOR, "value": 150},{"name": "Dagger", "type": Type.WEAPON, "value": 15},{"name": "Health Potion", "type": Type.CONSUMABLE, "value": 5}, {"name": "Mana Potion", "type": Type.CONSUMABLE, "value": 5}]



#Mostly testing various python related things, ignore
class Type(StrEnum):
    WEAPON = "weapon"
    ARMOR = "armor"
    CONSUMABLE = "consumable"

class Item():
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value
    def __str__(self):
        return f"{self.name} - Type: {self.type} - Value: {self.value}gp"
    def print_json(self):
        return f'"name": "{self.name}", "type": "{self.type}", "value": "{self.value}"'
    
if __name__ == "__main__":
    list_items = []
    list_items.append(Item("Sword", Type.WEAPON, 50))
    list_items.append(Item("Healing Potion", Type.CONSUMABLE, 5))
    list_items.append(Item("Serrated Blade", Type.WEAPON, 122))
    list_items.append(Item("Invisibility Potion", Type.CONSUMABLE, 152))
    list_items.append(Item("Elven Chain", Type.ARMOR, 2500))

    for item in list_items:
        print("{\n", item.print_json(), "\n}")