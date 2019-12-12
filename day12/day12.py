import itertools
import numpy as np

class Moon:
    def __init__(self, ax, ay, az):
        self.x = ax
        self.y = ay
        self.z = az
        self.vx = 0
        self.vy = 0
        self.vz = 0

    def __str__(self):
        return 'pos=<x={} y={} z={}> vel=<x={} y={} z={}>'.format(self.x, self.y, self.z, self.vx, self.vy, self.vz)

    def apply_velocity(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def get_energy(self):
        return (np.abs(self.x) + np.abs(self.y) + np.abs(self.z)) *\
               (np.abs(self.vx) + np.abs(self.vy) + np.abs(self.vz))

    def to_array(self):
        return np.array([self.x, self.y, self.z, self.vx, self.vy, self.vz])


def main():
    moons = []
    current = []
    with open("input.txt", "r") as input_file:

        for line in input_file:
            data = line.strip()[1:-1].split(", ")
            nums = [int(dat.split('=')[1]) for dat in data]
            moon = Moon(*nums)
            moons.append(moon)
            # print(moon)
            current.append(moon.to_array())

    previous_constellation = np.array([current])

    for i in range(3000):
        perms = itertools.combinations(moons, 2)
        # apply gravity
        for p in perms:
            p[0].vx += np.sign(p[1].x - p[0].x)
            p[1].vx += np.sign(p[0].x - p[1].x)
            p[0].vy += np.sign(p[1].y - p[0].y)
            p[1].vy += np.sign(p[0].y - p[1].y)
            p[0].vz += np.sign(p[1].z - p[0].z)
            p[1].vz += np.sign(p[0].z - p[1].z)

        # print('')
        # print("after {} steps".format(i + 1))
        # total_energy = 0
        current = []
        for moon in moons:
            moon.apply_velocity()
            # print(moon)
            # total_energy += moon.get_energy()
            current.append(moon.to_array())
        current = np.asarray(current)

        if current in previous_constellation:
            print("found after {} steps".format(i))
            break
        else:
            print("step {}".format(i))

        previous_constellation = np.append(previous_constellation, [current], axis=0)

        # print("total energy: {}".format(total_energy))
    # print(previous_constellation)


if __name__ == "__main__":
    main()
