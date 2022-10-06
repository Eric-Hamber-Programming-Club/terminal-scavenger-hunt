import random
import sys
import os
import subprocess as sp

MAXIMUM_NODES = 75

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

n1, n2 = [i for i in prufer if prufer[i] != 0]
tree[n1].append(n2)
tree[n2].append(n1)
tree[0].append(-1)

names = random.sample(words, n)

# create directories
def construct(path, parent, node):
    newpath = path + [names[node]]
    tree[node].remove(parent)
    if tree[node]:
        os.mkdir(os.path.join(*newpath))
        for child in tree[node]:
            construct(newpath, node, child)
    else:
        add_file(newpath)

image = False
def add_file(path):
    global image
    number = random.randint(1, 10)
    if number == 1:
        file, ext = "suspicious", ".jpg" if image else ".txt"
        image = not image
    elif 2 <= number <= 7:
        file, ext = "fishyfile", ".txt"
    else:
        file, ext = "fish", ".jpg"
    
    sp.call(f"cp {file+ext} {os.path.join(*path)}{ext}", shell=True)


construct([], -1, 0)
print("folders generated.")
        


