# Feladat leírás:
# Adott egy 4X4-es saktábla. A satktáblára 1 királynőt és 1 huszárt kell elhelyezni, oly módon, hogy ( az ismert szabályok
# értelmében ) ne tudják leütni egymász. Hányféleképp tudjuk ezt megtenni?
#
# Megoldás logikája:
# Felvettem 2 db 7X7-es numpy tömböt ez jelképezi a sakktáblát. (Azért 7X7-es a tábla, hogy amikor csúsztatom az X
# helyét mindig benne maradjon a 4X4 tartományban )

# A királynő tömbjében 'X'-el jelöltem a királynő helyét és 'q' val az általa üthető mezőket.
# A Huszár tömbjében 'X'-el jelöltem a huszár helyét és 'h' val az általa üthető mezőket.

# A tömböket egymásra vetítve rendre összeadtam őket, és ahol a táblán nem szerpel sem az 'Xh' sem a 'qX',
# abban a felállásban nincs ütközés.

import numpy as np
from numpy import char


def get_all_options(hit_table):
    """ return all lineups
        Input: numpy_array
        Output: numpy_array """

    return [hit_table[i:i + 4, j:j + 4].copy() for j in range(3, -1, -1) for i in range(3, -1, -1)]


def possible(all_queen_options, all_horse_options):
    """ Return all possible lineups
        Inputs: numpy_array, numpy_array
        Output: int """

    available_count = 0

    for q in all_queen_options:
        for h in all_horse_options:

            current = char.add(q, h)
            if (current == 'XX').sum() or (current == 'qX').sum() or (current == 'Xh').sum(): continue
            available_count += 1

    return available_count


queen = np.array([
    ['q', '.', '.', 'q', '.', '.', 'q'],
    ['.', 'q', '.', 'q', '.', 'q', '.'],
    ['.', '.', 'q', 'q', 'q', '.', '.'],
    ['q', 'q', 'q', 'X', 'q', 'q', 'q'],
    ['.', '.', 'q', 'q', 'q', '.', '.'],
    ['.', 'q', '.', 'q', '.', 'q', '.'],
    ['q', '.', '.', 'q', '.', '.', 'q'],
])


horse = np.array([
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', 'h', '.', 'h', '.', '.'],
    ['.', 'h', '.', '.', '.', 'h', '.'],
    ['.', '.', '.', 'X', '.', '.', '.'],
    ['.', 'h', '.', '.', '.', 'h', '.'],
    ['.', '.', 'h', '.', 'h', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
])

all_queen_options = get_all_options(queen)
all_horse_options = get_all_options(horse)

print(f'{possible(all_queen_options, all_horse_options)} féle képpen lehet elhelyezni a királynőt és a huszárt',\
        'úgy, hogy azok ne üssék egymást.')
