class Room(object):
    def __init__(self, name, south, east, north, west, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


entrance = Room("Entrance of House", None, "Locked Door", "Empty Rm1", "The door is behind you and is locked.")
EmptyRm1 = Room("Empty Room", "Kitchen", )

current_node = entrance
directions = ['north', 'south', 'east', 'west']

while True:
    print(current_node['NAME'])  # Change
    print(current_node['DESCRIPTION'])  # Change
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            # Change
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")
