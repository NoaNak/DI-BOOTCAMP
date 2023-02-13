class Door:

    def __init__(self):
        self.is_opened = False

    def open_door(self):
        self.is_opened = True
        print("The door is open")

    def close_door(self):
        self.is_opened = False
        print("The door is open")



class BlockedDoor(Door):
    
    def open_door(self):
        raise AttributeError("The BlockedDoor cannot be opened.")

    def close_door(self):
        raise AttributeError("The BlockedDoor cannot be close.")


