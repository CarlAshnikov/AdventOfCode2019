import numpy as np
from day9 import day9


def print_field(field, maxx_val, miny_val):
    for y in reversed(range(miny_val, 1)):
        text = '|'
        for x in range(0, maxx_val):
            text += field[(x, y)]
        print(text)


def get_adjacent_fields(coord):
    result = []
    for i in [-1, 1]:
        result.append((coord[0], coord[1] + i))
        result.append((coord[0] + i, coord[1]))
    return result


def main():
    read_data = np.loadtxt('input.txt', delimiter=',', dtype=np.int64)
    comp = day9.computer(read_data)
    stop = False
    x = 0
    y = 0
    maxx = 0
    miny = 0
    field = {}
    while not stop:
        output, stop = comp.process_until_output(0)
        if output == 10:
            y -= 1
            if maxx == 0:
                maxx = x
            x = 0
        else:
            if not stop:
                field[(x, y)] = chr(output)
                if y < miny:
                    miny = y
            x += 1

    print_field(field, maxx, miny)
    sum = 0
    for coord in field:
        if field[coord] == '#':
            adjacent = get_adjacent_fields(coord)
            count = 0
            for a in adjacent:
                if field.get(a, '.') == '#':
                    count += 1
            if count >= 3:
                value = np.abs(coord[0]) * np.abs(coord[1])
                sum += value
                print('{} {} {}'.format(coord, value, sum))

    print(sum)


if __name__ == "__main__":
    main()