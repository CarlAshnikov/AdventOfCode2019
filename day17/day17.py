import numpy as np
from day9 import day9
from day11 import day11
import sys

def print_field(field, maxx_val, miny_val):
    for y in reversed(range(miny_val, 1)):
        text = '|'
        for x in range(0, maxx_val):
            text += field.get((x, y), '.')
        print(text)


def extraction(input_text):
    #text = 'R,6,L,6,L,10,L,8,L,6,L,10,L,6,R,6,L,6,L,10,L,8,L,6,L,10,L,6,R,6,L,8,L,10,R,6,R,6,L,6,L,10,L,8,L,6,L,10,L,6' + \
    #       ',R,6,L,8,L,10,R,6,R,6,L,6,L,10,R,6,L,8,L,10,R,6'
    text = input_text
    lengths = []
    for a in range(1, 6):
        for b in range(1, 6):
            for c in range(1, 6):
                lengths.append([a, b, c])
    finished = False
    patterns = []
    for current_lengths in lengths:
        idx = 0
        patterns = []
        while idx < len(text):
            matched = False
            current_text = text[idx:]
            for p in patterns:
                if current_text.startswith(p):
                    # skip match + adjacent comma
                    idx += len(p) + 1
                    matched = True
                    break
            # matched is good
            if matched:
                continue

            # not matched and no pattern available = leave
            if len(patterns) >= 3:
                break

            # take pattern with current length
            length = current_lengths[len(patterns)]
            pattern = ','.join(current_text.split(',')[:2 * length])
            patterns.append(pattern)
            idx += len(pattern) + 1

        if idx >= len(text):
            finished = True
            break

    if finished:
        # print(patterns)
        for d in zip(patterns, ['A', 'B', 'C']):
            text = text.replace(d[0], d[1])
        # print(text)
        return text, patterns


def get_adjacent_fields(coord):
    result = []
    for i in [-1, 1]:
        result.append((coord[0], coord[1] + i))
        result.append((coord[0] + i, coord[1]))
    return result


def to_ascii_array(text):
    res = [ord(x) for x in text]
    res.append(10)
    return res


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
        output, stop = comp.process_until_output(0, False, True)
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

    res, pats = extraction(','.join(walk_the_way(field)))

    main = to_ascii_array(res)
    pattern_ascii = [to_ascii_array(x) for x in pats]
    feed_and_print(comp, main)
    for p in pattern_ascii:
        feed_and_print(comp, p)

    comp.process_until_output(ord('n'), True)
    comp.process_until_output(10, True)
    stop = False
    while not stop:
        output, stop = comp.process_until_output(0)
        print(output)

def feed_and_print(comp, data):
    stop = False
    for n in data:
        output, stop = comp.process_until_output(n, True)

    text = '|'
    while not stop:
        output, stop = comp.process_until_output(0, False, True)
        if output == 10:
            print(text)
            text = '|'
        else:
            if not stop:
                text += chr(output)

def walk_the_way(field):
    rob_pos = ()
    for f in field:
        val = field[f]
        if field[f] in ['^', '>', '<', 'v']:
            rob_pos = f
    rob = day11.Robot()
    rob.x = rob_pos[0]
    rob.y = rob_pos[1]

    moves = []
    move_counter = 0
    while True:
        if field.get(rob.do_move(rob.x, rob.y, rob.direction), '.') == '#':
            rob.move()
            move_counter += 1
        elif field.get(rob.do_move(rob.x, rob.y, rob.get_right_turn(rob.direction)), '.') == '#':
            if move_counter != 0:
                moves.append(str(move_counter))
            rob.turn_right()
            moves.append('R')
            move_counter = 0
        elif field.get(rob.do_move(rob.x, rob.y, rob.get_left_turn(rob.direction)), '.') == '#':
            if move_counter != 0:
                moves.append(str(move_counter))
            rob.turn_left()
            moves.append('L')
            move_counter = 0
        else:
            if move_counter != 0:
                moves.append(str(move_counter))
            break
    return moves


def extract_intersections(field):
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
                # print('{} {} {}'.format(coord, value, sum))
    print(sum)


if __name__ == "__main__":
    main()
