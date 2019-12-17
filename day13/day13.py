import numpy as np
from day9 import day9


def print_playfield(field, ball, paddle):
    for y in range(25):
        text = ''
        for x in range(40):
            val = field[(x, y)]
            if val == 0:  # empty
                text += ' '
            elif val == 1:  # wall
                text += '|'
            elif val == 2:  # block
                text += '#'
            elif val == 3:  # paddle
                text += 'T'
            else:
                text += 'O'
        print(text)
    if (-1, 0) in field:
        print('score: {} ball: {} paddle: {}'.format(field[(-1, 0)], ball, paddle))


def main():
    read_data = np.loadtxt('input.txt', delimiter=',', dtype=np.int64)
    comp = day9.computer(read_data)
    play_field = {}
    stop = False
    had_input = False
    input_val = 0
    ball_coord = (0, 0)
    paddle_coord = (0, 0)
    while not stop:
        current_values = []
        for i in range(3):
            output, stop = comp.process_until_output(input_val)
            current_values.append(output)
            if stop:
                break

        if not stop:
            play_field[(current_values[0], current_values[1])] = current_values[2]

            if current_values[2] == 3:
                paddle_coord = (current_values[0], current_values[1])

            if current_values[2] == 4:
                coord = (current_values[0], current_values[1])
                going_up = ball_coord[1] > coord[1]
                #if going_up:
                if paddle_coord[0] < coord[0]:
                    input_val = 1

                if paddle_coord[0] > coord[0]:
                    input_val = -1

                if ball_coord == (0, 0) or paddle_coord == (0, 0):
                    input_val = 0

                ball_coord = coord

                if had_input:
                    print_playfield(play_field, ball_coord, paddle_coord)

            if comp.next_is_input():
                print_playfield(play_field, ball_coord, paddle_coord)
                comp.process_input(input_val)
                had_input = True


    print_playfield(play_field, ball_coord, paddle_coord)


if __name__ == "__main__":
    main()
