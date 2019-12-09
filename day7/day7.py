import numpy as np
import sys
import itertools

read_data = np.loadtxt('day7/input.txt', delimiter=',', dtype=int)

stop = False

print(read_data)

outputs = 0

class thruster():
    def __init__(self, data, phase):
        self.phase = phase
        self.data = data
        self.pointer = 0
        self.stopped = False
        self.get_phase = True
        self.last_output_value = 0

    def get_first_value(self, a_instruction):
        return self.get_value(a_instruction[-3], self.data[self.pointer + 1])


    def get_second_value(self, a_instruction):
        return self.get_value(a_instruction[-4], self.data[self.pointer + 2])


    def get_value(self, value_type, value):
        if value_type == 0:
            return self.data[value]
        else:
            return value


    def get_input(self, amp):
        if self.get_phase:
            self.get_phase = False
            return phase_settings[amp]
        else:
            return self.last_output_value

    def process_until_output(self, input_value):
        self.last_output_value = input_value
        while True:
            instruction = [int(x) for x in "{:05d}".format(self.data[self.pointer])]

            if instruction[-1] == 1:
                val1 = self.get_first_value(instruction)
                val2 = self.get_second_value(instruction)
                res = val1 + val2                    
                self.data[self.data[self.pointer + 3]] = res
                self.pointer += 4
            elif instruction[-1] == 2:
                val1 = self.get_first_value(instruction)
                val2 = self.get_second_value(instruction)
                res = val1 * val2
                self.data[self.data[self.pointer + 3]] = res
                self.pointer += 4
            elif instruction[-1] == 3:
                self.data[self.data[self.pointer + 1]] = self.get_input(i)
                self.pointer += 2
            elif instruction[-1] == 4:
                #print("output: {}".format(get_first_value(instruction)))
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
                    self.data[self.data[self.pointer + 3]] = 1
                else:
                    self.data[self.data[self.pointer + 3]] = 0
                self.pointer += 4
            elif instruction[-1] == 8:
                if self.get_first_value(instruction) == self.get_second_value(instruction):
                    self.data[self.data[self.pointer + 3]] = 1
                else:
                    self.data[self.data[self.pointer + 3]] = 0
                self.pointer += 4
            elif instruction[-1] == 9 and instruction[-2] == 9:
                #print("Finished! {}".format(i))
                self.stopped = True
                return (self.last_output_value, True)
            else:
                print("ERROR")
                sys.exit()

phase_set = [5, 6, 7, 8, 9]

perms = itertools.permutations(phase_set)
max_val = 0
max_phases = []
results = {}

for phase_settings in perms:
    thrusters = []
    for i in range(5):
        thrusters.append(thruster(read_data.copy(), phase_settings[i]))
    run = 0
    stop = False        
    last_output_value = 0

    while not stop == True:
        run += 1

        for i in range(5):
            last_output_value, stop = thrusters[i].process_until_output(last_output_value)
            
            
        print("run: {} {} {}".format(run, phase_settings, last_output_value)) 
        if last_output_value > max_val:
            max_val = last_output_value
            max_phases = phase_settings

print("max {} {}".format(max_phases, max_val))
