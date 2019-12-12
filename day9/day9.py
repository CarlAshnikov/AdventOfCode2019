import numpy as np
import sys
import itertools

class computer():
    def __init__(self, data):
        self.data = data
        self.pointer = 0
        self.stopped = False
        self.get_phase = True
        self.last_output_value = 0
        self.relative_base = 0

    def get_first_value(self, a_instruction):
        return self.get_value(a_instruction[-3], self.data[self.pointer + 1])

    def get_second_value(self, a_instruction):
        return self.get_value(a_instruction[-4], self.data[self.pointer + 2])

    def check_index(self, index):
        diff = index - len(self.data) + 1
        if diff > 0:
            zeros = np.zeros(diff + 2, dtype=np.int64)
            self.data = np.append(self.data, zeros, axis=0)

    def get_value(self, value_type, value):
        if value_type == 0:
            ind = value
        elif value_type == 1:
            return value
        else:
            ind = value + self.relative_base
        self.check_index(ind)
        return self.data[ind]

    def write_value(self, value_type, index, data):
        if value_type == 0:
            ind = int(index)
        elif value_type == 2:
            ind = (index) + self.relative_base
        else:
            print("ERROR")
            exit()
        self.check_index(ind)
        self.data[ind] = int(data)

    def get_input(self):
        return self.last_output_value

    def process_until_output(self, input_value):
        self.last_output_value = input_value
        while True:
            instruction = [int(x) for x in "{:05d}".format(self.data[self.pointer])]

            if instruction[-1] == 1:
                val1 = self.get_first_value(instruction)
                val2 = self.get_second_value(instruction)
                res = val1 + val2
                self.write_value(instruction[-5], self.data[self.pointer + 3], res)
                self.pointer += 4
            elif instruction[-1] == 2:
                val1 = self.get_first_value(instruction)
                val2 = self.get_second_value(instruction)
                res = val1 * val2
                self.write_value(instruction[-5], self.data[self.pointer + 3], res)
                self.pointer += 4
            elif instruction[-1] == 3:
                self.write_value(instruction[-3], self.data[self.pointer + 1], self.get_input())
                self.pointer += 2
            elif instruction[-1] == 4:
                # print("output: {}".format(get_first_value(instruction)))
                self.last_output_value = self.get_first_value(instruction)
                self.pointer += 2
                return (self.last_output_value, False)
            elif instruction[-1] == 5:
                if self.get_first_value(instruction) != 0:
                    self.pointer = self.get_second_value(instruction)
                else:
                    self.pointer += 3
            elif instruction[-1] == 6:
                if self.get_first_value(instruction) == 0:
                    self.pointer = self.get_second_value(instruction)
                else:
                    self.pointer += 3
            elif instruction[-1] == 7:  # less than
                if self.get_first_value(instruction) < self.get_second_value(instruction):
                    self.write_value(instruction[-5], self.data[self.pointer + 3], 1)
                else:
                    self.write_value(instruction[-5], self.data[self.pointer + 3], 0)
                self.pointer += 4
            elif instruction[-1] == 8:
                if self.get_first_value(instruction) == self.get_second_value(instruction):
                    self.write_value(instruction[-5], self.data[self.pointer + 3], 1)
                else:
                    self.write_value(instruction[-5], self.data[self.pointer + 3], 0)
                self.pointer += 4
            elif instruction[-1] == 9 and instruction[-2] == 9:
                # print("Finished! {}".format(i))
                self.stopped = True
                return (self.last_output_value, True)
            elif instruction[-1] == 9:
                self.relative_base += self.get_first_value(instruction)
                self.pointer += 2
            else:
                print("ERROR")
                sys.exit()

def main():
    read_data = np.loadtxt('input.txt', delimiter=',', dtype=np.int64)

    stop = False

    print(read_data)

    outputs = 0
    comp = computer(read_data.copy())
    stop = False
    while not stop:
        res, stop = comp.process_until_output(2)
        print(res)
