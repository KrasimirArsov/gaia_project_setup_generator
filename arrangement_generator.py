"""The arrangement_generator generates a setup for a Gaia project game in the form of tuples"""

import random

setted_seed=0

def set_seed(seed):
    setted_seed = seed


def generate_map(number_of_players=4, seed=setted_seed):
    """This function returns a tuple of tuples that represents the arrangement of the sectors

    ((s,r), (s, r)...)
    The tuple is either 10 or 6(the quantity of sectors in total) sub tuples long
    The index of the sub tuple represents sectors location in the layout as shown below
       9   0   4
     8   1   2   5
       7   3   6

    s - the number of the sector
    r - the rotation position of the sector(0 - pointing up(0 deg), 1 - pointing upper right(60 deg), 5 - pointing upper
        left(300 deg))
    """

    # give the seed parameter to the random module if one is provided and an empty sectors list is created
    if seed is not 0:
        random.seed(seed)
    randomized_sectors = list()

    # fill the sectors list with either 6 or 10 sectors, depending on the number of players argument
    if number_of_players == 3 or number_of_players == 4:
        randomized_sectors = [[1, -1], [2, -1], [3, -1], [4, -1], [5, -1], [6, -1], [7, -1], [8, -1], [9, -1], [10, -1]]
    elif number_of_players == 1 or number_of_players == 2:
        randomized_sectors = [[1, -1], [2, -1], [3, -1], [4, -1], [5, -1], [6, -1]]
    else:
        raise ValueError

    # sectors locations and rotation positions are randomized
    random.shuffle(randomized_sectors)
    for sector in randomized_sectors:
        sector[1] = random.choice(range(6))
        sector = tuple(sector)

    # return a tuple of the randomized sectors list
    return tuple(randomized_sectors)


def generate_round_scoring_tiles(seed=setted_seed):
    """This function returns a tuple of 6 round scoring tiles"""

    if seed is not 0:
        random.seed(seed)
    all_tiles_list = [1, 2, 3, 4, 5, 5, 6, 6, 7, 7]
    randomized_tiles = list()

    for _ in range(6):
        chosen_tile_index = random.randint(0, len(all_tiles_list) - 1)
        randomized_tiles.append(all_tiles_list[chosen_tile_index])
        all_tiles_list.pop(chosen_tile_index)

    return tuple(randomized_tiles)


def generate_final_scoring_tiles(seed=setted_seed):
    """This function returns a tuple 2 final scoring tiles"""

    if seed is not 0:
        random.seed(seed)
    all_tiles_list = [1, 2, 3, 4, 5, 6]
    randomized_tiles = list()

    for _ in range(2):
        chosen_tile_index = random.randint(0, len(all_tiles_list) - 1)
        randomized_tiles.append(all_tiles_list[chosen_tile_index])
        all_tiles_list.pop(chosen_tile_index)

    return tuple(randomized_tiles)


def generate_round_boosters(number_of_players=4, seed=setted_seed):
    """This function returns a tuple of number of players + 3 round booster tiles"""

    if seed is not 0:
        random.seed(seed)
    all_boosters_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    randomized_tiles = list()

    for _ in range(number_of_players + 3):
        chosen_tile_index = random.randint(0, len(all_boosters_list) - 1)
        randomized_tiles.append(all_boosters_list[chosen_tile_index])
        all_boosters_list.pop(chosen_tile_index)

    return tuple(randomized_tiles)


def generate_standard_tech_tiles(seed=setted_seed):
    """This function returns a tuple of 9 standard tiles

    The first 6 of the sequence are going under the 6 research tracks from left to right
        ([0] - Terrafotming, [2] - Artificial intelligence, etc.)
    The last 3 are going in the three trackless slots
    """

    if seed is not 0:
        random.seed(seed)
    all_standard_tiles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    randomized_tiles = list()

    for _ in range(9):
        chosen_tile_index = random.randint(0, len(all_standard_tiles) - 1)
        randomized_tiles.append(all_standard_tiles[chosen_tile_index])
        all_standard_tiles.pop(chosen_tile_index)

    return tuple(randomized_tiles)


def generate_advanced_tech_tiles(seed=setted_seed):
    """This function returns a tuple of 6 advanced tech tiles

    The first 6 of the sequence are going under the 6 research tracks from left to right
        ([0] - Terrafotming, [2] - Artificial intelligence, etc.)
    The last 3 are going in the three trackless slots
    """

    if seed is not 0:
        random.seed(seed)
    all_advanced_tiles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ,15]
    randomized_tiles = list()

    for _ in range(6):
        chosen_tile_index = random.randint(0, len(all_advanced_tiles) - 1)
        randomized_tiles.append(all_advanced_tiles[chosen_tile_index])
        all_advanced_tiles.pop(chosen_tile_index)

    return tuple(randomized_tiles)


def generate_races(seed=setted_seed):

    if seed is not 0:
        random.seed(seed)
    all_races = ((1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14))
    randomized_races = list()

    for i in range(7):
        randomized_races.append(all_races[i][random.randint(0,1)])

    return tuple(randomized_races)

