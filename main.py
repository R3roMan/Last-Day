# Max's TO DO LIST: Add spikes, add jump orb, make smaller character sprite, fix collision detection, improve jumping, fix camera edges to room, fix background

import pygame, sys
from pygame import QUIT, K_UP, K_DOWN, K_LEFT, K_RIGHT

import button
import player
import platforms
import camera
import background
import rooms
import bullet
import enemy
import recoverypoint

white = "#FFFFFF"
black = "#000000"

WIDTH, HEIGHT = 1200, 750

z1 = enemy.Enemy("Zombie", 500, 300, 199, 251, "f", "m", 3, 200, "zombie.png")
#zombie2 =
#zombie3 = 
#zombie4 = 
#zombie5 =
list_enemies = []

room1 = rooms.Rooms(("""                                         
[                                            ]
[                                      #  0   
[                          # #       #        
[                       #       #  #      ####
[             #      #      #     #          ]
[      0     #   #  #                        ]
[        #                                   ]
==========  ================================"""), 4500, 900, True, True) #rework
room2 = rooms.Rooms("""                       
[            0                 ]       
[                              ]                    
             #                 ]
          #                    ]
[ #    #                       ]
[ ###         ####  ####       ]
[                              ]""", 4000, 900, False, False)
room_list = [room1, room2]


def load_menu(DISPLAYSCREEN):
    menu = pygame.image.load("MENUSCREEN.png")
    menu = pygame.transform.scale(menu, (WIDTH, HEIGHT))
    DISPLAYSCREEN.blit(menu, (0, 0))

def game_over(DISPLAYSCREEN):
    clock= pygame.time.Clock()
    run = True
    while run:
        DISPLAYSCREEN.fill((0, 0, 0))

        pygame.display.update()
        clock.tick(60)

def bullet_check(bullets, bullet_draw_pos, bullet_direction, bob):
    reloaded = True
    if len(bullets) >= 1:
        reloaded = False
        if bullet_direction == "RIGHT":
            if bullets[len(bullets)-1].x > bullets[len(bullets)-2].x + 300:
                reloaded = True
        if bullet_direction == "LEFT":
            if bullets[len(bullets)-1].x < bullets[len(bullets)-2].x - 300:
                reloaded = True
      #  if bullet_direction == "UP":
       #     if bullets[len(bullets)-1].x > bob.y + bob.height - 300:
        #        reloade = True
    return reloaded

def make_room(DISPLAYSCREEN, list_platforms, list_checkpoints):
    coin = pygame.image.load("coin.jpg")
    for room in room_list:
        room_index = room_list.index(room)
        if room.state == True:
            cl_room = room_list[room_index]
            for i in cl_room.design:
                if i == " ":
                    room.x = room.x + 100
                if i == "\n":
                    room.x = 0
                    room.y = room.y + 100
                if i == "#":
                    platform = platforms.Plat("floating", room.x, room.y, 100, 50)
                    list_platforms.append(platform)
                    room.x += 100
                if i == "[" or i == "]":
                    platform = platforms.Plat("wall", room.x, room.y, 50, 100)
                    list_platforms.append(platform)
                    room.x += 50
                if i == "=":
                    platform = platforms.Plat("ground", room.x, room.y, 200, 200)
                    list_platforms.append(platform)
                    room.x += 200
                if i == "0":
                    rec_point = recoverypoint.Recpoint(room.x, room.y, False)
                    list_checkpoints.append(rec_point)
                    room.x += 50
                if i == "x": #for spikes
                    DISPLAYSCREEN.blit(coin, ((room.x, room.y)))
            return list_platforms


def make_platforms(DISPLAYSCREEN, list_platforms, camera_obj):

    for platform in list_platforms:
        platform.draw(DISPLAYSCREEN, camera_obj)
        
#def make_enemies(DISPLAYSCREEN, camera_obj):
#    for enemy in enemy_list:
#        enemy_list = room_list.index(enemy)
#        if enemy.state == True

def switch_room(bob):
    switched = False
    for room in room_list: 
        if room.state == True:
            next_room_index = room_list.index(room) + 1
            prev_room_index = room_list.index(room) - 1
            if next_room_index < len(room_list):
                if bob.x > room.width:
                    room.state = False
                    if room.checked == False:
                        room.checked = True
                    room_list[next_room_index].state = True
                    bob.x = 100
                    switched = True
                    return switched
            if len(room_list) > 1:
                if bob.x < 0:
                    room.state = False
                    if room.checked == False:
                        room.checked = True
                    room_list[prev_room_index].state = True
                    bob.x = room_list[prev_room_index].width - 100
                    switched = True
                    return switched
    return switched

def menu(DISPLAYSCREEN):
    pygame.display.set_caption("day_zero")
    begin_button = button.Button(460, 410, 250, 90)
    quit_button = button.Button(440, 650, 300, 65)
    clock= pygame.time.Clock()
    run = True

    while run:
        pygame.event.pump()
        DISPLAYSCREEN.fill((0, 0, 0))
        load_menu(DISPLAYSCREEN)
        mouse = pygame.mouse.get_pos()
        if begin_button.button_action(DISPLAYSCREEN, mouse):
            run = False
            gamestate = "GAMEPLAY"
        if quit_button.button_action(DISPLAYSCREEN, mouse):
            run = False
            gamestate = "QUIT"
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                run = False
                gamestate = "QUIT"
        pygame.display.update()
        clock.tick(60)
    return gamestate


#72, 108
def game_play(DISPLAYSCREEN):
    pygame.display.set_caption("level_1")
    pygame.mixer.init()
    clock = pygame.time.Clock()
    b1 = background.Background(0, 0, WIDTH, HEIGHT)
    bob = player.Player(300, 300, 72, 108, "dude", 8, "r", 3) #define  player
    camera_obj = camera.Camera(WIDTH, HEIGHT)
    list_platforms = []
    list_checkpoints = []
    b1.tiles_amount()
    bullets = []
    bullet_direction = "RIGHT"
    switched = True
    music = False

    run = True
    while run:
        pygame.display.update()
        DISPLAYSCREEN.fill((0, 0, 0))

        if switched == True:
            list_platforms = []
            list_checkpoints = []
            print("yuh uh")
            list_platforms = make_room(DISPLAYSCREEN, list_platforms, list_checkpoints)


        #switch rooms
        switched = switch_room(bob)

        #draw background
        b1.draw_background(DISPLAYSCREEN, camera_obj, bob)

        #draw camera
        camera_obj.update(DISPLAYSCREEN, bob, WIDTH, HEIGHT)

        #draw platforms 
        plat_index = make_platforms(DISPLAYSCREEN, list_platforms, camera_obj)

        #draw character
        bullet_draw_pos = bob.draw(DISPLAYSCREEN, camera_obj) #draw player

        bob.draw_stats(DISPLAYSCREEN, bullet_draw_pos, WIDTH, HEIGHT)

        bob.save_recovery(list_checkpoints)
        for point in list_checkpoints:
            point.update(DISPLAYSCREEN, camera_obj)
        #make_enemies(DISPLAYSCREEN, camera_obj)
        
        if bob.skin != "dude" and music == False:
            pygame.mixer.music.load(bob.skin+"_song.mp3")
            pygame.mixer.music.play(-1)
            music = True

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                run = False

        on_plat = bob.on_plat(list_platforms)
        if not on_plat:
            bob.gravity()

        pressed = bob.movement(list_platforms)
        if pressed == "LEFT":
            bob.direction = "l"
            bob.x -= bob.speed
            for bullet_obj in bullets:
                bullet_obj.x += bob.speed - 5
        if pressed == "RIGHT":
            bob.direction = "r"
            bob.x += bob.speed
            for bullet_obj in bullets:
                bullet_obj.x -= bob.speed - 5
        if pressed == "UP":
            bob.y -= 2
            bob.jump_vel -= 15
    
        if pressed != "" and pressed != "UP":
            bullet_direction = pressed

        if bob.shoot():
            reloaded = bullet_check(bullets, bullet_draw_pos, bullet_direction, bob)
            if reloaded == True:
                if bullet_direction == "RIGHT":
                    new_bullet = bullet.Bullet(bullet_draw_pos.x + bob.width, bob.y + bob.height // 2, 100, 30, bob.speed*3, bullet_direction, bob.skin)
                    bob.x -= bob.speed
                    bullets.append(new_bullet)
                if bullet_direction == "LEFT":
                    new_bullet = bullet.Bullet(bullet_draw_pos.x, bob.y + bob.height // 2, 100, 30, bob.speed*3, bullet_direction, bob.skin)
                    bob.x += bob.speed
                    bullets.append(new_bullet)

        for bullet_obj in bullets:
            bullet_obj.update(DISPLAYSCREEN, bob, camera_obj)
            if bullet_obj.destroy(bob, bullet_draw_pos):
                bullets.remove(bullet_obj)
        

        bob.plat_collision(list_platforms)
        fallen = bob.voidfall(list_checkpoints, bullets)
        if fallen == True:
            bullets = bob.recover(list_checkpoints, bullets)

        if bob.check_death():
            gamestate = "GAMEOVER"
            run = False
        
        bob.update()
            
        pygame.display.update()
        clock.tick(60)

    return gamestate

def main():
    pygame.init()
    DISPLAYSCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    gamestate = "MENU"
    while gamestate != "QUIT":
        if gamestate == "MENU":
            gamestate = menu(DISPLAYSCREEN)
        elif gamestate == "GAMEPLAY":
            gamestate = game_play(DISPLAYSCREEN)
        elif gamestate == "GAMEOVER":
            gamestate = game_over(DISPLAYSCREEN)
    pygame.quit()
    sys.exit()

    
if __name__ == "__main__":
    main()

#medium.com for buttons
