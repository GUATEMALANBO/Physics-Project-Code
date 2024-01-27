import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 600, 400
CAR_RADIUS = 40
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bumper Cars")

# background image
background_image = pygame.image.load("road background2.jpg")  
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# bumper car images
blue_car_image = pygame.image.load("Knight bumper car.png")
red_car_image = pygame.image.load("Red Knight bumper car.png")

blue_car_image = pygame.transform.scale(blue_car_image, (CAR_RADIUS * 2, CAR_RADIUS * 2))
red_car_image = pygame.transform.scale(red_car_image, (CAR_RADIUS * 2, CAR_RADIUS * 2))

collision_sound = pygame.mixer.Sound("Metal hit sound Effect.mp3")

# Car properties
blue_car_x = WIDTH // 4
blue_car_y = HEIGHT // 2
blue_car_speed_x = 5
blue_car_speed_y = 5

red_car_x = WIDTH // 1.5
red_car_y = HEIGHT // 2
red_car_speed_x = -1
red_car_speed_y = -1

pygame.mixer.init()

# Load music
pygame.mixer.music.load("Undertale Soundtrack.mp3") 
pygame.mixer.music.set_volume(0.3)  

# Play the music on loop
pygame.mixer.music.play(-1)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    blue_car_x += blue_car_speed_x
    blue_car_y += blue_car_speed_y

    red_car_x += red_car_speed_x
    red_car_y += red_car_speed_y

    # Bounce off the walls for blue car
    if blue_car_x - CAR_RADIUS < 0 or blue_car_x + CAR_RADIUS > WIDTH:
        blue_car_speed_x = -blue_car_speed_x

    if blue_car_y - CAR_RADIUS < 0 or blue_car_y + CAR_RADIUS > HEIGHT:
        blue_car_speed_y = -blue_car_speed_y

    # Bounce off the walls for red car
    if red_car_x - CAR_RADIUS < 0 or red_car_x + CAR_RADIUS > WIDTH:
        red_car_speed_x = -red_car_speed_x

    if red_car_y - CAR_RADIUS < 0 or red_car_y + CAR_RADIUS > HEIGHT:
        red_car_speed_y = -red_car_speed_y

    # collision between cars
    distance = math.sqrt((blue_car_x - red_car_x)**2 + (blue_car_y - red_car_y)**2)
    if distance < 2 * CAR_RADIUS:
        blue_car_speed_x, red_car_speed_x = red_car_speed_x, blue_car_speed_x
        blue_car_speed_y, red_car_speed_y = red_car_speed_y, blue_car_speed_y
        
        # Play collision sound
        collision_sound.play()

    # Draw the background
    screen.blit(background_image, (0, 0))

    # Draw blue bumper car
    if blue_car_speed_x < 0:
        blue_car_image_flipped = pygame.transform.flip(blue_car_image, True, False)
        screen.blit(blue_car_image_flipped, (int(blue_car_x - CAR_RADIUS), int(blue_car_y - CAR_RADIUS)))
    else:
        screen.blit(blue_car_image, (int(blue_car_x - CAR_RADIUS), int(blue_car_y - CAR_RADIUS)))

    # Draw red bumper car
    if red_car_speed_x < 0:
        red_car_image_flipped = pygame.transform.flip(red_car_image, True, False)
        screen.blit(red_car_image_flipped, (int(red_car_x - CAR_RADIUS), int(red_car_y - CAR_RADIUS)))
    else:
        screen.blit(red_car_image, (int(red_car_x - CAR_RADIUS), int(red_car_y - CAR_RADIUS)))

    pygame.display.flip()

    pygame.time.Clock().tick(FPS)