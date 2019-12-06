import numpy as np

wires = []
with open("input.txt", "r") as data_input:
    for line in data_input:
        wire = []
        for entry in line.strip().split(","):
            wire.append((entry[0], int(entry[1:])))
        wires.append(wire)

print(wires)
locations = {}

for wire in wires:
    x = 0
    y = 0
    my_locs = set()
    counter = 0
    for entry in wire:
        for i in range(entry[1]):
            counter += 1
            if entry[0] == 'U':
                y += 1
            elif entry[0] == 'D':
                y -= 1
            elif entry[0] == 'L':
                x -= 1
            else:
                x += 1
            loc = (x, y)
            if loc not in my_locs:
                my_locs.add(loc)
                if loc in locations:
                    locations[loc][1] += 1
                    locations[loc][0] += counter
                else:
                    locations[loc] = [counter, 1]

largeval = 1000000
min_x = largeval
min_y = largeval
max_x = -largeval
max_y = -largeval

min_dist = 10000000000
min_coord = (0, 0)
for loc in locations:
    max_x = max(max_x, loc[0])
    max_y = max(max_y, loc[1])
    min_x = min(min_x, loc[0])
    min_y = min(min_y, loc[1])
    if locations[loc][1] > 1:
        dist = locations[loc][0]
        if dist < min_dist:
            min_dist = dist
            min_coord = loc

print(min_dist)
print(min_coord)


def print_image():
    for y in reversed(range(min_y - 1, max_y + 1)):
        line = ''
        for x in range(min_x - 1, max_x + 1):

            if x == 0 and y == 0:
                line += 'O'
            elif (x, y) in locations:
                line += '+'
            else:
                line += '.'
        print(line)
