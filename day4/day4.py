import numpy as np
import sys

start_num = 284639
end_num = 748759

counter = 0
current_num = start_num
while current_num < end_num:
    current = np.asarray([int(s) for s in str(current_num)])
    diffs = current[1:] - current[:-1]
    increases = np.min(diffs) >= 0
    nums = np.asarray([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(9, 1)
    diffs = np.abs(current - nums)
    diffs2 = diffs[:, 1:] + diffs[:, :-1]
    #print(diffs2)
    nonz = np.count_nonzero(diffs2 == 0, axis=1)
    is_correct = np.isin(1, nonz)

    if increases and is_correct:
        counter += 1
        print(current_num)

    current_num += 1

print(counter)
