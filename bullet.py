import pygame

class Bullet:

    def __init__(self, x, y, width, height, speed, direction, skin):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.direction = direction
        self.rect = pygame.Rect(x, y, width, height)
        if direction == "RIGHT":
            self.img = pygame.image.load(skin + "_bullet_right.png")
        if direction == "LEFT":
            self.img = pygame.image.load(skin + "_bullet_left.png")

    
    def update(self, DISPLAYSCREEN, bob, camera):
        bullet_draw_pos = camera.apply(self)
        if self.direction == "RIGHT":
            self.x += self.speed
        if self.direction == "LEFT":
            self.x -= self.speed
        DISPLAYSCREEN.blit(self.img, (self.x, bullet_draw_pos.y))
    
    def destroy(self, bob,  player_draw_pos):
        if self.x > (player_draw_pos.x + (1200//2)) or self.x < (player_draw_pos.x - (1200//2)):
            return True
        else:
            return False
        
    
