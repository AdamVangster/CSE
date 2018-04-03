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

    def move(self):
        print("You moved to a different room.")

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

    def inventory(self):
        print("You open you inventory.")

    def health(self):
        print("You only have 1 health.")

    def move(self):
        print("You moved to a different room.")
