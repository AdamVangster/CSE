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
Horror_House_Map = {
    'ENTRANCE': {
        'NAME': 'Entrance Of House',
        'DESCRIPTION': 'You are at the front of the door. The door is behind you.',
        'PATHS': {
            'WEST': 'EMPTY RM.1',
            'SOUTH': '...',
            'NORTH': '...',
            'EAST': 'Locked Door'
        }
    },
    'EMPTY RM.1': {
        'NAME': 'Empty Room',
        'DESCRIPTION': 'This is a empty room with one locker.',
        'PATHS': {
            'WEST': 'LIVING RM.',
            'SOUTH': 'KITCHEN',
            'EAST': 'ENTRANCE',
            'NORTH': '...'
        }
    },
    'KITCHEN': {
        'NAME': 'Kitchen',
        'DESCRIPTION': 'There is a cabinet that is open.',
        'PATHS': {
            'WEST': 'EMPTY RM.2',
            'SOUTH': '...',
            'EAST': '...',
            'NORTH': 'EMPTY  RM.1'
        }
    },
    'EMPTY RM.2': {
        'NAME': 'Empty Room',
        'DESCRIPTION': 'This is a empty room with a locker and a bag.',
        'PATHS': {
            'WEST': '...',
            'SOUTH': '...',
            'EAST': 'KITCHEN',
            'NORTH': 'LIVING RM.'
        }
    },
    'LIVING RM.': {
        'NAME': 'Living Room',
        'DESCRIPTION': 'This is a living room with a picture frame.',
        'PATHS': {
            'WEST': 'ARCADE',
            'SOUTH': 'EMPTY RM.2',
            'EAST': 'EMPTY RM.1',
            'NORTH': 'HALLWAY'
        }
    },
    'ARCADE RM.': {
        'NAME': 'Arcade Room',
        'DESCRIPTION': 'This is a arcade room with lots of games.',
        'PATHS': {
            'WEST': ...,
            'SOUTH': 'STORAGE RM.',
            'EAST': 'LIVING RM.',
            'NORTH': 'EMPTY RM.3'
        }
    },
    'STORAGE RM.': {
        'NAME': 'Storage Room',
        'DESCRIPTION': 'There is a lot of boxes in this room.',
        'PATHS': {
            'WEST': ...,
            'SOUTH': ...,
            'EAST': ...,
            'NORTH': 'ARCADE RM.'
        }
    },
    'EMPTY RM.3': {
        'NAME': 'Empty Room',
        'DESCRIPTION': 'This is a empty room with one locker.',
        'PATHS': {
            'WEST': ...,
            'SOUTH': 'ARCADE RM.',
            'EAST': ...,
            'NORTH': ...
        }
    },
    'HALLWAY': {
        'NAME': 'Hallway',
        'DESCRIPTION': 'This hallway have lockers along the side of it.',
        'PATHS': {
            'WEST': ...,
            'SOUTH': 'LIVING RM.',
            'EAST': 'BEDROOM.1',
            'NORTH': 'BEDROOM.2'
        }
    },
    'BEDROOM.1': {
        'NAME': 'Bedroom',
        'DESCRIPTION': 'This is just a ordinary room with a bed and desks.',
        'PATHS': {
            'WEST': 'HALLWAY',
            'SOUTH': ...,
            'EAST': 'BATHROOM.1',
            'NORTH': 'CLOSET.1'
        }
    },
    'BATHROOM.1': {
        'NAME': 'Bathroom',
        'DESCRIPTION': 'This look like just a normal bathroom.',
        'PATHS': {
            'WEST': 'BEDROOM.1',
            'SOUTH': ...,
            'EAST': ...,
            'NORTH': ...,
        }
    },
    'CLOSET.1': {
        'NAME': 'Closet',
        'DESCRIPTION': 'This closet have a lot of boxes and clothes.',
        'PATHS': {
            'WEST': ...,
            'SOUTH': 'BEDROOM.1',
            'EAST': ...,
            'NORTH': ...
        }
    },
    'BEDROOM.2': {
        'NAME': 'Bedroom',
        'DESCRIPTION': 'This is a normal Bedroom with a locker.',
        'PATHS': {
            'WEST': 'CLOSET.2',
            'SOUTH': 'HALLWAY',
            'EAST': ...,
            'NORTH': 'BATHROOM.2'
        }
    },
    'CLOSET.2': {
        'NAME': 'Closet',
        'DESCRIPTION': 'This closet have lots of boxes and clothes.',
        'PATHS': {
            'WEST': ...,
            'SOUTH': ...,
            'EAST': 'BEDROOM.2',
            'NORTH': ...,
        }
    },
    'BATHROOM.2': {
        'NAME': 'Bathroom',
        'DESCRIPTION': 'This bathroom have a creepy painting.',
        'PATHS': {
            'WEST': ...,
            'SOUTH': 'BEDROOM.2',
            'EAST': ...,
            'NORTH': ...
        }
    }
}

current_node = Horror_House_Map['ENTRANCE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = Horror_House_Map[name_of_node]
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")
