import numpy as np
import sys
import itertools

with open('day8/input.txt', "r") as input_file:
    line = input_file.readline()
    read_data = [int(x) for x in line]

width = 25

height = 6

num_pix_per_layer = width * height
layers = np.split(np.asarray(read_data), len(read_data) / num_pix_per_layer)

zeros = np.count_nonzero(layers, axis=1)

min_index = np.argmax(zeros)

ones = np.where(layers[min_index] == 1)
twos = np.where(layers[min_index] == 2)
print(len(ones[0]) * len(twos[0]))

result = [2 for i in range(width * height)]
for layer in layers:
    for i in range(width * height):
        if result[i] == 2:
            if layer[i] != 2:
                result[i] = layer[i]

print(np.split(np.asarray(result), height))

for j in range(height):
    text = ""
    for i in range(width):
        if result[i + j * width] == 1:
            text += '.'
        else:
            text += "#"
    print(text)
