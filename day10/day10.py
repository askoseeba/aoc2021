fname = 'test-input.txt'
fname = 'input.txt'

with open(fname) as f:
    data = f.read().rstrip().split('\n')

error_scores = {
    ')':     3,
    ']':    57,
    '}':  1197,
    '>': 25137
}

ac_scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

required_endings = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

def _score(required_ending, line):
    ac_score = 0
    while len(line):
        if line[0] == required_ending:
            return 0, 0, line[1:]
        if line[0] in required_endings.values():
            return error_scores[line[0]], 0, line[1:]
        err_score, ac_score, line = _score(required_endings[line[0]], line[1:])
        if err_score:
            return err_score, 0, line
    return 0, 5 * ac_score + ac_scores[required_ending], line

def score(line):
    err_score, ac_score, line = _score(required_endings[line[0]], line[1:])
    if err_score or ac_score:
        return err_score, ac_score, line
    elif len(line):
        return score(line)
    return 0, 0, 0

scores = [score(line) for line in data]
print('Part 1:', sum([score[0] for score in scores]))
ac = [score[1] for score in scores if score[1]]
ac.sort()
print('Part 2:', ac[int(len(ac) / 2)])
