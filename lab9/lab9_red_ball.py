import pygame
pygame.init()

W, H = 600, 400
sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("Red Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

radius = 25
x = W // 2
y = H // 2

clock = pygame.time.Clock()
FPS = 20
speed = 20
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x - speed > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x + speed < W:
        x += speed
    if keys[pygame.K_UP] and y - speed > 0:
        y -= speed
    if keys[pygame.K_DOWN] and y + speed < H:
        y += speed

    sc.fill(WHITE)
    pygame.draw.circle(sc, RED, (x, y), radius)
    pygame.display.update()
    clock.tick(FPS)