import math

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
screen.convert_alpha()

start = pygame.time.get_ticks()

looping = True

while looping:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            looping = False

    # Draw a rectangle

    new_time = pygame.time.get_ticks() - start

    #surface = pygame.Surface(screen.get_size()).convert_alpha()

    surface = screen.copy().convert_alpha()

    surface.fill((0, 0, 0, 1))

    #screen.fill((0, 0, 0, 1))

    # pygame.draw.rect(surface,
    #                  (0, 0, 0, 100),
    #                  pygame.Rect(0, 0, surface.get_width(), surface.get_height())
    #                  )

    r = 200 + 20 * math.cos(new_time / 400)

    xpos = screen.get_width() / 2 + r * math.cos(new_time / 1000)
    ypos = screen.get_height() / 2 + r * math.sin(new_time / 1000)

    radius = 60 + 20 * math.sin(new_time / 200)

    h = 180 + 180  * math.sin(new_time / 1000)
    s = 50 + 50 * math.sin(new_time / 2000 + math.pi / 2)

    mycolor = pygame.Color(0, 0, 0)
    mycolor.hsva = (h, s, 100, 1)

    pygame.draw.circle(surface=surface,
                       color=mycolor,
                       center=(xpos, ypos),
                       radius=radius,
                       width=0
                       )

    screen.blit(surface, (0, 0))

    # Update display

    pygame.display.flip()
