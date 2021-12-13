import aocutils as aoc
import numpy as np

fname = 'test-input.txt'
fname = 'input.txt'

with open(fname) as f:
    data = f.read().rstrip().split('\n\n')

dots  = np.array([list(map(int, line.split(','))) for line in data[0].split('\n')])
folds = np.array([(line[0] != 'y', int(line[1])) for line in [line[11:].split('=') for line in data[1].split('\n')]])

def fold(paper, axis, line):
    half1 = paper[0 : line, :] if axis == 0 else paper[:, 0 : line]
    half2 = paper[line + 1 :, :] if axis == 0 else paper[:, line + 1 :]
    return half1 | np.flip(half2, axis)

x_dim, y_dim = dots[:, 0].max() + 1, dots[:, 1].max() + 1
y_dim = y_dim if y_dim % 2 == 1 else y_dim + 1 # fixes the issue with the live data
paper = np.zeros((y_dim, x_dim), dtype = int)
paper[dots[:, 1], dots[:, 0]] = 1

print('Part 1:', fold(paper, folds[0, 0], folds[0, 1]).sum())

for fld in folds:
    paper = fold(paper, fld[0], fld[1])

print('Part 2:')
aoc.print_2D(paper, {0: ' ', 1: '#'})
