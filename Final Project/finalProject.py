#Dillon Bales

#Video Game Inventory System 


class Player:
    player_roster = []
    def __init__(self, player_name, player_level):
        self.player_name = player_name
        self.player_level = player_level
        self.inventory = []
        self.capacity = 0
        self.max_capacity = 500
        Player.player_roster.append(self)

    #Displays all players that have been created
    @classmethod
    def display_lobby(cls):
        print(f"Players in lobby:")
        for player in cls.player_roster:
            print(f"{player.player_name}: lvl {player.player_level}")
        print("")


    #add an item to player's inventory    
    def add_item(self, item):
        if item.weight + self.capacity <= self.max_capacity:
            self.inventory.append(item)
            self.capacity += item.weight
            print(f"{item.name} added to {self.player_name}'s inventory\nCapacity: {self.capacity}/{self.max_capacity}\n")
        else:
            print(f"Cannot add because inventory would be over capacity\nCapacity: {self.capacity}/{self.max_capacity}\n")

    #remove an item from player's inventory
    def remove_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                self.inventory.remove(item)
                self.capacity -= item.weight
                print(f"{item.name} has been removed from {self.player_name}'s inventory\nCapacity: {self.capacity}/{self.max_capacity}\n")
                return
        print(f"Item in not in {self.player_name}'s inventory")

    #displays all the item names in player's inventory
    def open_inventory(self):
        print(f"{self.player_name}'s Inventory:")
        for item in self.inventory:
            print(f"{item.name}")
        print("")

    #displays all the item info for items in player's inventory
    def all_info(self):
        print(f"{self.player_name}'s Inventory (detailed):")
        for item in self.inventory:
            print(f"Item: {item.name}\nValue: {item.value}\nWeight: {item.weight}\n")

    #display weight capacity for player
    def inventory_weight(self):
        print(f"{self.player_name}'s current capacity is at {self.capacity}/{self.max_capacity}\n") 
        

class Item:

    def __init__(self, name, value, weight):
       self.name = name
       self.value = value
       self.weight = weight

    #display item information   
    def item_info(self):
       print(f"Item: {self.name}\n Value: {self.value}\n Weight: {self.weight}\n")

    
class Weapon(Item):
    def __init__(self, name, value, weight, damage):
        super().__init__(name, value, weight)
        self.damage = damage

    def attack(self):
        print(f"Delt {self.damage} damage to ememy")

class Armour(Item):
    def __init__(self, name, value, weight, defence):
        super().__init__(name, value, weight)
        self.defence = defence

    def block(self):
        print(f"Absorbed {self.defence} damage")

class Potion(Item):
    def __init__(self, name, value, weight, effect, duration):
        super().__init__(name, value, weight)
        self.effect = effect
        self.duration = duration

    def drink(self):
        print(f"Player now has {self.effect} for {self.duration}")

# Create Players
player1 = Player("Bjorn", 10)
player2 = Player("Zara", 15)

# Create Items
sword = Weapon("Iron Sword", value=100, weight=30, damage=25)
shield = Armour("Wooden Shield", value=60, weight=20, defence=15)
potion = Potion("Health Potion", value=25, weight=5, effect="Health Regeneration", duration="10 seconds")
axe = Weapon("Battle Axe", value=150, weight=50, damage=40)
armor = Armour("Chainmail", value=120, weight=40, defence=30)

# Test Lobby Display
Player.display_lobby()

# Add Items to Bjorn's Inventory
player1.add_item(sword)
player1.add_item(shield)
player1.add_item(potion)

# Add Items to Zara's Inventory
player2.add_item(axe)
player2.add_item(armor)

# View Inventories
player1.open_inventory()
player1.inventory_weight()
player1.all_info()

player2.open_inventory()
player2.inventory_weight()

# Try Removing Item
player1.remove_item("Health Potion")  
player1.remove_item("Magic Wand")     

# Bjorn's Inventory After Removal
player1.open_inventory()
player1.inventory_weight()

# Testing Item-Specific Methods

# Sword attack
print("Attack with sword:")
sword.attack()

# Shield block
print("Block with sheild:")
shield.block()

# Potion drink
print("Drink potion:")
potion.drink()

# Create a very heavy item
mega_hammer = Weapon("Mega Hammer", value=500, weight=1000, damage=999)

# Testing Overcapacity
player1.add_item(mega_hammer)



