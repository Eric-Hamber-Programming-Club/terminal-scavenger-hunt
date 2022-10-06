import random
import sys
import os

MAXIMUM_NODES = 200

# load words
with open("words.txt", "r") as f:
    words = f.read().strip().split("\n")

# get/set seed
seed = input("Enter seed: ")
if not seed:
    seed = random.randrange(sys.maxsize)

if isinstance(seed, str) and seed.isdigit():
    seed = int(seed)

random.seed(seed)
print(f"Initialized generator with seed {seed}")

# build graph
n = random.randrange(MAXIMUM_NODES)
prufer = dict((i, 1) for i in range(n))
pruferlist = []
tree = dict((i, []) for i in range(n))

for i in range(n-2):
    x = random.randrange(n)
    prufer[x] += 1
    pruferlist.append(x)


for el in pruferlist:
    for i in range(n):
        if prufer[i] == 1:
            tree[el].append(i)
            tree[i].append(el)
            prufer[i] -= 1
            prufer[el] -= 1
            break


