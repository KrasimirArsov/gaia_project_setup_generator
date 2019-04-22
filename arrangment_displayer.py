"""arrangment_displayer, when ran, displays a setup for a single Gaia project playthrough"""

import pygame
from arrangement_generator import *

SECTORS_PATH = "assets/sprites/sectors/"
SECTORS_SIZE = (240, 260)
SECTORS_COORDINATES = ((362, 26), (227, 210), (453, 236), (317, 420), (590, 52), (680, 262), (544, 446), (91, 394),
                       (0, 184), (136, 0))

ROUND_SCORING_TILES_PATH = "assets/sprites/round_scoring_tiles/"
ROUND_SCORING_TILES_SIZE = (105, 120)
ROUND_SCORING_TILES_COORDINATES = ((12, 16), (122, 16), (232, 16), (342, 16), (452, 16), (562, 16))

FINAL_SCORING_TILES_PATH = "assets/sprites/final_scoring_tiles/"
FINAL_SCORING_TILES_SIZE = (120, 77)
FINAL_SCORING_TILES_COORDINATES = ((684, 0), (684, 82))

ROUND_BOOSTERS_PATH = "assets/sprites/round_boosters/"
ROUND_BOOSTERS_SIZE = (84, 246)
ROUND_BOOSTERS_COORDINATES = ((0, 13), (95, 13), (188, 13), (283, 13), (375, 13), (471, 13), (564, 13))

RACE_PORTRAITS_PATH = "assets/sprites/race_portraits/"
RACE_PORTRAITS_SIZE = (139, 138)
RACE_PORTRAITS_COORDINATES = ((22, 0), (179, 0), (336, 0), (493, 0), (100, 121), (257, 121), (415, 121))

STANDARD_TECH_TILES_PATH = "assets/sprites/standard_tech_tiles/"
STANDARD_TECH_TILES_SIZE = (117, 88)
STANDARD_TECH_TILES_COORDINATES = ((4, 135), (130, 135), (254, 135), (379, 135), (504, 135), (629, 135), (100, 242),
                                   (317, 242), (533, 242))

ADVANCED_TECH_TILES_PATH = "assets/sprites/advanced_tech_tiles/"
ADVANCED_TECH_TILES_SIZE = (93, 74)
ADVANCED_TECH_TILES_COORDINATES = ((15, 31), (141, 31), (265, 31), (391, 31), (515, 31), (640, 31))

FEDERATION_TOKENS_PATH = "assets/sprites/federation_tokens/"
FEDERATION_TOKENS_SIZE = (38, 46)
FEDERATION_TOKENS_COORDINATES = (0, 0)


def generate_the_map_section_surface(sectors_sequence):
    map_surface = pygame.Surface((920, 710), pygame.SRCALPHA, 32)
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
            map_surface.blit(sectors_surfaces[sectors_sequence[i][0] - 1], SECTORS_COORDINATES[i])
        else:
            print("case2, {}", sectors_sequence[i])
            map_surface.blit(sectors_surfaces[sectors_sequence[i][0] - 1],
                             (SECTORS_COORDINATES[i][0] - 53, SECTORS_COORDINATES[i][1] - 39))
    return map_surface


def generate_the_scoring_tiles_surface(sectors_sequence):
    scoring_tiles_surface = pygame.Surface((920, 710), pygame.SRCALPHA, 32)
    sectors_surfaces = list()

    return scoring_tiles_surface