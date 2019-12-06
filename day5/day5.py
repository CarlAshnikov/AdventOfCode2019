import numpy as np
import sys

first_data = np.loadtxt('input.txt', delimiter=',', dtype=int)

instruction_pointer = 0
stop = False


def get_value(value_type, value):
    if value_type == 0:
        return first_data[value]
    else:
        return value


def get_input():
    return 5


outputs = 0


def get_first_value(a_instruction):
    return get_value(a_instruction[-3], first_data[instruction_pointer + 1])


def get_second_value(a_instruction):
    return get_value(a_instruction[-4], first_data[instruction_pointer + 2])


while not stop:
    instruction = [int(x) for x in "{:05d}".format(first_data[instruction_pointer])]

    if instruction[-1] == 1:
        val1 = get_first_value(instruction)
        val2 = get_second_value(instruction)
        res = val1 + val2
        first_data[first_data[instruction_pointer + 3]] = res
        instruction_pointer += 4
    elif instruction[-1] == 2:
        val1 = get_first_value(instruction)
        val2 = get_second_value(instruction)
        res = val1 * val2
        first_data[first_data[instruction_pointer + 3]] = res
        instruction_pointer += 4
    elif instruction[-1] == 3:
        first_data[first_data[instruction_pointer + 1]] = get_input()
        instruction_pointer += 2
    elif instruction[-1] == 4:
        print("output: {}".format(get_first_value(instruction)))
        instruction_pointer += 2
        outputs += 1
    elif instruction[-1] == 5:
        if get_first_value(instruction) != 0:
            instruction_pointer = get_second_value(instruction)
        else:
            instruction_pointer += 3
    elif instruction[-1] == 6:
        if get_first_value(instruction) == 0:
            instruction_pointer = get_second_value(instruction)
        else:
            instruction_pointer += 3
    elif instruction[-1] == 7:  # less than
        if get_first_value(instruction) < get_second_value(instruction):
            first_data[first_data[instruction_pointer + 3]] = 1
        else:
            first_data[first_data[instruction_pointer + 3]] = 0
        instruction_pointer += 4
    elif instruction[-1] == 8:
        if get_first_value(instruction) == get_second_value(instruction):
            first_data[first_data[instruction_pointer + 3]] = 1
        else:
            first_data[first_data[instruction_pointer + 3]] = 0
        instruction_pointer += 4
    elif instruction[-1] == 9 and instruction[-2] == 9:
        print("Finished!")
        break
    else:
        print("ERROR")
        sys.exit()
