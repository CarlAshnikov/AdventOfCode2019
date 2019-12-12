import numpy as np
from day9 import day9
from enum import IntEnum


class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Robot:
    def __init__(self):
        self.direction = Direction.UP
        self.x = 0
        self.y = 0
        self.minx = 0
        self.maxx = 0
        self.miny = 0
        self.maxy = 0

    def move(self):
        if self.direction == Direction.UP:
            self.y += 1
        elif self.direction == Direction.DOWN:
            self.y -= 1
        elif self.direction == Direction.LEFT:
            self.x -= 1
        elif self.direction == Direction.RIGHT:
            self.x += 1

        self.minx = np.minimum(self.x, self.minx)
        self.maxx = np.maximum(self.x, self.maxx)
        self.miny = np.minimum(self.y, self.miny)
        self.maxy = np.maximum(self.y, self.maxy)

    def turn_right(self):
        if self.direction == Direction.LEFT:
            self.direction = Direction.UP
        else:
            self.direction = Direction(self.direction + 1)

    def turn_left(self):
        if self.direction == Direction.UP:
            self.direction = Direction.LEFT
        else:
            self.direction = Direction(self.direction - 1)

    def get_position(self):
        return self.x, self.y


def get_output(input_val, outputcounter):
    outputs = [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0]
    return outputs[outputcounter], outputcounter >= len(outputs) - 1


def main():
    outputcounter = 0
    rob = Robot()
    panels = {}
    read_data = np.loadtxt('input.txt', delimiter=',', dtype=np.int64)
    comp = day9.computer(read_data)
    panels[rob.get_position()] = 1
    print(rob.get_position())
    stop = False
    while not stop:
        if rob.get_position() in panels:
            input_value = panels[rob.get_position()]
        else:
            input_value = 0
        color, stop = comp.process_until_output(input_value)
        # color, stop = get_output(input_value, outputcounter)
        # outputcounter += 1
        panels[rob.get_position()] = color
        turn, stop = comp.process_until_output(input_value)
        # turn, stop = get_output(input_value, outputcounter)
        # outputcounter += 1

        if turn == 0:
            rob.turn_left()
        else:
            rob.turn_right()

        rob.move()

        print(rob.get_position())

    for pan in panels:
        print('{} -> {}'.format(pan, panels[pan]))
    print(len(panels))
    for y in reversed(range(rob.miny-2, rob.maxy+2)):
        text = ''
        for x in range(rob.minx, rob.maxx):
            coord = (x, y)
            if coord in panels:
                if panels[coord] == 0:
                    text += '.'
                else:
                    text += '#'
            else:
                text += '.'
        print(text)

if __name__ == '__main__':
    main()
