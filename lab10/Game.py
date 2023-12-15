#importing pygame and it's moduls
#importing sys 
import pygame, sys
from pygame.locals import *
import random, time

#initialzing the pygame engine
pygame.init()

#setting up FPS as 60 
FPS = 60
#using tick() for working with an object of pygame.time.Clock class
FramePerSec = pygame.time.Clock()
#RGB system of colors (Red, Green, Blue)
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#creating variables for using in this program
#screen size
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
#speed and score of enemy car
SPEED = 5
SCORE = 0
#speed and score of coins
SPEED_COINS = 5
SCORE_COINS = 0

#setting up two fonts with sizeand font family
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
#Game Over title for the end of game
game_over = font.render("Game Over", True, BLACK)

#downloanding image for background
background = pygame.image.load("AnimatedStreet.png")

#creating a white screen with size and title "Game"
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

#creating Enemy class
#pygame.sprite.Sprite makes the Enemy class it’s child class
class Enemy(pygame.sprite.Sprite):
      #function __init__() to assign values to object properties and other operations
      def __init__(self):
        #super() function to make the child class inherit
        #all the methods and properties from its parent
        super().__init__() 
        #downloanding image of enemy car
        self.image = pygame.image.load("Enemy.png")
        #creating a rectangle of the same size as the image
        self.rect = self.image.get_rect()
        #defining a starting position for the rect randomly but with boundaries
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
      #creating method move to control the movement of the enemy car
      def move(self):
        #making SCORE variable global for using it later outside this function
        global SCORE
        #moving the Enemy object down by Speed
        self.rect.move_ip(0,SPEED)
        #checking to see if the top of the Enemy has reached the end of the screen
        #checking if there was no collision between enemy's and player's cars
        if (self.rect.bottom > 600):
            #counter for enemy cars increses by 1
            SCORE += 1
            #resetting coin it back to the top of screen
            #and at a random location on the X axis
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

#creating Player class
#pygame.sprite.Sprite makes the Player class it’s child class
class Player(pygame.sprite.Sprite):
    #function __init__() to assign values to object properties and other operations
    def __init__(self):
        #super() function to make the child class inherit
        #all the methods and properties from its parent
        super().__init__() 
        #downloanding image of player car
        self.image = pygame.image.load("Player.png")
        #creating a rectangle of the same size as the image
        self.rect = self.image.get_rect()
        #defining a starting position for the rect
        self.rect.center = (160, 520)
    #creating method move to control the movement of the player
    def move(self):
        #checking if any keys are pressed down or not
        pressed_keys = pygame.key.get_pressed()
        #if player isn’t able to move off screen
        if self.rect.left > 0:
              #if left key was pressed - move rect by 5 to the left 
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        #if player isn’t able to move off screen
        if self.rect.right < SCREEN_WIDTH:    
              #if right key was pressed - move rect by 5 to the right     
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

#creating Coin class
#pygame.sprite.Sprite makes the Coin class it’s child class
class Coin(pygame.sprite.Sprite):
      #function __init__() to assign values to object properties and other operations
      def __init__(self):
        #super() function to make the child class inherit
        #all the methods and properties from its parent
        super().__init__() 
        #downloanding image of coin
        self.image = pygame.image.load("coin.png")
        #creating a rectangle of the same size as the image
        self.rect = self.image.get_rect()
        #defining a starting position for the rect randomly but with boundaries
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
      #creating method move to control the movement of the coin
      def move(self):
        #making SCORE_COINS variable global for using it later outside this function
        global SCORE_COINS
        #moving the Coin object down by Speed
        self.rect.move_ip(0,SPEED)
        #if coordinates of coin's rect and player car's rect have collision or not
        if self.rect.colliderect(P1.rect) or self.rect.bottom > 600:
            #checking if they have
            if self.rect.colliderect(P1.rect):
                #counter for coins increses by 1
                SCORE_COINS += 1
                #playing sound for getting coin
                pygame.mixer.Sound('coin.mp3').play()
            #resetting coin it back to the top of screen
            #and at a random location on the X axis
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

#setting up sprites: player, enemy and coin
P1 = Player()
E1 = Enemy()
C1 = Coin()

#creating groups for sprites
#adding all enemy's cars in enemies group
enemies = pygame.sprite.Group()
enemies.add(E1)
#adding all coins cars in coins group
coins = pygame.sprite.Group()
coins.add(C1)
#adding all enemies, coins and player in all_sprites group
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

#creating custom event called INC_SPEED
INC_SPEED = pygame.USEREVENT + 1
#set_timer() function to call the INC_SPEED 
#event object every 1000 milliseconds, or 1 second
pygame.time.set_timer(INC_SPEED, 1000)

#quitting the game loop
while True:
    #cycling through all events occur
    for event in pygame.event.get():
        #increasing speed by each round
        if event.type == INC_SPEED:
              SPEED += 0.5      
        #determining whether the game was to be closed or not by QUIT signal
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #creating counter for scores of enemy cars in the upper left corner
    #using blit() method for drawing background as surface and rectangle as object
    DISPLAYSURF.blit(background, (0,0))
    #setting up font and color
    scores = font_small.render(str(SCORE), True, BLACK)
    #using blit() method for drawing scores as surface and rectangle as object
    DISPLAYSURF.blit(scores, (10,10))

    #creating counter for coins that were collected in the upper right corner
    #using blit() method for drawing background as surface and rectangle as object
    DISPLAYSURF.blit(background, (SCREEN_WIDTH,0))
    #setting up font and color
    scores = font_small.render(str(SCORE_COINS), True, BLACK)
    #using blit() method for drawing scores as surface and rectangle as object
    DISPLAYSURF.blit(scores, (SCREEN_WIDTH - 20,10))

    #moving and re-drawing all sprites
    for entity in all_sprites:
        entity.move()
        #using blit() method for drawing image as surface and rectangle as object
        DISPLAYSURF.blit(entity.image, entity.rect)
        
    #if collision occurs between player's and enemy's cars
    if pygame.sprite.spritecollideany(P1, enemies):
          #playing sound for crash
          pygame.mixer.Sound('crash.wav').play()
          #freezing the game to make crash understandable 
          time.sleep(0.5)
          #filling screen by red
          DISPLAYSURF.fill(RED)
          #using blit() method for drawing title as surface and rectangle as object
          DISPLAYSURF.blit(game_over, (30,250))
          #udpating the screen
          pygame.display.update()
          #clearing all sprites
          for entity in all_sprites:
                entity.kill() 
          #freezing the game to make the end of the game understandable 
          time.sleep(2)
          #calling pygame.quit and sys.exit to close 
          #the pygame window and the python script respectively
          pygame.quit()
          sys.exit()        
    
    #udpating the screen
    pygame.display.update()
    #maling sure udpating repeats only 60 times per second
    FramePerSec.tick(FPS)
