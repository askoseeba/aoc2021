fname = 'test-input.txt'
fname = 'input.txt'

with open (fname, 'r') as f:
    data = [int(num) for num in f.read().split('\n')[:-1]]

#
# Part 1
#

increased = 0
for i in range(1, len(data)):
    if data[i] > data[i - 1]:
        increased += 1
print('Increased %d times.' % increased)

#
# Part 2
#

increased = 0
for i in range(4, len(data) + 1):
    if sum(data[i - 4 : i - 1]) < sum(data[i - 3 : i]):
        increased += 1
print('Increased %d times.' % increased)
