fname = 'test-input.txt'
fname = 'input.txt'

with open (fname, 'r') as f:
    data = [int(num) for num in f.read().rstrip().split(',')]

def populate(data, days):
    population = [data.count(i) for i in range(9)]
    for i in range(days):
        population = [population[0] + population[7] if i == 6 else population[0] if i == 8 else population[i + 1] for i in range(9)]
    return population

print('Part 1:', sum(populate(data, 80)))
print('Part 2:', sum(populate(data, 256)))
