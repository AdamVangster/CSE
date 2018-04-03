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
        print("You drank %s" % self.name)

    def put_on(self):
        print("You put on the %s" % self.name)

    def open(self):
        print("You open the %s" % self.name)


class Interactable(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def move(self):
        print("You moved the %s" % self.name)

    def hide(self):
        print("You hid in the %s" % self.name)

    def smash(self):
        print("You smashed the %s" % self.name)

    def open(self):
        print("You opened the %s" % self.name)


# Intractable
class Locker(Interactable):
    def __init__(self, name, description):
        super(Locker, self).__init__(name, description)

    def hide(self):
        Interactable.hide(self.name)


class Lock(Interactable):
    def __init__(self, name, description):
        super(Lock, self).__init__(name, description)

    def open(self):
        Interactable.open(self.name)


class Safe(Interactable):
    def __init__(self, name, description):
        super(Safe, self).__init__(name, description)

    def open(self):
        Interactable.open(self.name)


class Painting(Interactable):
    def __init__(self, name, description):
        super(Painting, self).__init__(name, description)

    def move(self):
        Interactable.move(self.name)


class Drawer(Interactable):
    def __init__(self, name, description):
        super(Drawer, self).__init__(name, description)

    def open(self):
        Interactable.open(self.name)


class CrackedWall(Interactable):
    def __init__(self, name, description):
        super(CrackedWall, self).__init__(name, description)

    def smash(self):
        Interactable.smash(self.name)


# Tool
class Tool(Item, Interactable):
    def __init__(self, name, description):
        Item.__init__(self, name, description)
        Interactable.__init__(self, name, description)

    def open(self):
        Interactable.open(self.name)

    def smash(self):
        Interactable.smash(self.name)


class Hammer(Tool):
    def __init__(self, name, description):
        Item.__init__(self, name, description)
        Interactable.__init__(self, name, description)

    def smash(self):
        Interactable.smash(self.name)


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


class SafeKey(Key):
    def __init__(self, name, description):
        super(SafeKey, self).__init__(name, description)

    def open(self):
        Key.open(self.name)


# Consumable
class Consumable(Item):
    def __init__(self, name, description):
        super(Consumable, self).__init__(name, description)

    def eat(self):
        Item.eat(self.name)


class Pizza(Consumable):
    def __init__(self, name, description):
        super(Pizza, self).__init__(name, description)

    def eat(self):
        Item.eat(self.name)


class WaterBottle(Consumable):
    def __init__(self, name, description):
        super(WaterBottle, self).__init__(name, description)

    def drink(self):
        Item.drink(self.name)


# Wearable
class Wearable(Item):
    def __init__(self, name, description):
        super(Wearable, self).__init__(name, description)

    def put_on(self):
        Item.put_on(self.name)


class Clothes(Wearable):
    def __init__(self, name, description):
        super(Clothes, self).__init__(name, description)

    def put_on(self):
        Item.put_on(self.name)


class Mask(Wearable):
    def __init__(self, name, description):
        super(Mask, self).__init__(name, description)

    def put_on(self):
        Item.put_on(self.name)


# Containers
class Container(Item):
    def __init__(self, name, description):
        super(Container, self).__init__(name, description)

    def pick_up(self):
        Item.put_on(self.name)

    def open(self):
        Item.open(self.name)


class Box(Container):
    def __init__(self, name, description):
        super(Box, self).__init__(name, description)

    def pick_up(self):
        Container.put_on(self.name)

    def open(self):
        Container.open(self.name)


class Backpack(Container):
    def __init__(self, name, description):
        super(Backpack, self).__init__(name, description)

    def pick_up(self):
        Container.pick_up(self.name)

    def open(self):
        Container.open(self.name)


class Jar(Container):
    def __init__(self, name, description):
        super(Jar, self).__init__(name, description)

    def pick_up(self):
        Container.pick_up(self.name)

    def open(self):
        Container.open(self.name)
