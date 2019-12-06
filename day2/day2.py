import numpy as np

first_data = np.loadtxt('input.txt', delimiter=',', dtype=int)
target_value = 19690720
program_pointer = 0
first_entry = 0
noun = 0
verb = 0
while first_entry != target_value:
    program_pointer = 0
    data = first_data.copy()
    data[1] = noun
    data[2] = verb
    while data[program_pointer] != 99:
        first = data[data[program_pointer + 1]]
        second = data[data[program_pointer + 2]]
        result = 0
        if data[program_pointer] == 1:
            result = first + second
        elif data[program_pointer] == 2:
            result = first * second
        else:
            print("ERROR")
            exit()
        data[data[program_pointer + 3]] = result
        program_pointer += 4
    first_entry = data[0]
    if first_entry == target_value:
        break
    if verb == 99:
        noun += 1
        verb = 0
    else:
        verb += 1

    if noun == 99:
        break
    
print(100 * noun + verb)
