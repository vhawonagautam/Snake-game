# Example file showing a circle moving on screen
import pygame 
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 750))
clock = pygame.time.Clock()
running = True
dt = 0
speed = 400
player_pos = pygame.Vector2(10,10)
direction = (speed,0)

food = (random.randint(0, 1280),random.randint(0, 750))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    
    pygame.draw.rect(screen, "yellow",(player_pos.x ,player_pos.y ,20,20))
    
    # player_pos +=  direction
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        direction = (0, -speed)
    elif keys[pygame.K_DOWN]:
        direction = (0, speed)
    elif keys[pygame.K_LEFT]:
        direction = (-speed, 0)
    elif keys[pygame.K_RIGHT]:
        direction = (speed, 0)
        

    # player_pos += direction *dt
    player_pos.x += direction[0]*dt
    player_pos.y += direction[1]*dt
   
   
    
    player_pos.x = max(0, min(player_pos.x, 1280 - 20))
    player_pos.y = max(0, min(player_pos.y, 750 - 20))
    
    
    pygame.draw.rect(screen, "brown", (*food, 20, 20))
    player_rect = pygame.Rect(player_pos.x, player_pos.y, 20, 20)
    food_rect = pygame.Rect(food[0], food[1], 20, 20)


    if player_rect.colliderect(food_rect):
     print("Collision detected!")
    
    pygame.display.flip()
    
    
    
    # # flip() the display to put your work on screen
    # pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()