#fname = 'test-input-0.txt'
#fname = 'test-input.txt'
fname = 'input.txt'

import aocutils as aoc
from collections import defaultdict

cavern = aoc.load_2D_imag(fname, symbols_to_int = True)

def energy_up(locs):
    for loc in locs:
        if flashed[loc]:
            continue
        cavern[loc] += 1
        if cavern[loc] == 10:
            flashed[loc] = True
            energy_up(aoc.neighbours_2D_imag(loc, cavern))
            cavern[loc] = 0

flash_count      = 0
all_flashed_step = 0
step             = 0
while not all_flashed_step or step <= 100:
    flashed = defaultdict(bool)
    step   += 1
    energy_up(cavern.keys())
    new_flashes = sum(flashed.values())
    if step <= 100:
        flash_count += new_flashes
    if not sum(cavern.values()):
        all_flashed_step = step
        
print('Part 1:', flash_count)
print('Part 2:', all_flashed_step)
