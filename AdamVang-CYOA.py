import time
import random

# time_delay_short = .2  # default is 2
# time_delay_long = .3  # Default is 3
#
#
# Instruction = {
#     print('Welcome to Escape The House'),
#     time.sleep(time_delay_short),
#     print("You was trick into a haunted house by bullies."),
#     print("There is a ghost in the house that will get closer"),
#     print("to you each time you make a move."),
#     time.sleep(time_delay_long),
#     print("There are multiple items to find and puzzle to solve to"),
#     print("get the key to open the lock in the front door"),
#     time.sleep(time_delay_long),
#     print("There are lockers all around where you can"),
#     print("hide in so you won't get caught by the ghost."),
#     time.sleep(time_delay_long),
#     print("When the ghost is close to you, you have a"),
#     print("weird sense of feeling in the air."),
#     print("At that moment, you should HIDE in one of the locker."),
#     time.sleep(time_delay_short),
#     print("Good Luck")
# }

print()

To_Do_List = {
    print('Find a weapon and kill'),
    print('the ghost until she find you.'),
    print('Kill her before she kills you.')
}

print('------------------------------------')

# def hide():
#     Interactable.hide(locker)
#     print()
#     cmd = ""
#     while cmd != "get out":
#         cmd = input(">_ ")
#         if cmd == "get out":
#             Interactable.get_out(locker)
#     print()
#     move_monster()
#     print("The ghost is at the %s " % ghost.location.name)

# Items
class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def pick_up(self):
        print("You picked up the %s" % self.name)

    def drop(self):
        print("You dropped the %s" % self.name)

    def eat(self):
        print("You ate the %s" % self.name)

    def drink(self):
        print("You drank the %s" % self.name)

    def put_on(self):
        print("You put on the %s" % self.name)

    def open(self):
        print("You opened the %s" % self.name)


class Interactable(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def move(self):
        print("You move the %s" % self.name)

    def hide(self):
        print("You hid in the locker.")

    def open(self):
        print("You open the %s" % self.name)

    def get_out(self):
        print("You got out of the locker.")

class Weapon(Item):
    def __init__(self, name, description):
        super(Weapon, self).__init__(name, description)

    def pick_up(self):
        print('You picked up the %s.' % self.name)

    def drop(self):
        print('You dropped the %s.' % self.name)

class knife(Weapon):
    def __init__(self, name, description):
        super(knife, self).__init__(name, description)

    def pick_up(self):
        print('You picked up the %s' % self.name)

    def drop(self):
        print('You dropped the %s.' % self.name)

class sword(Weapon):
    def __init__(self, name, description):
        super(sword, self).__init__(name, description)

    def pick_up(self):
        print('You picked up the %s' % self.name)

    def drop(self):
        print("You dropped the %s" % self.name)

class blades(Weapon):
    def __init__(self, name, description):
        super(blades, self).__init__(name, description)

    def pick_up(self):
        print("You picked up the %s." % self.name)

    def drop(self):
        print("You dropped the %s" % self.name)

# Intractable
class Locker(Interactable):
    def __init__(self, name, description):
        super(Locker, self).__init__(name, description)

    def hide(self):
        Interactable.hide(self.name)

    def get_out(self):
        Interactable.hide(self.name)


class PadLock(Interactable):
    def __init__(self, name, description):
        super(PadLock, self).__init__(name, description)

    def open(self):
        Interactable.open(self.name)


class Safe(Interactable):
    def __init__(self, name, description, items=None):
        super(Safe, self).__init__(name, description)
        self.items = items

    def open(self):
        Interactable.open(self.name)


class Drawer(Interactable):
    def __init__(self, name, description, items=None):
        super(Drawer, self).__init__(name, description)
        self.items = items

    def open(self):
        Interactable.open(self.name)


class FrontDoor(Interactable):
    def __index__(self, name, description):
        super(FrontDoor, self).__init__(name, description)

    def open(self):
        Interactable.open(self.name)


# Tool
class Tool(Item, Interactable):
    def __init__(self, name, description):
        Item.__init__(self, name, description)
        Interactable.__init__(self, name, description)

    def open(self):
        Interactable.open(self.name)


# Keys/Tool
class Key(Tool):
    def __init__(self, name, description):
        Item.__init__(self, name, description)
        Interactable.__init__(self, name, description)

    def open(self):
        Interactable.open(self.name)


class LockKey(Key):
    def __init__(self, name, description):
        super(LockKey, self).__init__(name, description)

    def open(self):
        Key.open(self.name)

    def pick_up(self):
        Item.pick_up(self.name)

    def drop(self):
        Item.drop(self.name)


class SafeKey(Key):
    def __init__(self, name, description):
        super(SafeKey, self).__init__(name, description)

    def open(self):
        Key.open(self.name)

    def pick_up(self):
        Item.pick_up(self.name)

    def drop(self):
        Item.drop(self.name)


class StorageKey(Key):
    def __init__(self, name, description):
        super(StorageKey, self).__init__(name, description)

    def open(self):
        Key.open(self.name)

    def pick_up(self):
        if Item.pick_up(self.name):
            print("You picked up the storage key.")

    def drop(self):
        Item.drop(self.name)

    def use(self, player):
        if player.location.name == "Arcade Room":
            player.location.south = "storage_rm"
            print("You unlock the door to the storage room")
        else:
            print("The key doesn't seem to work here")


# Consumable
class Consumable(Item):
    def __init__(self, name, description):
        super(Consumable, self).__init__(name, description)

    def eat(self):
        Item.eat(self.name)


class Pizza(Consumable):
    def __init__(self, name, description):
        super(Pizza, self).__init__(name, description)

    def pick_up(self):
        Item.put_on(self.name)

    def drop(self):
        Item.drop(self.name)

    def eat(self):
        Item.eat(self.name)


class WaterBottle(Consumable):
    def __init__(self, name, description):
        super(WaterBottle, self).__init__(name, description)

    def pick_up(self):
        Item.put_on(self.name)

    def drop(self):
        Item.drop(self.name)

    def drink(self):
        Item.drink(self.name)


# Wearable
class Wearable(Item):
    def __init__(self, name, description):
        super(Wearable, self).__init__(name, description)

    def put_on(self):
        Item.put_on(self.name)

    def pick_up(self):
        Item.put_on(self.name)

    def drop(self):
        Item.drop(self.name)


class Clothes(Wearable):
    def __init__(self, name, description):
        super(Clothes, self).__init__(name, description)

    def pick_up(self):
        Item.pick_up(self.name)

    def drop(self):
        Item.drop(self.name)

    def put_on(self):
        Item.put_on(self.name)


class Mask(Wearable):
    def __init__(self, name, description):
        super(Mask, self).__init__(name, description)

    def pick_up(self):
        Item.pick_up(self.name)

    def drop(self):
        Item.drop(self.name)

    def put_on(self):
        Item.put_on(self.name)


# Containers
class Container(Item):
    def __init__(self, name, description, items=None):
        super(Container, self).__init__(name, description)
        self.items = items

    def pick_up(self):
        Item.pick_up(self.name)

    def open(self, location):
        location.item = self.items


class Box(Container):
    def __init__(self, name, description, items=None):
        super(Box, self).__init__(name, description)
        self.items = items


class Backpack(Container):
    def __init__(self, name, description, items=None):
        super(Backpack, self).__init__(name, description)
        self.items = items

    def pick_up(self):
        Container.pick_up(self.name)

    def drop(self):
        Container.drop(self.name)


class Jar(Container):
    def __init__(self, name, description, items=None):
        super(Jar, self).__init__(name, description)
        self.items = items


# Character
class Character(object):
    def __init__(self, name, health, inventory, description, location=None):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.description = description
        self.location = location

    def description(self):
        print("%s" % self.description)

    def name(self):
        print("%s" % self.name)

    def health(self):
        print("You took damage. A lot of damage.")

    def inventory(self):
        print(hero.inventory)

    def move(self,direction):
        self.location.character.remove(self)
        try:
            self.location = globals()[getattr(self.location, direction)]
        except KeyError:
            pass
        self.location.character.append(self)


class NPC(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def attack(self):
        print("The ghost killed you.")


class Ghost(Character):
    def __init__(self, name, description):
        super(Ghost, self).__init__(name, None,  None, description)

    def attack(self):
        print("The ghost killed you")

    def move(self, direction):
        try:
            self.location = globals()[getattr(self.location, direction)]
        except KeyError:
            pass

class Hero(Character):
    def __init__(self, name, health, inventory, description, location=None):
        super(Hero, self).__init__(name, health, inventory, description, location)
        self.location = None

    def pick_up(self, item):
        self.inventory = item
        print("You pick up the %s" % item.name)

    def drop(self, item):
        self.inventory = None
        print("You drop the %s" % item.name)

    def open(self, interactable):
        Item.open(self.name)
        Interactable.open(self.name)

    # def hide(self, interactable):
    #     if hero in locker:
    #         Interactable.hide(interactable)
    #         print("You hid in the locker")
    #     else:
    #         print("You are not in a locker.")

    def get_out(self):
        if hero in Locker:
            if self.get_out():
                print("You are out of the locker.")

    def health(self):
        print("You only have 1 health.")

    def move(self, direction):
        self.location = globals()[getattr(self.location, direction)]

    def attack(self):
        print("You killed the ghost.")
        print("Good Game xD")
        quit(0)

    """
    We want the hero to move normally, but we want all other characters to add them to the list of character per room
    
    So, I have a move method in Character, and I override it in the Hero class.
    """
class Room(object):
    def __init__(self, name, south, east, north, west, description, item=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.item = item
        self.character = []

        def move(self, direction):
            self.location = globals()[getattr(self.location, direction)]


# Make Item
# lock_key = LockKey("Lock Key", "This key is use to open the lock on the front door.")
# safe_key = SafeKey("Safe Key", "This key is use to open a safe.")
# storage_key = StorageKey("Storage Key", "You can the lock on the door at the storage key.")
# jar = Jar("Jar", "Looks like you can throw this.")
# backpack = Backpack("Backpack", "You can carry the backpack but it's useless.", lock_key)
# box = Box("Box", "There's nothing in the box, you can move them.")
# mask = Mask("Mask", "You can wear this mask to make your self looks cool.")
# clothes = Clothes("Clothes", "You can wear these clothes to make you looks good.")
# water_bottle = WaterBottle("Watter Bottle", "Still looks drinkable.")
# pizza = Pizza("Pizza", "This pizza still looks eatable.")
# locker = Locker("Locker", "You can hide in it.")
# drawer = Drawer("A Desk Drawer", "There could be item in this.")
# safe = Safe("Safe", "You can open this with a safe key.")
# padlock = PadLock("PadLock", "You can open this lock with a lock key.")
mini_knife = knife("Knife", 'This is just a regular kitchen knife.')
Ryu_ichimonji = sword("Ryū ichimonji", 'This sword belongs to genji. How did it end up here?')
Blades_Of_Chaos = blades("Blades of Chaos", 'These weapon was given by the god of war... Aries...')

# Make Characters
hero = Hero("Dashie", 1, [], "You are T H I C C and you don't have aim.")
ghost = Ghost("Tina", "She is satan daughter.")


entrance = Room("Entrance of House", None, None, "Locked Door", "empty_rm1", "The door is behind you is locked.")
empty_rm1 = Room("Empty Room", "kitchen", "entrance", None, "livingRm", "This is a empty room with a locker.")
kitchen = Room("Kitchen", None, None, "empty_rm1", "empty_rm2", "This is a nice kitchen.")
empty_rm2 = Room("Empty Room", None, "kitchen", "living_rm", None, "Looks like a empty room.")
living_rm = Room("Living Room", "empty_rm2", "empty_rm1", "hallway", "arcade_rm", "There is just"
                                                                                  "a tilted picture frame.")
arcade_rm = Room("Arcade Room", "storage_rm", "living_rm", "empty_rm3", None, "There's a lot of lockers and games.")
storage_rm = Room("Storage Room", None, None, "arcade_rm", None, "There's a safe inside the storage room.")
empty_rm3 = Room("Empty Room", "arcade_rm", None, None, None, "There's is 1 locker in this room.")
hallway = Room("HallWay", "living_rm", "bedroom1", "bedroom2", None, "There's a lot of scary paints and lockers.")
bedroom1 = Room("BedRoom", None, "bathroom1", "closet1", "hallway", "There's a bed with a desk.")
bathroom1 = Room("BathRoom", None, None, None, "bedroom1", "Just a small bedroom.")
closet1 = Room("Closet", "bedroom1", None, None, None, "This closet have a lot of boxes and clothes.")
bedroom2 = Room("BedRoom", "hallway", None, "bathroom2", "closet2", "This is a normal bedroom with a locker.")
closet2 = Room("Closet", None, "bedroom2", None, None, "This closet have a lot of boxes and clothes.")
bathroom2 = Room("Bathroom", "bedroom2", None, None, None, "The bathroom have creepy painting.")


# def randomize_container():
#     list_of_keys = [storage_key, lock_key, safe_key]
#     list_of_containers = [backpack, jar, box, drawer, safe]
#     for key in list_of_keys:
#         picked = False
#         container = None
#         while not picked or container is None:
#             container = random.choice(list_of_containers)
#             if key in [safe_key, storage_key] and container == safe:
#                 pass
#             else:
#                 picked = True
#         container.items = key


def randomize_item_room():
    list_of_items = [mini_knife, Blades_Of_Chaos, Ryu_ichimonji]
    list_of_rooms = [entrance, empty_rm1, empty_rm2, empty_rm3, kitchen, living_rm, arcade_rm, storage_rm,
                     hallway, bedroom1, bedroom2, closet1, closet2, bathroom1, bathroom2]
    for item in list_of_items:
        room = random.choice(list_of_rooms)
        room.item = item
        list_of_rooms.remove(room)


hero.location = entrance

list_of_room2 = [empty_rm1, empty_rm2, empty_rm3, kitchen, living_rm, arcade_rm, storage_rm,
                hallway, bedroom1, bedroom2, closet1, closet2, bathroom1, bathroom2]

#
# def place_monster():
#     for ghost in monster:
#         room = random.choice(list_of_room2)
#         ghost.location = room
#         room.character.append(ghost)


monster = [ghost]
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']
# randomize_container()
randomize_item_room()


def place_monster():
    for ghost in monster:
        room = random.choice(list_of_room2)
        ghost.location = room
        room.character.append(ghost)
#
def move_monster():
    for char in monster:
        rand_direction = random.choice(directions)
        try:
            char.move(rand_direction)
        except ValueError:
            print(char.name)
            print(char.location.name)
            print(rand_direction)
            # quit(2)


# ghost.location = list_of_room2
place_monster()
print(ghost.location.name)

while True:
    print("You are at the %s" % hero.location.name)
    print(hero.location.description)
    
    if hero.location.item is not None:
        print("There is a(n) %s in the room" % hero.location.item.name)
    else:
        print("There is no item in here for you to pick up.")
        print()

    if hero.inventory is not None:
        hero.attack()
    else:
        print("You need a weapon to attack.")

    if len(hero.location.character) > 0:  # If there are characters in the room. This assumes an empty room has a length of 0.
        print("There are the following characters in the room:")
        for char in hero.location.character:
            print(char.name)  # Print each character's name

    if hero.inventory is None:
        print("You died.")
        quit(0)
    else:
        hero.attack()
        print("You killed the ghost.")
        print("Good Job")

    command = input('>_').lower().strip()
    if hero.location.character is not None:
        for character in hero.location.character:
            print(character.name)
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]

    # Items
    # if command[:7] == "pick up":
    #     item = command[8:]
    # if command[:4] == "open":
    #     item = command[5:]

    if ghost in hero.location:
        if 'attack' in command:
            hero.attack()
        else:
            print("She's ain't here.")

    if "take" in command:
        if hero.location.item is not None:
            hero.pick_up(hero.location.item)
            print()
            hero.location.item = None
        else:
            print("There is no item in the room.")
            print()

    elif "drop" in command:
        if hero.inventory is not None:
            hero.location.item = hero.inventory
            hero.drop(hero.inventory)

        else:
            print("You don't have any item in your inventory.")
        # hero.location.item = hero.inventory
        # hero.drop(hero.location.item.inventory.remove)
    elif "open" in command:
        if isinstance(hero.location.item, Container):
            hero.location.item.open(hero.location)
        else:
            print("There is nothing to open")
    # elif "hide" in command:
    #     if locker == hero.location.item:
    #         hide()
    #     else:
    #         print("There's no locker in this room.")
    #         print()
    # elif "get out" in command:
    #     print("You are not in a locker.")
    elif "inventory" in command:
        if hero.inventory is not None:
            print(hero.inventory.name)
            print()
        else:
            print("You got nothing in your inventory.")
            print()
    # Change room
    elif command in directions:
        try:
            hero.move(command)
        except KeyError:
            print("You cannot go this way")
            print()
    else:
        print("Command not recognized")
        print()
    move_monster()
    print("The ghost is at the %s " % ghost.location.name)

# """
# So the ghost is created and can be placed in a random room. We just need it to move on its own
# """
