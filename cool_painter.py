import pygame, time

MOUSE_UP = 1026
MOUSE_DOWN = 1025
MOUSE_MOVE = 1024


pygame.init()
pygame.display.set_caption('drawerzzz')
window = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
pygame.display.update()
draw = False

def draw_line(start_pos, end_pos):
    mirror_start_pos = (start_pos[0], 600 - start_pos[1])
    mirror_end_pos = (end_pos[0], 600 - end_pos[1])
    pygame.draw.line(window, (239, 210, 68), start_pos, end_pos)
    pygame.draw.line(window, (239, 210, 68), mirror_start_pos, mirror_end_pos)
    pygame.draw.line(window, (239, 210, 68), start_pos, mirror_start_pos)
    pygame.draw.line(window, (239, 210, 68), end_pos, mirror_end_pos)


while running:
    clock.tick(10)
    fst_point = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if fst_point[1] <= 300: 
            if not draw and event.type == MOUSE_DOWN:
                draw = True
            elif draw and event.type == MOUSE_DOWN:
                draw = False
        elif fst_point[1] > 300:
            draw = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            window.fill((0,0,0))
    if draw:
        time.sleep(0.003)
        snd_point = pygame.mouse.get_pos()
        if snd_point[1] < 300: 
            draw_line(fst_point, snd_point)
        print("fst = " + str(fst_point))
        print("snd = " + str(snd_point))


    pygame.display.update()