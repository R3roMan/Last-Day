import pygame

class Plat():
    def __init__(self, type, plat_x, plat_y, width, height):
        self.type = type
        self.x = plat_x
        self.y = plat_y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(plat_x, plat_y, width, height)
        self.img = pygame.image.load("C:\D\Programming\Python\plat.png")
        self.l1_platforms = []

    def update(self):
        pass

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def draw(self, DISPLAYSCREEN, camera):
        platform_draw_pos = camera.apply(self)
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        DISPLAYSCREEN.blit(self.img, (platform_draw_pos.x, platform_draw_pos.y))
        return
