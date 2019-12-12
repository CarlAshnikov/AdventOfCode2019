import numpy as np

asteroids = []
with open("input.txt", 'r') as input_file:
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
    result = -np.arctan2(-a_ratio[:, 1], a_ratio[:, 0]) / np.pi * 180 + 90
    result[np.where(result < 0)] += 360
    return result


def get_ratios(a_current, invalid=None):
    if invalid is None:
        invalid = []
    a_ratios = np.array([])
    indices = []
    counter = 0
    distances = []
    for compare in asteroids:
        if np.any(a_current != compare) and counter not in invalid:
            ratio = get_ratio(compare - a_current)
            if a_ratios.size == 0:
                a_ratios = np.array([ratio])
                indices.append(counter)
                distances.append(np.linalg.norm(compare - a_current))
            else:
                stuff = np.all(a_ratios == ratio, axis=1)
                if not np.any(stuff):
                    a_ratios = np.append(a_ratios, [ratio], axis=0)
                    indices.append(counter)
                    distances.append(np.linalg.norm(compare - a_current))
                else:
                    found_at = int(np.where(stuff)[0])
                    dist = np.linalg.norm(compare - a_current)
                    if distances[found_at] > dist:
                        distances[found_at] = dist
                        indices[found_at] = counter
        counter += 1
    return a_ratios, indices


# 11 13 210
nums = []
for current in asteroids:
    ratios, asteroid_indices = get_ratios(current)
    nums.append(ratios.size / 2)

for s in zip(asteroids, nums):
    print(s[0], s[1])
station = asteroids[np.argmax(nums)]
print(station)
print(np.max(nums))

destroyed = []
while len(destroyed) < len(asteroids) - 1:
    ratios, asteroid_indices = get_ratios(station, destroyed)
    angles = ratio_to_angle(ratios)
    #for dat in zip(ratios, asteroid_indices, angles):
    #    print('{} {} {}'.format(dat[0], asteroids[dat[1]], dat[2]))
    current_data = list(zip(angles, asteroid_indices))
    current_data.sort(key=lambda x: x[0])
    for dat in current_data:
        print('{} {} {}'.format(len(destroyed) + 1, asteroids[dat[1]], dat[0]))
        destroyed.append(dat[1])
asteroid_200 = asteroids[destroyed[199]]
print(asteroid_200[0] * 100 + asteroid_200[1])
