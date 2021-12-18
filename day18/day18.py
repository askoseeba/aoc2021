from functools import reduce
import itertools
import math
import re

def add(left, right):
    added =  '[' + left + ',' + right + ']'
    reduce = True
    while reduce:
        exploded = explode(added)
        if exploded != added:
            added = exploded
            continue
        splitted = split(added)
        if splitted != added:
            added = splitted
            continue
        reduce = False
    return added

def explode(data):
    r = re.compile(r'(\[\d+,\d+\])')
    found = False
    for m_pair in r.finditer(data):
        if data[:m_pair.span()[0]].count('[') - data[:m_pair.span()[0]].count(']') >= 4:
            found = True
            break
    if not found:
        return data
    pair, span = eval(m_pair.group(1)), m_pair.span(1)
    m_left = re.search(r'^.*[\[,](\d+)', data[:span[0]])
    if m_left:
        left_span = m_left.span(1)
        left_data = data[:left_span[0]] + str(int(m_left.group(1)) + int(pair[0])) + data[left_span[1] : span[0]]
    else:
        left_data = data[:span[0]]
    m_right = re.search(r'^.*?(\d+)', data[span[1]:])
    if m_right:
        right_span = m_right.span(1)
        right_data = data[span[1] : span[1] + right_span[0]] + str(int(m_right.group(1)) + int(pair[1])) + data[span[1] + right_span[1]:]
    else:
        right_data = data[span[1]:]
    return left_data + '0' + right_data

def split(data):
    m_num = re.search(r'^.*?(\d\d+)', data)
    if not m_num:
        return data
    num, span = int(m_num.group(1)), m_num.span(1)
    pair = math.floor(num / 2), math.ceil(num / 2)
    return data[:span[0]] + '[%d,%d]' % (math.floor(num / 2), math.ceil(num / 2)) + data[span[1]:]

def magnitude(data):
    left  = data[0] if type(data[0]) == int else magnitude(data[0])
    right = data[1] if type(data[1]) == int else magnitude(data[1])
    return 3 * left + 2 * right

def max_pairwise_magnitude(data):
    pairs = filter(lambda pair: pair[0] != pair[1], itertools.product(data,data))
    #for pair in pairs:
    #    print(magnitude(eval(add(pair[0], pair[1]))))
    #return 0
    return max([magnitude(eval(add(pair[0], pair[1]))) for pair in pairs])

fname = 'test-input-1.txt'
fname = 'test-input-2.txt'
fname = 'test-input-3.txt'
fname = 'input.txt'

with open(fname) as f:
    data = f.read().rstrip().split('\n')

added = reduce(add, data)

print('Part 1:', magnitude(eval(added)))
print('Part 2:', max_pairwise_magnitude(data))
