import pygame
from datetime import datetime
pygame.init()

W, H = 800, 600

sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("Mickey Mouse clock")

WHITE = (255, 255, 255)

mickey = pygame.image.load("main-clock.png")
left_hand = pygame.image.load("left-hand.png")
right_hand = pygame.image.load("right-hand.png")

mickey = pygame.transform.scale(mickey, (mickey.get_width() // 2.7, mickey.get_height() // 2.7))
right_hand = pygame.transform.scale(right_hand, (right_hand.get_width() // 1.2, right_hand.get_height() // 1.5))
left_hand = pygame.transform.scale(left_hand, (left_hand.get_width() // 1.2, left_hand.get_height() // 1.5))

angle_sec = 0
angle_min = 0
clock = pygame.time.Clock()
FPS = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    t = datetime.now()
    angle_sec = -6 * t.second
    angle_min = -6 * t.minute
    sc.fill(WHITE)

    left_hand_surf = pygame.transform.rotate(left_hand, angle_sec)
    right_hand_surf = pygame.transform.rotate(right_hand, angle_min)

    mickey_rect = mickey.get_rect(center=(W // 2, H // 2))
    left_hand_rect = left_hand_surf.get_rect(center=(W // 2, H // 2))
    right_hand_rect = right_hand_surf.get_rect(center=(W // 2, H // 2))

    sc.blit(mickey, mickey_rect)
    sc.blit(left_hand_surf, left_hand_rect)
    sc.blit(right_hand_surf, right_hand_rect)

    pygame.display.update()

    clock.tick(FPS)