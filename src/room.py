# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    
    def __str__(self):
        display_string = ""
        display_string += f"\n----------------\n"
        display_string += f"\nLocation: {self.name}\n"
        display_string += f"\nDetails: {self.description}\n"
        display_string += f"\nItems  Available: {self.items}\n"
        #display_string += f"\n{self.get_exits_string()}\n"
        return display_string
    
    def get_room_in_direction(self, direction):
        if hasattr(self, f"{direction}_to"):
            return getattr(self, f"{direction}_to")
        return None

        '''
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None
        '''
    
    def remove_item(self, item):
        self.items.remove(item)
    
    def add_item(self, item):
        self.items.append(item)