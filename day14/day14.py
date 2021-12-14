from collections import defaultdict

fname = 'test-input.txt'
fname = 'input.txt'

with open(fname) as f:
    template, rules = f.read().rstrip().split('\n\n')
rules = [rule.split(' -> ') for rule in rules.split('\n')]
    
def step(pairs):
    new_pairs = pairs.copy()
    for rule in rules:
        if not pairs[rule[0]]:
            continue
        new_pairs[rule[0][0] + rule[1]   ] += pairs[rule[0]]
        new_pairs[rule[1]    + rule[0][1]] += pairs[rule[0]]
        new_pairs[rule[0]] -= pairs[rule[0]]
    return new_pairs

def solve(steps):
    pairs = defaultdict(int)
    for i in range(len(template) - 1):
        pairs[template[i : i + 2]] += 1
    for i in range(steps):
        pairs = step(pairs)
    elements = defaultdict(int)
    for (el1, el2), count in pairs.items():
        elements[el1] += count
    elements[template[-1]] += 1
    return max(elements.values()) - min(elements.values())

print('Part 1:', solve(10))
print('Part 2:', solve(40))
