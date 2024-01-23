import pygame


class Button:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.clicked = False

    def button_action(self, DISPLAYSCREEN, mouse):
        action = False
        pygame.draw.rect(DISPLAYSCREEN, "white", self.rect, 1)
        if self.rect.collidepoint(mouse):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            else:
                self.clicked = False
            return action

