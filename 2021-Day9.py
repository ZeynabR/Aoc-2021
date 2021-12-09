import numpy as np

def make_matrix(rows, columns, lines):
    locations = np.zeros((rows, columns))
    for l in range(rows):
        for k in range(columns):
            num = int(lines[l][k])
            locations[l][k] = num
    return locations


def find_basin(rows, columns, locations):
    basins = []
    for r in range(rows):
        for c in range(columns):
            if locations[r][c] != 9:
                index = r * columns + c
                if c == columns - 1:
                    indexes = [i for i in [index - 1, index + columns, index - columns] if
                               i in [*range(columns * rows - 1)]]
                elif c == 0:
                    indexes = [i for i in [index + 1, index + columns, index - columns] if
                               i in [*range(columns * rows - 1)]]
                else:
                    indexes = [i for i in [index + 1, index - 1, index + columns, index - columns] if
                               i in [*range(columns * rows - 1)]]
                adjacent = [i for i in indexes if locations[int(i / columns)][i % columns] < 9] + [index]
                basin_check = [i for i in basins if any(j in i for j in adjacent)]
                if basin_check == []:
                    basins.append(adjacent)
                else:
                    adjacent = [i for i in adjacent if i not in basin_check[0]]
                    basins[basins.index(basin_check[0])] += adjacent
    return basins


with open('Day9-Data') as f:
    lines = f.readlines()
lines = [list(l.strip()) for l in lines]
rows = int(len(lines))
# print(rows)
columns = int(len(lines[0]))
# print(columns)
locations = make_matrix(rows, columns, lines)
basins = find_basin(rows, columns, locations)
basins_size = sorted([len(set(b)) for b in basins])
print(basins_size[-1] * basins_size[-2] * basins_size[-3])
