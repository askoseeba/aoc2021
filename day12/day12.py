#fname = 'test-input-1.txt'
#fname = 'test-input-2.txt'
#fname = 'test-input-3.txt'
fname = 'input.txt'

with open(fname) as f:
    data = [frozenset(line.split('-')) for line in f.read().rstrip().split('\n')]

def map_paths(current_cave, current_path, small_twice_allowed = False, small_twice_used = False):
    if current_cave == 'end':
        new_complete = current_path.copy()
        new_complete.append(current_cave)
        complete_paths.append(new_complete)
        return
    if current_cave == 'start' and current_cave in current_path:
        return
    if current_cave.islower() and current_cave in current_path:
        if small_twice_used or not small_twice_allowed:
            return
        small_twice_used = True
    new_current_path = current_path.copy()
    new_current_path.append(current_cave)
    neighbours = {set(pair - {current_cave}).pop() for pair in data if current_cave in pair}
    for neighbour in neighbours:
        map_paths(neighbour, new_current_path, small_twice_allowed, small_twice_used)

complete_paths = []
map_paths('start', [])
print('Part 1:', len(complete_paths))
import sys
sys.stdout.flush()

complete_paths = []
map_paths('start', [], True)
print('Part 2:', len(complete_paths))
