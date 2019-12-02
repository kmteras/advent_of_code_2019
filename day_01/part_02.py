import math
import os


def fuel_count(mass: float) -> int:
    fuel = max(0, math.floor(mass / 3) - 2)
    if fuel <= 0:
        return fuel
    else:
        return fuel + fuel_count(fuel)


# Run tests
assert fuel_count(14) == 2
assert fuel_count(1969) == 966
assert fuel_count(100756) == 50346

wd = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(wd, 'modules.txt'), 'r') as f:
    modules = f.read().strip().splitlines()

    print(modules)

    print(sum(list(map(fuel_count, map(lambda x: int(x), modules)))))
