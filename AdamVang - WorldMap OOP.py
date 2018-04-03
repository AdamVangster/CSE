import time
Instruction = {
    print('Welcome to Escape The House'),
    time.sleep(2),
    print("You was trick into a haunted house by bullies."),
    print("There is a ghost in the house that will get closer"),
    print("to you each time you make a move."),
    time.sleep(3),
    print("There is a key somewhere in the house to open the"),
    print("the lock on the front door."),
    time.sleep(3),
    print("There are lockers all around where you can"),
    print("hide in so you won't get caught by the ghost."),
    time.sleep(3),
    print("When the ghost is close to you, you have a"),
    print("weird sense of feeling in the air."),
    print("At that moment, you should HIDE."),
    time.sleep(2),
    print("Good Luck")
}


class Room(object):
    def __init__(self, name, south, east, north, west, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description


entrance = Room("Entrance of House", None, None, "Locked Door", "empty_rm1", "The door is behind you is locked.")
empty_rm1 = Room("Empty Room", "kitchen", "Entrance", None, "LivingRm", "This is a empty room with a locker.")
kitchen = Room("Kitchen", None, None, "empty_rm1", "empty_rm2", "There's a cabinet that is open.")
empty_rm2 = Room("Empty Room", None, "kitchen", "living_rm", None, "A empty room with a backpack.")
living_rm = Room("Living Room", "empty_rm2", "empty_rm1", "hally_way", "arcade_Rm", "There's a tilted picture frame.")
arcade_rm = Room("Arcade Room", "storage_rm", "living_rm", "empty_rm3", None, "There's a lot of lockers and games.")
storage_rm = Room("Storage Room", None, None, "arcade_rm", None, "This is a lot of boxes in this room.")
empty_rm3 = Room("Empty Room", "arcade_rm", None, None, None, "There's is 1 locker in this room.")
hallway = Room("HallWay", "living_rm", "bedroom1", "bedroom2", None, "There's a lot of scary paints and lockers.")
bedroom1 = Room("BedRoom", None, "bathroom1", "closet1", "hallway", "There's a bed with a desk.")
bathroom1 = Room("BathRoom", None, None, None, "bedroom1", "This is a small bathroom with a small crack on the wall.")
closet1 = Room("Closet", "bedroom1", None, None, None, "This closet have a lot of boxes and clothes.")
bedroom2 = Room("BedRoom", "hallway", None, "bathroom2", "closet2", "This is a normal bedroom with a locker.")
closet2 = Room("Closet", None, "bedroom2", None, None, "This closet have a lot of boxes and clothes.")
bathroom2 = Room("Bathroom", "bedroom2", None, None, None, "The bathroom have creepy painting.")


current_node = entrance
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")
