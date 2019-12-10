import numpy as np

asteroids = []
with open("input_test.txt", 'r') as input_file:
    row = 0
    for line in input_file:
        col = 0
        for entry in line.strip():
            if entry == '#':
                asteroids.append(np.array([col, row]))
            col += 1
        row += 1


def get_ratio(coordinate):
    for i in range(2, np.min(np.abs(coordinate))):
        while (coordinate[0] % i) == 0 and (coordinate[1] % i) == 0 and coordinate[0] != 0 \
                and coordinate[1] != 0:
            coordinate[0] = int(coordinate[0] / i)
            coordinate[1] = int(coordinate[1] / i)
    if coordinate[1] != 0 and (coordinate[0] % coordinate[1]) == 0:
        coordinate[0] = int(coordinate[0] / np.abs(coordinate[1]))
        coordinate[1] = int(coordinate[1] / np.abs(coordinate[1]))
    if coordinate[0] != 0 and (coordinate[1] % coordinate[0]) == 0:
        coordinate[1] = int(coordinate[1] / np.abs(coordinate[0]))
        coordinate[0] = int(coordinate[0] / np.abs(coordinate[0]))
    return coordinate


def ratio_to_angle(a_ratio):
    return -np.arctan2(-a_ratio[:, 1], a_ratio[:, 0]) / np.pi * 180 + 90


def get_ratios(a_current):
    a_ratios = np.array([])
    for compare in asteroids:
        if np.any(a_current != compare):
            ratio = get_ratio(compare - a_current)
            if a_ratios.size == 0:
                a_ratios = np.array([ratio])
            else:
                stuff = np.all(a_ratios == ratio, axis=1)
                if not np.any(stuff):
                    a_ratios = np.append(a_ratios, [ratio], axis=0)
    return a_ratios


# 11 33 210
nums = []
for current in asteroids:
    ratios = get_ratios(current)
    nums.append(ratios.size / 2)

for s in zip(asteroids, nums):
    print(s[0], s[1])
station = asteroids[np.argmax(nums)]
print(station)
print(np.max(nums))
