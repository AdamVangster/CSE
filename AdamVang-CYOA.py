import time
import random
time_delay_short = .2  # default is 2
time_delay_long = .3  # Default is 3

Instruction = {
    print('Welcome to Escape The House'),
    time.sleep(time_delay_short),
    print("You was trick into a haunted house by bullies."),
    print("There is a ghost in the house that will get closer"),
    print("to you each time you make a move."),
    time.sleep(time_delay_long),
    print("There are multiple items to find and puzzle to solve to"),
    print("get the key to open the lock in the front door"),
    time.sleep(time_delay_long),
    print("There are lockers all around where you can"),
    print("hide in so you won't get caught by the ghost."),
    time.sleep(time_delay_long),
    print("When the ghost is close to you, you have a"),
    print("weird sense of feeling in the air."),
    print("At that moment, you should HIDE in one of the locker."),
    time.sleep(time_delay_short),
    print("Good Luck")
}


# Items
class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def pick_up(self):
        if command == 'pick up':
            print("You picked up the %s" % self.name)

    def drop(self):
        if command == 'drop':
            print("You dropped the %s" % self.name)

    def eat(self):
        if command == 'eat':
            print("You ate the %s" % self.name)

    def drink(self):
        if command == 'drink':
            print("You drank %s" % self.name)

    def put_on(self):
        if command == 'put on':
            print("You put on the %s" % self.name)

    def open(self):
        if command == 'open':
            print("You open the %s" % self.name)


class Interactable(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def move(self):
        if command == 'move':
            print("You moved the %s" % self.name)

    def hide(self):
        if command == 'hide':
            print("You hid in the %s" % self.name)

    def open(self):
        if command == 'open':
            print("You opened the %s" % self.name)


# Intractable
class Locker(Interactable):
    def __init__(self, name, description):
        super(Locker, self).__init__(name, description)

    def hide(self):
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

    def open(self):
        Item.open(self.name)


class Box(Container):
    def __init__(self, name, description, items=None):
        super(Box, self).__init__(name, description)
        self.items = items

    def pick_up(self):
        Container.pick_up(self.name)

    def drop(self):
        Container.drop(self.name)

    def open(self):
        Container.open(self.name)


class Backpack(Container):
    def __init__(self, name, description, items=None):
        super(Backpack, self).__init__(name, description)
        self.items = items

    def pick_up(self):
        Container.pick_up(self.name)

    def open(self):
        Container.open(self.name)

    def drop(self):
        Container.drop(self.name)


class Jar(Container):
    def __init__(self, name, description, items=None):
        super(Jar, self).__init__(name, description)
        self.items = items

    def pick_up(self):
        Container.pick_up(self.name)

    def drop(self):
        Container.drop(self.name)

    def open(self):
        Container.open(self.name)


# Character
class Character(object):
    def __init__(self, name, health, inventory, description):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.description = description

    def description(self):
        print("%s" % self.description)

    def name(self):
        print("%s" % self.name)

    def health(self):
        print("You took damage. A lot of damage.")

    def inventory(self):
        print("Here is you inventory.")


class NPC(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def attack(self):
        print("The ghost killed you.")


class Ghost(NPC):
    def __init__(self, name, description):
        super(Ghost, self).__init__(name, description)

    def attack(self):
        print("The ghost killed you")


class Hero(Character):
    def __init__(self, name, health, inventory, description):
        super(Hero, self).__init__(name, health, inventory, description)
        self.location = None

    def inventory(self):
        print("You open you inventory.")

    def health(self):
        print("You only have 1 health.")

    def move(self, direction):
        self.location = globals()[getattr(self.location, direction)]


# Rooms
class Room(object):
    def __init__(self, name, south, east, north, west, description, item=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.item = item


# Make Item
lock_key = LockKey("Lock Key", "This key is use to open the lock on the front door.")
safe_key = SafeKey("Safe Key", "This key is use to open a safe.")
storage_key = StorageKey("Storage Key", "You can the lock on the door at the storage key.")
jar = Jar("Jar", "Looks like you can throw this.")
backpack = Backpack("Backpack", "You can carry the backpack but it's useless.", lock_key)
box = Box("Box", "There's nothing in the box, you can move them.")
mask = Mask("Mask", "You can wear this mask to make your self looks cool.")
clothes = Clothes("Clothes", "You can wear these clothes to make you looks good.")
water_bottle = WaterBottle("Watter Bottle", "Still looks drinkable.")
pizza = Pizza("Pizza", "This pizza still looks eatable.")
locker = Locker("Locker", "You can hide in it.")
drawer = Drawer("A Desk Drawer", "There could be item in this.")
safe = Safe("Safe", "You can open this with a safe key.")
padlock = PadLock("PadLock", "You can open this lock with a lock key.")
frontdoor = FrontDoor("Front Door", "You can open the door.")

# Make Characters
hero = Hero("Dashie", 1, False, "You are T H I C C and you don't have aim.")
ghost = Ghost("Tina", "She is satan daughter.")

# Make Rooms
entrance = Room("Entrance of House", None, None, "Locked Door", "empty_rm1", "The door is behind you is locked.")
empty_rm1 = Room("Empty Room", "kitchen", "entrance", None, "livingRm", "This is a empty room with a locker.")
kitchen = Room("Kitchen", None, None, "empty_rm1", "empty_rm2", "There's a cabinet that is open.")
empty_rm2 = Room("Empty Room", None, "kitchen", "living_rm", None, "A empty room with a backpack.", backpack)
living_rm = Room("Living Room", "empty_rm2", "empty_rm1", "hally_way", "arcade_Rm", "There's a tilted picture frame.")
arcade_rm = Room("Arcade Room", "storage_rm", "living_rm", "empty_rm3", None, "There's a lot of lockers and games.")
storage_rm = Room("Storage Room", None, None, "arcade_rm", None, "There's a safe inside the storage room.")
empty_rm3 = Room("Empty Room", "arcade_rm", None, None, None, "There's is 1 locker in this room.")
hallway = Room("HallWay", "living_rm", "bedroom1", "bedroom2", None, "There's a lot of scary paints and lockers.")
bedroom1 = Room("BedRoom", None, "bathroom1", "closet1", "hallway", "There's a bed with a desk.")
bathroom1 = Room("BathRoom", None, None, None, "bedroom1", "This is a small bathroom with a small crack on the wall.")
closet1 = Room("Closet", "bedroom1", None, None, None, "This closet have a lot of boxes and clothes.")
bedroom2 = Room("BedRoom", "hallway", None, "bathroom2", "closet2", "This is a normal bedroom with a locker.")
closet2 = Room("Closet", None, "bedroom2", None, None, "This closet have a lot of boxes and clothes.")
bathroom2 = Room("Bathroom", "bedroom2", None, None, None, "The bathroom have creepy painting.")


def randomize_containter():
    list_of_keys = [storage_key, lock_key, safe_key]
    list_of_containers = [backpack, jar, box, drawer, safe]
    for key in list_of_keys:
        picked = False
        container = None
        while not picked or container is None:
            container = random.choice(list_of_containers)
            if key in [safe_key, storage_key] and container == safe:
                pass
            else:
                picked = True
        container.items = key


def randomize_item_room():
    list_of_items = [backpack, jar, drawer, box]
    list_of_rooms = [storage_rm, arcade_rm, empty_rm2, bedroom1, closet2, living_rm, closet1, kitchen,
                     entrance, empty_rm1, empty_rm3]
    for item in list_of_items:
        room = random.choice(list_of_rooms)
        room.item = item
        list_of_rooms.remove(room)


hero.location = entrance
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']
randomize_containter()
randomize_item_room()

while True:
    print(hero.location.name)
    print(hero.location.description)
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            hero.move(command)
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")
