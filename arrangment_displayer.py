"""arrangment_displayer, when ran, displays a setup for a single Gaia project playthrough"""

import pygame
from arrangement_generator import *

SECTORS_PATH = "assets/sprites/sectors/"
SECTORS_SIZE = (240, 260)
SECTORS_SECTION_SIZE = (920, 710)
SECTORS_COORDINATES = ((362, 26), (227, 210), (453, 236), (317, 420), (590, 52), (680, 262), (544, 446), (91, 394),
                       (0, 184), (136, 0))

ROUND_SCORING_TILES_PATH = "assets/sprites/round_scoring_tiles/"
ROUND_SCORING_TILES_SIZE = (105, 120)
ROUND_SCORING_TILES_SECTION_SIZE = (675, 160)
ROUND_SCORING_TILES_COORDINATES = ((12, 16), (122, 16), (232, 16), (342, 16), (452, 16), (562, 16))

FINAL_SCORING_TILES_PATH = "assets/sprites/final_scoring_tiles/"
FINAL_SCORING_TILES_SIZE = (120, 77)
FINAL_SCORING_TILES_SECTION_SIZE = (135, 160)
FINAL_SCORING_TILES_COORDINATES = ((7, 0), (7, 83))

ROUND_BOOSTERS_PATH = "assets/sprites/round_boosters/"
ROUND_BOOSTERS_SIZE = (84, 246)
ROUND_BOOSTERS_SECTION_SIZE = (650, 270)
ROUND_BOOSTERS_COORDINATES = ((0, 13), (95, 13), (188, 13), (283, 13), (375, 13), (471, 13), (564, 13))

RACE_PORTRAITS_PATH = "assets/sprites/race_portraits/"
RACE_PORTRAITS_SIZE = (139, 138)
RACE_PORTRAITS_SECTION_SIZE = (650, 260)
RACE_PORTRAITS_COORDINATES = ((22, 0), (179, 0), (336, 0), (493, 0), (100, 121), (257, 121), (415, 121))

FEDERATION_TOKENS_PATH = "assets/sprites/federation_tokens/"
FEDERATION_TOKENS_SIZE = (38, 46)
FEDERATION_TOKENS_SECTION_SIZE = (38, 46)
FEDERATION_TOKENS_COORDINATES = (0, 0)

ADVANCED_TECH_TILES_PATH = "assets/sprites/advanced_tech_tiles/"
ADVANCED_TECH_TILES_SIZE = (93, 74)
ADVANCED_TECH_TILES_SECTION_SIZE = (750, 120)
ADVANCED_TECH_TILES_COORDINATES = ((15, 31), (141, 31), (265, 31), (391, 31), (515, 31), (640, 31))

STANDARD_TECH_TILES_PATH = "assets/sprites/standard_tech_tiles/"
STANDARD_TECH_TILES_SIZE = (117, 88)
STANDARD_TECH_TILES_SECTION_SIZE = (750, 200)
STANDARD_TECH_TILES_COORDINATES = ((4, 2), (130, 2), (254, 2), (379, 2), (504, 2), (629, 2), (100, 116),
                                   (317, 116), (533, 116))


def load_sprites(path, size):
    loaded_sprites_surfaces = list()
    counter = 1

    while True:
        try:
            loaded_sprites_surfaces.append(
                pygame.transform.scale(
                    pygame.image.load("{}{}.png".format(path, counter)).convert_alpha(), size))
            counter += 1
        except pygame.error:
            if len(loaded_sprites_surfaces) > 0:
                break
            else:
                raise pygame.error

    return loaded_sprites_surfaces


def display_map_section(sectors_sequence=generate_map()):
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


def draw_section(all_tiles_surfaces, section_size, tiles_coordinates, chosen_tiles):
    section_surface = pygame.Surface(section_size, pygame.SRCALPHA, 32)

    for i in range(len(tiles_coordinates)):
        section_surface.blit(all_tiles_surfaces[chosen_tiles[i]-1], tiles_coordinates[i])

    return section_surface

def draw_setup():
    setup_sections_surfaces = list()

    setup_sections_surfaces.append(draw_section(load_sprites(ROUND_SCORING_TILES_PATH,
                                                             ROUND_SCORING_TILES_SIZE),
                                                ROUND_SCORING_TILES_SECTION_SIZE,
                                                ROUND_SCORING_TILES_COORDINATES,
                                                generate_round_scoring_tiles()))
    setup_sections_surfaces.append(draw_section(load_sprites(FINAL_SCORING_TILES_PATH,
                                                             FINAL_SCORING_TILES_SIZE),
                                                FINAL_SCORING_TILES_SECTION_SIZE,
                                                FINAL_SCORING_TILES_COORDINATES,
                                                generate_final_scoring_tiles()))
    setup_sections_surfaces.append(draw_section(load_sprites(ROUND_BOOSTERS_PATH,
                                                             ROUND_BOOSTERS_SIZE),
                                                ROUND_BOOSTERS_SECTION_SIZE,
                                                ROUND_BOOSTERS_COORDINATES,
                                                generate_round_boosters()))
    setup_sections_surfaces.append(draw_section(load_sprites(RACE_PORTRAITS_PATH,
                                                             RACE_PORTRAITS_SIZE),
                                                RACE_PORTRAITS_SECTION_SIZE,
                                                RACE_PORTRAITS_COORDINATES,
                                                generate_races()))
    setup_sections_surfaces.append(draw_section(load_sprites(ADVANCED_TECH_TILES_PATH,
                                                             ADVANCED_TECH_TILES_SIZE),
                                                ADVANCED_TECH_TILES_SECTION_SIZE,
                                                ADVANCED_TECH_TILES_COORDINATES,
                                                generate_advanced_tech_tiles()))
    setup_sections_surfaces.append(draw_section(load_sprites(STANDARD_TECH_TILES_PATH,
                                                             STANDARD_TECH_TILES_SIZE),
                                                STANDARD_TECH_TILES_SECTION_SIZE,
                                                STANDARD_TECH_TILES_COORDINATES,
                                                generate_standard_tech_tiles()))

    return setup_sections_surfaces

""""
pygame.init()
main_surface = pygame.display.set_mode((1600, 900))

loaded_sprites = load_sprites(FINAL_SCORING_TILES_PATH, FINAL_SCORING_TILES_SIZE)
print(loaded_sprites)

st_section = draw_section(loaded_sprites, FINAL_SCORING_TILES_SECTION_SIZE, FINAL_SCORING_TILES_COORDINATES, generate_final_scoring_tiles())
print(st_section)

main_surface.blit(st_section, (10, 10))

while True:
    pygame.display.update()
"""
