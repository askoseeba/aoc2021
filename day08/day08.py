fname = 'test-input-0.txt'
fname = 'test-input.txt'
fname = 'input.txt'

with open (fname, 'r') as f:
    data = [[digits.split() for digits in line.split(' | ')] for line in f.read().rstrip().split('\n')]

print('Part 1:', sum([1 for line in list(zip(*data))[1] for digit in line if len(digit) in {2, 3, 4, 7}]))

def wires_to_digits(wirings):
    # As I ran out of free time during the Day 8, I decided to solve it next morning
    # by cheating a bit -- I got the conceptual idea spoiler of how to deduce all the
    # digits from the "easy four ones" from the solution provided by a person with
    # user name 'coriandor' here:
    # https://www.reddit.com/r/adventofcode/comments/rbj87a/2021_day_8_solutions/
    digits = {}
    digits[1] = next(filter(lambda wiring: len(wiring) == 2, wirings)) # Needed for 6
    digits[4] = next(filter(lambda wiring: len(wiring) == 4, wirings)) # Needed for 9
    digits[7] = next(filter(lambda wiring: len(wiring) == 3, wirings)) # Needed for 9
    digits[8] = next(filter(lambda wiring: len(wiring) == 7, wirings))
    digits[6] = next(filter(lambda wiring: len(wiring) == 6 and len(digits[1] - wiring) == 1, wirings))             # Needed for 0, 5
    digits[9] = next(filter(lambda wiring: len(wiring) == 6 and len(wiring - digits[4] - digits[7]) == 1, wirings)) # Needed for 0, 3
    digits[0] = next(filter(lambda wiring: len(wiring) == 6 and wiring not in {digits[6], digits[9]}, wirings))
    digits[5] = next(filter(lambda wiring: len(wiring) == 5 and len(digits[6] - wiring) == 1, wirings))         # Needed for 2, 3
    digits[3] = next(filter(lambda wiring: len(wiring) == 5 and wiring != digits[5] and len(wiring - digits[9]) == 0 and len(digits[9] - wiring) == 1, wirings)) # Needed for 2
    digits[2] = next(filter(lambda wiring: len(wiring) == 5 and wiring not in {digits[3], digits[5]}, wirings))
    
    return {wiring: digit  for digit, wiring in digits.items()}

outputs = []
for display in data:
    wirings = wires_to_digits([frozenset(wiring) for wiring in display[0]])
    outputs.append(int(''.join([str(wirings[frozenset(wiring)]) for wiring in display[1]])))

print('Part 2:', sum(outputs))
