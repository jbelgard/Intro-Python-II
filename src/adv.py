from room import Room
from player import Player
from item import Item

# Declare all the rooms

item1 = Item("Sword", "It's long and sharp")
item2 = Item("Shield", "This will protect you from other sharp things")
item3 = Item("Bow", "Can shoot arrows")
item4 = Item("Boots", "Some sturdy shoes for you to wear")
item5 = Item("Bomb", "Looks like it could explode and go Boom")
item6 = Item("Arrows", "A bundle of arrows that need the bow to fire")
item7 = Item("Treasure Chest", "There used to be something here but it's been cleared out.")
item8 = Item("Quiver", "A case to hold the arrows")

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

outside.add_items([])
foyer.add_items([item1, item8])
overlook.add_items([item4, item5, item6])
narrow.add_items([item2, item3])
treasure.add_items([item7])

print(player1.pick_up_item())

print(f"Welcome {player1.name}!")
print("You are about to embark on an adventure, be sure to keep an eye out for useful items that will be helpful to you along your path")
print("Be weary of the danger that lurks around every corner.")
print("Good luck!")

while True:
    print(f"-----------------")
    print(f" n = North, e = East, s = South, w = West, i = Inventory, q = Quit Game")
    print(f"-----------------")
    print(f"Current location: {player1.current_room.name}")
    print(f" {player1.current_room.description}")
    print(f" Items in room: {player1.current_room.items}")
    print(f"-----------------")

    myInput = input(f"What would you like to do?: ")

    if(myInput == 'q'):
        print(f"!!! Thanks for playing! !!!")
        break
    elif(myInput == 'n'):
        if hasattr(player1.current_room, 'n_to'):
            player1.current_room = player1.current_room.n_to
        else:
            print("!!!! You Can't Go There! !!!")
    elif (myInput == 'e'):
        if hasattr(player1.current_room, 'e_to'):
            player1.current_room = player1.current_room.e_to
        else:
            print("!!! You Can't Go There! !!!")
    elif (myInput == 's'):
        if hasattr(player1.current_room, 's_to'):
            player1.current_room = player1.current_room.s_to
        else:
            print("!!! You Can't Go There! !!!")
    elif (myInput == 'w'):
        if hasattr(player1.current_room, 'w_to'):
            player1.current_room = player1.current_room.e_to
        else:
            print("!!! You Can't Go There! !!!")
    elif(myInput == 'i'):
        print(f"!!! Player inventory: {player1.inventory}!!!")
    elif(myInput ==f'Pick up {Item.name}'):
        player1.current_room.remove_item(Item.name)

    else:
        print("!!! You don't know how to do that! !!!")

#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
