import aocutils as aoc
import numpy as np

fname = 'test-input.txt'
fname = 'input.txt'

with open(fname) as f:
    data = f.read().rstrip().split('\n\n')

alg = data[0]

def pixel(image, alg, x, y):
    slice = image[y - 1 : y + 2, x - 1 : x + 2]
    return alg[aoc.bits_to_int((slice == '#').astype(int).flatten())]

def enhance(count):
    image = np.array(aoc.load_2D(fname = None, input_str = data[1], padding_symbol = '.', padding_width = count + 1))
    size = aoc.size_2D(image)
    for i in range(count):
        infinity = '.' if alg[0] == '.' or i % 2 == 1 else '#'
        new_image = np.full_like(image, infinity)
        x_start, x_stop, y_start, y_stop = count - i, size[0] - (count - i), count - i, size[1] - (count - i)
        for y in range(x_start, x_stop):
            for x in range(y_start, y_stop):
                new_image[y, x] = pixel(image, alg, x, y)
        image = new_image
    return image

print('Part 1:', np.sum(enhance(2) == '#'))
print('Part 2:', np.sum(enhance(50) == '#'))
