# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, inventory=None):
        self.name = name
        self.current_room = current_room
        self.inventory = []
        
    def move_player(self, direction):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else: 
            print("\nYou cannot move in that direction")
        
    def get_item(self, item):
        for room_item in self.current_room.items:
            if room_item.name == item:
                self.inventory.append(room_item)
                room_item.on_take()
                self.current_room.remove_item(room_item)
            
    def drop_item(self, item):
        for inventory_item in self.inventory:
            if inventory_item.name == item:
                self.inventory.remove(inventory_item)
                inventory_item.on_drop()
                self.current_room.add_item(inventory_item)
            