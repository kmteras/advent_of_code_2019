import math
import os


def fuel_count(mass: float) -> int:
    return math.floor(mass / 3) - 2


# Run tests
assert fuel_count(12) == 2
assert fuel_count(14) == 2
assert fuel_count(1969) == 654
assert fuel_count(100756) == 33583

wd = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(wd, 'modules.txt'), 'r') as f:
    modules = f.read().strip().splitlines()

    print(modules)

    print(sum(list(map(fuel_count, map(lambda x: int(x), modules)))))
