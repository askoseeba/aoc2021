fname = 'test-input.txt'
fname = 'input.txt'

with open (fname, 'r') as f:
    data = [int(num) for num in f.read().rstrip().split(',')]

def fuel(distance):
    return int((distance + 1) * distance / 2)

print('Part 1:', min([sum([     abs(num - target)  for num in data]) for target in range(min(data), max(data) + 1)]))
print('Part 2:', min([sum([fuel(abs(num - target)) for num in data]) for target in range(min(data), max(data) + 1)]))
