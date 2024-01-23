import pygame


class Camera():
    def __init__(self, width, height):
        self.rect = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height


    def apply(self, target):
        new = target.rect.move(self.rect.topleft)
        return new

    def update(self, DISPLAYSCREEN, target, WIDTH, HEIGHT):
        x = -target.rect.x + WIDTH // 2 
        y = -target.rect.y + HEIGHT // 2

        new_width = self.width // 5
        new_height = self.height // 5

        self.rect = pygame.Rect(x, y, new_width, new_height)
        #DISPLAYSCREEN.blit(player.img, (-self.rect[0], -self.rect[1]))

#        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))
#        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))
