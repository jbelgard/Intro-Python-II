from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms

Sword = Item("Sword", "It's long and sharp")
Shield = Item("Shield", "This will protect you from other sharp things")
Bow = Item("Bow", "Can shoot arrows")
Boots = Item("Boots", "Some sturdy shoes for you to wear")
Bomb = Item("Bomb", "Looks like it could explode and go Boom")
Arrows = Item("Arrows", "A bundle of arrows that need the bow to fire")
Treasure = Item("Treasure Chest", "There used to be something here but it's been cleared out.")
Quiver = Item("Quiver", "A case to hold the arrows")

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. \n Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. \n Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. \n The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player('Jason', room['foyer'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

outside = room["outside"]
foyer = room["foyer"]
overlook = room["overlook"]
narrow = room["narrow"]
treasure = room["treasure"]

outside.add_items()
foyer.add_items(Sword, Quiver)
overlook.add_items(Boots, Bomb, Arrows)
narrow.add_items(Shield, Bow)
treasure.add_items(Treasure)

name = imput("\n Greetings, adventurer.  What is your name?: ")

player = Player(name, room['outside'])

print(f"\n<<< Welcome {name}! >>>")
print("\n You are about to embark on an adventure, be sure to keep an eye out for useful items that will be helpful to you \n along your path")
print("Be weary of the danger that lurks around every corner.")
print("Good luck!")

while True:
    print(f"\n Current location: {player.current_room.name}")
    print(f" {player.current_room.description}")
    if len(player.current_room.items) >= 1:
        print("\n<<< Items in this room >>>")
        for item in player.current_room.items:
            print(f" {item.name}: {item.description}")
    if len(player.current_room.items) == 0:
        print("\n<<< No items in here >>>")

    myInput = input(f"------\nType Command for game commands\n-------\n What do you want to do?: ")

    if(myInput == 'q'):
        print(f"!!! Thanks for playing! !!!")
        break

    elif(myInput == 'n'):
        if hasattr(player.current_room, 'n_to'):
            player.current_room = player.current_room.n_to
            print("\n<<< You decide to head North >>>")
        else:
            print("\n<<< You can't go there! >>>")
    elif (myInput == 'e'):
        if hasattr(player.current_room, 'e_to'):
            player.current_room = player.current_room.e_to
            print("\n<<< You decide to head East >>>")
        else:
            print("\n<<< You can't go there! >>>")
    elif (myInput == 's'):
        if hasattr(player.current_room, 's_to'):
            player.current_room = player.current_room.s_to
            print("\n<<< You decide to head South >>>")
        else:
            print("\n<<< You can't go there! >>>")
    elif (myInput == 'w'):
        if hasattr(player.current_room, 'w_to'):
            player.current_room = player.current_room.w_to
            print("\n<<< You decide to head West >>>")
        else:
            print("\n<<< You can't go there! >>>")
    elif(myInput == 'i'):
        print(f"\n<<< Player inventory >>>")
        for item in player.inventory:
            print(f" {item.name}: {item.description}")

    elif (myInput.split()[0] == 'Get'):
        for item in player.current_room.items:
            if item.name == myInput.split()[1]:
                player.pick_up_item(item)
                print(f"\n<<< You picked up the{myInput[3:]} >>>")

    elif (myInput.split()[0] == 'Set'):
        for item in player.inventory:
            if item.name == myInput.split()[1]:
                player.drop_item(item)
                print(f"\n<<< You dropped up your{myInput[3:]} >>>")

    elif (myInput == 'Command'):
        print(f" \n<<< n = Go North, e = Go East, s = Go South, w = Go West, Get [ITEM NAME] = Add item to inventory,\n Drop [ITEM NAME] = Drop item from inventory, i = Inventory, q = Quit game >>>")

    else:
        print("\n<<< You don't know how to do that! >>>")

#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
