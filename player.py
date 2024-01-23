import pygame
from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_c, K_g

class Player:
    def __init__(self, x, y, width, height, skin, speed, direction, hp):
        self.x = x
        self.y = y
        self.jump_vel = 1
        self.width = width
        self.height = height
        self.skin = skin
        self.img = pygame.image.load(skin + "_right.png")
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        self.direction = direction
        self.hp = hp
        self.invincibility = 0

    def get_x(self, x):
        return x
    
    def get_y(self, y):
        return y

    def get_hp(self, hp):
        return hp
    
    def update(self):
        self.invincibility -= 5
        keys = pygame.key.get_pressed()
        if keys[K_g]:
            self.skin = "gojo"
        if self.direction == "l":
            self.img = pygame.image.load(self.skin+"_left.png")
        if self.direction == "r":
            self.img = pygame.image.load(self.skin+"_right.png")
        if self.skin != "dude":
            self.hp = 99
            self.speed = 20
    
    def draw(self, DISPLAYSCREEN, camera):
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        player_draw_pos = camera.apply(self)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        DISPLAYSCREEN.blit(self.img, (player_draw_pos.x, player_draw_pos.y))
        return player_draw_pos
    
    def draw_stats(self, DISPLAYSCREEN, player_draw_pos, WIDTH, HEIGHT):
        hp_img = pygame.image.load("heart.png")
        hp_draw_pos = [player_draw_pos.x - (WIDTH//2) + 50, player_draw_pos.y - (HEIGHT//2) + 50]
        for i in range(self.hp):
            DISPLAYSCREEN.blit(hp_img, (hp_draw_pos[0], hp_draw_pos[1]))
            hp_draw_pos[0] = hp_draw_pos[0] + 80
    


    def movement(self, room_platforms):
        pressed = ""
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            pressed = "LEFT"
        if keys[K_RIGHT]:
            pressed = "RIGHT"
        if keys[K_UP] and self.on_plat(room_platforms):
            pressed = "UP"
        return pressed
    
    def shoot(self):
        keys = pygame.key.get_pressed()
        if keys[K_c]:
            return True
                
                 
    def plat_collision(self, room_platforms):
        for plat in room_platforms:
            if self.y > plat.y - self.height and self.y < plat.y + plat.height: 
                if self.x + self.width >= plat.x and self.x + self.width <= plat.x + plat.width:
                    self.x = self.x - self.speed
                if self.x <= plat.x + plat.width and self.x >= plat.x:
                    self.x = self.x + self.speed
            if  self.x + self.width > plat.x and self.x < plat.x + plat.width:
                if self.y >= plat.y and self.y <= plat.y + plat.height:
                    self.y = plat.y + plat.height + 5
                    self.jump_vel = 1
                if self.y + self.height >= plat.y and self.y + self.height <= plat.y + plat.height:
                    self.y = plat.y - self.height
                    self.jump_vel = 1

                
    def on_plat(self, room_platforms):
        for plat in room_platforms:
            if plat.x <= self.x + self.width and self.x <= plat.x + plat.width and self.y + self.height >= plat.y and self.y <= plat.y + plat.height:
                return True
        return False
    
    def recover(self, list_checkpoints, bullets):
        i = len(list_checkpoints)-1
        print(list_checkpoints)
        while i != -1:
            current_point = list_checkpoints[i]
            print(i)
            if current_point.active:
                self.x, self.y = current_point.x, current_point.y
                bullets = []
                return bullets 
            i -= 1   
        self.x, self.y = 100, 300

    def save_recovery(self, list_checkpoints):
        for i in range(len(list_checkpoints)):
            current_point = list_checkpoints[i]
            if current_point.x + current_point.width >= self.x >= current_point.x and current_point.y <= self.y + self.height <= current_point.y + current_point.height:
                if current_point.active == False:
                    current_point.active = True
                for point in list_checkpoints:
                    print(point)
                    if point.active == True:
                        print("is active")

                for point in list_checkpoints[0:i]:
                    point.active = False
                if i < len(list_checkpoints) - 1:
                    for point in list_checkpoints[i+1:]:
                        point.active = False
                return

    def gravity(self):
        self.y += self.jump_vel
        self.jump_vel += 0.75

    def take_damage(self):
        self.hp -= 1
        self.invincibility = 100
        
    def voidfall(self, list_checkpoints, bullets):
        fallen = False
        if self.y > 1500:
            self.jump_vel = 3
            self.hp -= 1
            fallen = True
        return fallen
    
    def check_death(self):
        if self.hp <= 0:
            return True
        return False
