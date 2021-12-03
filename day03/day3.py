fname = 'test-input.txt'
fname = 'input.txt'

import aocutils as aoc
import numpy as np

with open (fname, 'r') as f:
    data = np.array([[int(c) for c in list(row)] for row in f.read().split('\n')[:-1]])

#
# Part 1
#

gamma_rate   = aoc.bits_to_int((np.sum(data, axis = 0) > len(data) / 2).astype(int))
epsilon_rate = aoc.bits_to_int((np.sum(data, axis = 0) < len(data) / 2).astype(int))

print('Part 1: %d.' % (gamma_rate * epsilon_rate))

#
# Part 2
#

data_i = data
for i in range(data.shape[1]):
    most_common  = (np.sum(data_i, axis = 0) >= len(data_i) / 2).astype(int)
    data_i = data_i[data_i[:, i] == most_common[i]]
    if data_i.shape[0] == 1:
        break
ox_gen_rating = aoc.bits_to_int(data_i[0])

data_i = data
for i in range(data.shape[1]):
    least_common = (np.sum(data_i, axis = 0) < len(data_i) / 2).astype(int)
    data_i = data_i[data_i[:, i] == least_common[i]]
    if data_i.shape[0] == 1:
        break
co2_scrubber_rating = aoc.bits_to_int(data_i[0])

print('Part 2: %d.' % (ox_gen_rating * co2_scrubber_rating))
