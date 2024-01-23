import pygame

class Rooms:

    def __init__(self, design, width, height, state, checked):
        self.x = 0
        self.y = 0
        self.design = design
        self.width = width
        self.height = height
        self.state = state
        self.checked = checked

    
    def change_rooms(self):
        self.state = False
        if self.checked == False:
            self.check = True
        return self.numb
