"""arrangment_displayer, when ran, displays a setup for a single Gaia project playthrough"""

import pygame
from arrangement_generator import *

SECTORS_PATH = "assets/sprites/sectors/"
SECTORS_SIZE = (240, 260)
SECTORS_COORDINATES = ((362, 26), (227, 210), (453, 236), (317, 420), (590, 52), (680, 262), (544, 446), (91, 394), (0, 184), (136, 0))


def display_map_section(sectors_sequence):
    map_section = pygame.Surface((920, 710), pygame.SRCALPHA, 32)
    sectors_surfaces = list()

    print("{}{}.png".format(SECTORS_PATH, 0+1))

    for i in range(10):
        sectors_surfaces.append(pygame.image.load("{}{}.png".format(SECTORS_PATH, i+1)).convert_alpha())
        sectors_surfaces[i] = pygame.transform.scale(sectors_surfaces[i], SECTORS_SIZE)
        sectors_surfaces[i] = pygame.transform.rotate(sectors_surfaces[i], sectors_sequence[i][1]*60)

    for i in range(10):
        #map_section.blit(sectors_surfaces[sectors_sequence[i][0] - 1], SECTORS_COORDINATES[i])

        if sectors_sequence[i][1] == 0 or sectors_sequence[i][1] == 3:
            print("case1, {}", sectors_sequence[i])
            map_section.blit(sectors_surfaces[sectors_sequence[i][0] - 1], SECTORS_COORDINATES[i])
        else:
            print("case2, {}", sectors_sequence[i])
            map_section.blit(sectors_surfaces[sectors_sequence[i][0] - 1],
                             (SECTORS_COORDINATES[i][0] - 53, SECTORS_COORDINATES[i][1] - 39))
    return map_section