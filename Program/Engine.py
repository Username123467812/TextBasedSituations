# config data
# NOTE: Anything that you want described in the room must be added as an object, inclduing the floor, walls, ceiling lights, and other details about the room.
objs = [[]]
rooms = [[]]
start_room_index = 0
start_msg = ""
# the 'rooms' array is an array of arrays of object names

# used in in the engine's running (don't touch unless modifying code)
room_index = -1
room_contents = []
command = ""
command_array = []

def startup():

    # if we did not obtain a saved room index, set it to the starting room 
    if room_index < 0:
        room_index = start_room_index
    
    room_contents = rooms[room_index]

def ask_command():
    command = input("Enter a command: ")

def run_command(_command):
    _output = []
    if _command[0] == "help" or _command[0] == "?":
        _output = ["'inspect' to inspect an object.","'room' to get a list of inspectable objects in the room."]
    elif _command[0] == "":
        _output = ["Enter a command!"]
    elif _command[0] == "room":
        _output = room_contents
    elif _command[0] == "inspect":
        _output = ["---REPLACE THIS LATER---"]
    else:
        _output = ["Unknown command!"]


    # print the command output
    print(_output)