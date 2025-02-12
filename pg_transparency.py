import math

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

start = pygame.time.get_ticks()

looping = True

while looping:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            looping = False

    # Clear screen

    screen.fill((0, 0, 0))

    # Draw a rectangle

    new_time = pygame.time.get_ticks() - start

    xpos = screen.get_width() / 2 + 200 * math.cos(new_time / 1000)
    ypos = screen.get_height() / 2 + 200 * math.sin(new_time / 1000)

    radius = 60 + 20 * math.sin(new_time / 200)

    pygame.draw.circle(surface=screen,
                       color=(255,255,255),
                       center=(xpos,ypos),
                       radius=radius
                       )

    # Update display

    pygame.display.flip()
