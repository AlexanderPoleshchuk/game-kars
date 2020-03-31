import pygame



pygame.init()
win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Карась - игра началась!")


walk_right = [pygame.image.load('static/pygame_right_1.png'), pygame.image.load('static/pygame_right_2.png'),
              pygame.image.load('static/pygame_right_3.png'), pygame.image.load('static/pygame_right_4.png'),
              pygame.image.load('static/pygame_right_5.png'), pygame.image.load('static/pygame_right_6.png')]

walk_left = [pygame.image.load('static/pygame_left_1.png'), pygame.image.load('static/pygame_left_2.png'),
              pygame.image.load('static/pygame_left_3.png'), pygame.image.load('static/pygame_left_4.png'),
              pygame.image.load('static/pygame_left_5.png'), pygame.image.load('static/pygame_left_6.png')]

bg = pygame.image.load('static/pygame_bg.jpg')
player_stand = pygame.image.load('static/pygame1.png')

clock = pygame.time.Clock()

x = 50
y = 425
width = 60
height = 71
speed = 5

isJump = False
jumpCount = 10

left = False
right = False
anim_count = 0


def draw_window():
    global anim_count
    win.blit(bg, (0, 0))
    if anim_count + 1 >= 30:
        anim_count = 0
    if left:
        win.blit(walk_left[anim_count // 5], (x,y))
        anim_count += 1
    elif right:
        win.blit(walk_right[anim_count // 5], (x,y))
        anim_count += 1
    else:
        win.blit(player_stand, (x, y))
    pygame.display.update()

run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - 5:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        anim_count = 0
    if not(isJump):
        if keys[pygame.K_UP]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    draw_window()



pygame.quit()

