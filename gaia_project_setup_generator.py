import pygame
import arrangment_displayer
import arrangement_generator

SECTIONS_DISPLAY_COORDINATES = ((10, 730), (695, 730), (940, 10), (940, 290), (840, 560), (840, 690))
pygame.init()

main_surface = pygame.display.set_mode((1600, 900))
sections = arrangment_displayer.draw_setup()

main_surface.blit(pygame.image.load("assets/sprites/background.png"), (0, 0))

sectors_sequence = ((1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 0), (8, 1), (9, 2), (10, 3))
main_surface.blit(arrangment_displayer.display_map_section(sectors_sequence), (10, 10))

for i in range(len(SECTIONS_DISPLAY_COORDINATES)):
    main_surface.blit(sections[i], SECTIONS_DISPLAY_COORDINATES[i])

pygame.display.update()

do_exit = False

while not do_exit:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            do_exit = True
