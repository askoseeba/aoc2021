fname = 'test-input.txt'
fname = 'input.txt'

with open (fname, 'r') as f:
    data = [((row[0]), int(row[1])) for row in [row.split() for row in f.read().split('\n')[:-1]]]

#
# Part 1
#

forward = [row[1] for row in data if row[0] == 'forward']
down    = [row[1] if row[0] == 'down' else -int(row[1]) for row in data if row[0] in {'down', 'up'}]

print('Part 1: %d.' % (sum(forward) * (sum(down))))

#
# Part 2
#

forward, aim, down = 0, 0, 0
for row in data:
    if row[0] == 'down':
        aim += row[1]
    elif row[0] == 'up':
        aim -= row[1]
    else: # row[0] == 'forward'
        forward += row[1]
        down += aim * row[1]

print('Part 2: %d.' % (forward * down))
