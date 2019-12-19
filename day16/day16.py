import numpy as np


def create_pattern(length, number, offset):
    vals = [0, 1, 0, -1]
    result = np.ones(length)
    count = 0
    val_index = 0
    while count < length:
        if (count + offset) % number == 0:
            val_index += 1
            val_index %= 4
        result[count] = vals[val_index]
        count += 1
    return result


def part_1(input_val):
    length_input = len(input_val)

    for i in range(1, 101):
        result_values = np.ones(length_input)
        for j in range(1, length_input + 1):
            pat = create_pattern(length_input, j, 1)
            result_values[j - 1] = np.sum(input_val * pat)
        input_val = np.array(result_values)
        input_val = np.abs(input_val)
        input_val = np.mod(input_val, 10)
        print('phase {}: {}'.format(i, input_val[:8]))


def main():
    with open('input.txt', 'r') as inputfile:
        input_data = np.array([int(x) for x in inputfile.readline().strip()])

    # part_1(input_data.copy())

    offset = ''.join([str(x) for x in input_data[:7]])
    offset = int(offset)
    input_val = np.tile(input_data, 10000)

    input_val = input_val[offset:]

    for i in range(1, 101):
        newdata = np.ones(len(input_val))
        newdata[-1] = input_val[-1]
        for j in reversed(range(len(input_val) - 1)):
            newdata[j] = newdata[j + 1] + input_val[j]

        input_val = np.mod(np.abs(np.asarray(newdata)), 10)

        print("round {} {}".format(i, input_val[:8]))


if __name__ == "__main__":
    main()
