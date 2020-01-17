from room import Room
from player import Player
from item import Item
# Declare all the room

possible_items = {
    'sword': Item("sword", "Good handle"),
    'shield': Item("shield", "Sturdy"),
    'arrows': Item("arrows", "Pair with bow"),
    'health': Item("potion", "Refreshing!"),
    'axe': Item("axe", "For axing"),
    'bow': Item('bow', 'Arrows?'), 
    'treasure': Item('gold', 'Buy something nice')
}
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [possible_items['health'], possible_items['arrows'],possible_items['bow']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [possible_items['shield']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [possible_items['sword'], possible_items['axe']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [possible_items['treasure']]),
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

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
# Make a new player object that is currently in the 'outside' room.
p = Player(input("What\'s your name?:   ") , room['outside'])
print()
print("Move in certain direction: n, s, e, w")
print("Check inventory: i")
print()

print(p.current_room)

directions = ['n', 's', 'e', 'w']

while True:
    m = input("\nWhat would you like to do?   ")
    if len(m) == 1:

        if m in directions:
            p.move_player(m)
        elif m == "i":
            print("Inventory:  ")
            if (len(p.inventory) == 0):
                print('No items')
            else:
                for i in range(len(p.inventory)):
                    print(p.inventory[i])
            print()
        #elif m == ""
        elif m == "q":
            # Quit
            print("Goodbye!")
            exit()
        else:
            print("\nDid not recognize that command")
    
    else:
        
        if m.split(' ')[0] in ['get', 'take']:
            p.get_item(m.split(' ')[1])

        elif m.split(' ')[0] == 'drop':
            p.drop_item(m.split(' ')[1])

        else:
            print("\nNo such item available")




