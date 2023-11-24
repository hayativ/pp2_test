import pygame
import os

pygame.init()
pygame.mixer.init()

W, H = 800, 600
sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("MP3 player")

music_dir = r'C:\Users\Yeva\Desktop\python\lab9\music'

musics = [f for f in os.listdir(music_dir)]

current_music = 0

pygame.mixer.music.load(os.path.join(music_dir, musics[current_music]))

def play():
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def next():
    global current_music
    current_music = (current_music + 1) % len(musics)
    pygame.mixer.music.load(os.path.join(music_dir, musics[current_music]))
    play()

def prev():
    global current_music
    current_music = (current_music - 1) % len(musics)
    pygame.mixer.music.load(os.path.join(music_dir, musics[current_music]))
    play()

while True:
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                play()
            elif event.key == pygame.K_DOWN:
                stop()
            elif event.key == pygame.K_RIGHT:
                next()
            elif event.key == pygame.K_LEFT:
                prev()
