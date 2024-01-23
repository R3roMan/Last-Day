import pygame
import math

class Background:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.amount = 0
        self.scroll = 0
        self.rect = pygame.Rect(x, y, width, height)


        self.background_image = pygame.image.load("Background.png")
        self.background_image = pygame.transform.scale(self.background_image, (width, height))
        self.background_surface = pygame.Surface((width * 3, height))
        for i in range(3):
            self.background_surface.blit(self.background_image, (i * width, 0))


    def draw_background(self, DISPLAYSCREEN, camera_obj, bob):
        back_draw_pos = camera_obj.apply(self)
        self.scroll = back_draw_pos.x + 10

        for i in range(0, self.amount):
            DISPLAYSCREEN.blit(self.background_surface, (i*self.width + 0.25*self.scroll, 0))
#            self.rect.x = i*self.width + back_draw_pos.x
#            self.rect.y = back_draw_pos.y
            pygame.draw.rect(DISPLAYSCREEN, "Yellow", self.rect, 5)


    def tiles_amount(self):
        self.amount = math.ceil(1200/self.width) + 2
  
