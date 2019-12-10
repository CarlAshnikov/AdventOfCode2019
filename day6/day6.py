import numpy as np
import sys

data = np.loadtxt('input.txt', delimiter=')', dtype=str)


class Node:
    def __init__(self, my_name):
        self.name = my_name
        self.pred = None
        self.succ = []

    def add_successor(self, anode):
        self.succ.append(anode)


nodes = {}
names = set()
for dat in data:
    names.add(dat[0])
    names.add(dat[1])

for name in names:
    node = Node(name)
    nodes[name] = node

for dat in data:
    nodes[dat[1]].pred = nodes[dat[0]]
    nodes[dat[0]].add_successor(nodes[dat[1]])

counter = 0
for name in nodes:
    current_node = nodes[name]
    while current_node.pred is not None:
        counter += 1
        current_node = current_node.pred

print(counter)

you_path = []
san_path = []

current_node = nodes["YOU"]
while current_node.pred is not None:
    you_path.append(current_node.pred.name)
    current_node = current_node.pred

current_node = nodes["SAN"]
while current_node.pred is not None:
    san_path.append(current_node.pred.name)
    current_node = current_node.pred

for name in you_path:
    for name2 in san_path:
        if name == name2:
            print(name)
            print(you_path.index(name) + san_path.index(name2))
            sys.exit()
