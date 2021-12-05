import numpy as np

fname = 'test-input.txt'
fname = 'input.txt'

with open (fname, 'r') as f:
    data = np.array([np.concatenate([[int(coord) for coord in point.split(',')] for point in line.split(' -> ')]) for line in f.read().rstrip().split('\n')])

#
# Part 1
#

data1    = data[(data[:, 0] == data[:, 2]) | (data[:, 1] == data[:, 3])]
max_x    = max(max(data1[:, 0]), max(data1[:, 2]))
max_y    = max(max(data1[:, 1]), max(data1[:, 3]))
vent_map = np.zeros((max_y + 1, max_x + 1), dtype = int)

for segment in data1:
    start_x, end_x = (segment[0], segment[2]) if segment[2] > segment[0] else (segment[2], segment[0])
    start_y, end_y = (segment[1], segment[3]) if segment[3] > segment[1] else (segment[3], segment[1])
    vent_map[start_y : end_y + 1, start_x : end_x + 1] += 1
    
print('Part 1:', len(vent_map[vent_map >= 2]))

#
# Part 2
#

data2    = data
max_x    = max(max(data2[:, 0]), max(data2[:, 2]))
max_y    = max(max(data2[:, 1]), max(data2[:, 3]))
vent_map = np.zeros((max_y + 1, max_x + 1), dtype = int)

for segment in data2:
    start_x, end_x = (segment[0], segment[2]) if segment[2] > segment[0] else (segment[2], segment[0])
    start_y, end_y = (segment[1], segment[3]) if segment[3] > segment[1] else (segment[3], segment[1])
    dx, dy         = segment[2] - segment[0], segment[3] - segment[1]
    if abs(dx) != abs(dy): # It is either horizontal or vertical segment
        vent_map[start_y : end_y + 1, start_x : end_x + 1] += 1
        continue
    diagonal = np.identity(end_x - start_x + 1, dtype = int)
    if dx != dy: # It is anti diagonal segment
        diagonal = np.fliplr(diagonal)
    vent_map[start_y : end_y + 1, start_x : end_x + 1] += diagonal
    
print('Part 2:', len(vent_map[vent_map >= 2]))
