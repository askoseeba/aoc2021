import functools
import itertools

# Test data
positions = [4, 8]
# Live data
positions = [6, 9]

#
# Part 1
#

class DeterministicDice:
    def __init__(self):
        self._rolled = 0
        self._state  = 0
    
    def roll(self):
        self._rolled += 1
        self._state   = self._state % 100 + 1
        return self._state
    
def move(start, steps):
    return (start - 1 + steps) % 10 + 1

dice = DeterministicDice()
p1_score = p2_score = 0
_positions = positions.copy()
while True:
    _positions[0] = move(_positions[0], dice.roll() + dice.roll() + dice.roll())
    p1_score     += _positions[0]
    if p1_score >= 1000:
        break
    _positions[1] = move(_positions[1], dice.roll() + dice.roll() + dice.roll())
    p2_score     += _positions[1]
    if p2_score >= 1000:
        break

looser_score = p1_score if p1_score <= p2_score else p2_score
print('Part 1:', looser_score * dice._rolled)

#
# Part 2
#

@functools.lru_cache(maxsize = None)
def quantum_dice(p1_pos, p2_pos, p1_score, p2_score, player):
    _wins      = [0, 0]
    for universe in itertools.product([1, 2, 3], [1, 2, 3], [1, 2, 3]):
        _positions         = [p1_pos,   p2_pos]
        _scores            = [p1_score, p2_score]
        _positions[player] = move(_positions[player], sum(universe))
        _scores[player]   += _positions[player]
        if _scores[player] >= 21:
            _wins[player] += 1
        else:
            _wins_added = quantum_dice(_positions[0], _positions[1], _scores[0], _scores[1], int(not player))
            _wins[0] += _wins_added[0]
            _wins[1] += _wins_added[1]
    return _wins[0], _wins[1]

p1_score = p2_score = 0
print('Part 2:', max(quantum_dice(positions[0], positions[1], 0, 0, 0)))
