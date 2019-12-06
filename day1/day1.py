import numpy as np

data = np.loadtxt('input.txt')
sum = 0
for i in data:
    result = i
    while result > 0:
        result = np.floor(result / 3) - 2
        if result < 0:
            break
        sum += result


print(sum)