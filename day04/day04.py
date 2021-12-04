import numpy as np

fname = 'test-input.txt'
fname = 'input.txt'

with open (fname, 'r') as f:
    data = f.read().rstrip().split('\n\n')

draw   = np.array([int(num) for num in data[0].split(',')])
boards = np.array([[[int(num) for num in line.split()] for line in board.split('\n')] for board in data[1:]])

#
# Part 1
#

def check_board(board_marks, i):
    return np.sum(np.sum(board_marks[i], axis = 0) == 5) + np.sum(np.sum(board_marks[i], axis = 1) == 5)

board_marks = np.isin(boards, draw[0:5])
found       = False
for num in draw[5:]:
    board_marks = (board_marks | (boards == num))
    for i in range(len(boards)):
        if check_board(board_marks, i):
            found = True
            break
    if found:
        break

print('Part 1:', np.sum(boards[i][~board_marks[i]]) * num)

#
# Part 2
#

board_marks = np.isin(boards, draw[0:5])
won_boards  = []
for num in draw[5:]:
    board_marks = (board_marks | (boards == num))
    for i in range(len(boards)):
        if i in won_boards:
            continue
        if check_board(board_marks, i):
            won_boards.append(i)
    if len(won_boards) == len(boards):
        break

print('Part 2:', np.sum(boards[won_boards[-1]][~board_marks[won_boards[-1]]]) * num)
