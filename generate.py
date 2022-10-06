import random
import sys
import os

with open("words.txt", "r") as f:
    words = f.read().strip().split("\n")

seed = input("Enter seed: ")
if not seed:
    seed = random.randrange(sys.maxsize)

if isinstance(seed, str) and seed.isdigit():
    seed = int(seed)

random.seed(seed)
print(f"Initialized generator with seed {seed}")
print(random.sample(words, 6))
