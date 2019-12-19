import numpy as np
from day9 import day9
from os import system

wall = 0
free = 1
oxy = 2

north = 1
south = 2
west = 3
east = 4


def coord_from_input(input_val):
    if input_val == north:
        return 0, 1
    elif input_val == east:
        return 1, 0
    elif input_val == south:
        return 0, -1
    else:
        return -1, 0


def change_direction(input_val):
    if input_val == north:
        return east
    elif input_val == east:
        return south
    elif input_val == south:
        return west
    else:
        return north


def change_direction_2(input_val):
    if input_val == north:
        return west
    elif input_val == west:
        return south
    elif input_val == south:
        return east
    else:
        return north


def print_it(extreme_vals, area_vals, robot_vals):
    system('cls')
    for y in reversed(range(extreme_vals[2], extreme_vals[3])):
        text = ''
        for x in range(extreme_vals[0], extreme_vals[1]):
            val = area_vals.get((x, y), 3)
            if (x, y) == robot_vals:
                text += 'R'
            elif val == 0:
                text += '#'
            elif val == 1:
                text += '.'
            elif val == 2:
                text += 'O'
            else:
                text += ' '
        print(text)


def find_reachable_neighbours(area_val, field_val):
    result = []
    for c in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        check_coord = (field_val[0] + c[0], field_val[1] + c[1])
        if check_coord in area_val:
            if area_val[check_coord] != 0:
                result.append(check_coord)
    return result


def main():
    read_data = np.loadtxt('input.txt', delimiter=',', dtype=np.int64)
    comp = day9.computer(read_data)
    area = {(0, 0): 1}
    stop = False
    x = 0
    y = 0
    xmin = 0
    xmax = 0
    ymin = 0
    ymax = 0
    counter = 0
    input_value = 1
    while not stop:
        output, stop = comp.process_until_output(input_value)
        coord = coord_from_input(input_value)
        if output == 0:
            area[(x + coord[0], y + coord[1])] = output
            input_value = change_direction(input_value)
        else:
            x += coord[0]
            y += coord[1]
            if (x, y) in area:
                input_value = change_direction_2(input_value)
            area[(x, y)] = output
            if output == 2:
                stop = True

        xmin = np.minimum(xmin, x)
        xmax = np.maximum(xmax, x)
        ymin = np.minimum(ymin, y)
        ymax = np.maximum(ymax, y)
        counter += 1
        #if counter % 1000 == 0:
        #    print_it((xmin - 1, xmax + 2, ymin - 1, ymax + 2), area, (x, y))
    oxy = ()
    for a in area:
        if area[a] == 2:
            oxy = a
            break

    print_it((xmin - 1, xmax + 2, ymin - 1, ymax + 2), area, (0, 0))
    numbered = {}
    # search shortest path
    to_check = [(oxy[0], oxy[1], 0)]
    while len(to_check) > 0:
        current = to_check.pop(0)
        current_coord = (current[0], current[1])
        if current_coord not in numbered or numbered[current_coord] > current[2]:
            numbered[current_coord] = current[2]
            neigh = find_reachable_neighbours(area, current_coord)
            for n in neigh:
                to_check.append((n[0], n[1], current[2] + 1))
    print(np.max(np.asarray(numbered.values())))

if __name__ == "__main__":
    main()
