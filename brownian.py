import pygame
import random
import sys
import numpy as np

def random_rotation():
    angle = random.uniform(0, 360)
    print(angle)
    return round(np.cos(np.deg2rad(angle)),2) , round(np.sin(np.deg2rad(angle)) ,2)
# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Dot")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Rectangle parameters
rect_width, rect_height = 300, 200
rect_x, rect_y = (WIDTH - rect_width) // 2, (HEIGHT - rect_height) // 2

# Dot parameters
dot_radius = 10
dot_x, dot_y = rect_x + rect_width//2, rect_y + rect_height//2
dot_speed = 2
dx, dy = 1, 0 # Initial direction of movement

clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the dot
    dot_x += dx * dot_speed
    dot_y += dy * dot_speed
    if dot_x < rect_x + dot_radius: 
        dot_x = rect_x + dot_radius
    elif dot_x > rect_x + rect_width - dot_radius:
        dot_x = rect_x + rect_width - dot_radius

    if dot_y < rect_y + dot_radius: 
        dot_y = rect_y + dot_radius
    elif dot_y > rect_y + rect_height - dot_radius:
        dot_y = rect_y + rect_height - dot_radius

    # Check for collision with walls
    if dot_x <= rect_x + dot_radius or dot_x >= rect_x + rect_width - dot_radius:
        dx, dy = random_rotation()
        print("-",dx, dy)
        

    if dot_y <= rect_y + dot_radius or dot_y >= rect_y + rect_height - dot_radius:
        dx, dy = random_rotation()
        print("-",dx, dy)


    # Fill the screen with background color
    screen.fill(WHITE)

    # Draw the rectangle
    pygame.draw.rect(screen, BLACK, (rect_x, rect_y, rect_width, rect_height))

    # Draw the dot
    pygame.draw.circle(screen, RED, (int(dot_x), int(dot_y)), dot_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(100)

# Quit Pygame
pygame.quit()
sys.exit()
