import pygame

class Recpoint:

    def __init__(self, x, y, active):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 200
        self.active = active
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def update(self, DISPLAYSCREEN, camera_obj):
        adjusted = camera_obj.apply(self)
        pygame.draw.rect(DISPLAYSCREEN, "white", (adjusted.x, adjusted.y, self.width, self.height))
    
