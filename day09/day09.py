fname = 'test-input.txt'
fname = 'input.txt'

import aocutils as aoc
import sys

data = aoc.load_2D_imag(fname, padding_symbol = '9', symbols_to_int = True)
size = aoc.size_2D_imag(data)

lows = []
for y in range(1, size[1] - 1):
    for x in range(1, size[0] - 1):
        if not len(aoc.neighbours_2D_imag(x + y * 1j, data, is_NESW = True, compare_fun = lambda num, neighbour: neighbour <= num)):
            lows.append(data[x + y * 1j])

print('Part 1:', sum(lows) + len(lows))
sys.stdout.flush()

import itertools

basin_parts = {x + y * 1j for x in range(1, size[0] - 1) for y in range(1, size[1] - 1) if data[x + y * 1j] < 9}
neighbours  = {frozenset(pair) for pair in filter(lambda pair: aoc.is_neighbour_2D_NESW_imag(*pair), itertools.product(basin_parts, basin_parts))}

prev_len, cur_len = -1, len(neighbours)
while prev_len != cur_len:
    print('D:', cur_len)
    new_neighbours = set()
    while neighbours:
        start_group      = neighbours.pop()
        neighbour_groups = {group for group in neighbours if len(start_group & group)}
        new_neighbours.add(frozenset.union(start_group, *neighbour_groups))
        neighbours       = neighbours - neighbour_groups
    neighbours = new_neighbours.copy()
    prev_len, cur_len = cur_len, len(neighbours)

basin_sizes = list(map(len, neighbours))
basin_sizes.sort()

print('Part 2:', basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])
