import numpy as np

fname = 'test-input-1.txt'
fname = 'test-input-2.txt'
fname = 'test-input-3.txt'
fname = 'input.txt'

with open(fname) as f:
    data = [sum([[1 if line[0] == 'on' else 0], sum([list(map(int, cuboid[2:].split('..')))
                                                     for cuboid in line[1].split(',')], [])], [])
            for line in [line.split(' ') for line in f.read().rstrip().split('\n')]]

#
# Part 1 -- quick brute force with numpy
#

small_cuboids = [cuboid for cuboid in data if cuboid[1] >= -50 and cuboid[2] <= 50 and cuboid[3] >= -50 and cuboid[4] <= 50 and cuboid[5] >= -50 and cuboid[6] <= 50]

small_cuboids_u = list(zip(*small_cuboids))
x_min, x_max = min(small_cuboids_u[1]), max(small_cuboids_u[2])
y_min, y_max = min(small_cuboids_u[3]), max(small_cuboids_u[4])
z_min, z_max = min(small_cuboids_u[5]), max(small_cuboids_u[6])

core = np.zeros((z_max - z_min + 1, y_max - y_min + 1, x_max - x_min + 1), dtype = int)
for cuboid in small_cuboids:
    core[cuboid[5] - z_min : cuboid[6] - z_min + 1,
         cuboid[3] - y_min : cuboid[4] - y_min + 1,
         cuboid[1] - x_min : cuboid[2] - x_min + 1] = cuboid[0]
x_min, x_max, y_min, y_max, z_min, z_max

print('Part 1:', np.sum(core))

#
# Part 2 -- execution time 3.7 seconds.
#

def segment_overlap(seg1, seg2):
    start, stop = max(seg1[0], seg2[0]), min(seg1[1], seg2[1])
    return [start, stop] if start <= stop else None

def cuboid_overlap(cub1, cub2, overlap_on):
    olx = segment_overlap(cub1[1:3], cub2[1:3])
    oly = segment_overlap(cub1[3:5], cub2[3:5])
    olz = segment_overlap(cub1[5:],  cub2[5:])
    return [overlap_on] + olx + oly + olz if olx and oly and olz else None

def slice_cuboid(cuboid, overlap):
    slices = []
    if cuboid[1] < overlap[1]: # Lower x
        slices.append([cuboid[0], cuboid[1],      overlap[1] - 1, cuboid[3],      cuboid[4],      cuboid[5],      cuboid[6]])
        cuboid[1] = overlap[1]
    if cuboid[2] > overlap[1]: # Upper x
        slices.append([cuboid[0], overlap[2] + 1, cuboid[2],      cuboid[3],      cuboid[4],      cuboid[5],      cuboid[6]])
        cuboid[2] = overlap[2]
    if cuboid[3] < overlap[3]: # Lower y
        slices.append([cuboid[0], cuboid[1],      cuboid[2],      cuboid[3],      overlap[3] - 1, cuboid[5],      cuboid[6]])
        cuboid[3] = overlap[3]
    if cuboid[4] > overlap[4]: # Upper y
        slices.append([cuboid[0], cuboid[1],      cuboid[2],      overlap[4] + 1, cuboid[4],      cuboid[5],      cuboid[6]])
        cuboid[4] = overlap[4]
    if cuboid[5] < overlap[5]: # Lower z
        slices.append([cuboid[0], cuboid[1],      cuboid[2],      cuboid[3],      cuboid[4],      cuboid[5],      overlap[5] - 1])
        cuboid[5] = overlap[5]
    if cuboid[6] > overlap[6]: # Upper z
        slices.append([cuboid[0], cuboid[1],      cuboid[2],      cuboid[3],      cuboid[4],      overlap[6] + 1, cuboid[6]])
        cuboid[6] = overlap[6]
    return slices

def volume(cuboid):
    return (cuboid[2] - cuboid[1] + 1) * (cuboid[4] - cuboid[3] + 1) * (cuboid[6] - cuboid[5] + 1)

cuboids = []
for new_cuboid in data:
    new_cuboids = []
    for cuboid in cuboids:
        olc = cuboid_overlap(new_cuboid, cuboid, new_cuboid[0])
        if olc:
            new_cuboids += slice_cuboid(cuboid, olc)
        else:
            new_cuboids.append(cuboid)
    cuboids = new_cuboids
    cuboids.append(new_cuboid)

print('Part 2:', sum([volume(cuboid) for cuboid in cuboids if cuboid[0]]))
