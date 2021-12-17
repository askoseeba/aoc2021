x_min, x_max, y_min, y_max =  20,  30,  -10,  -5  # Test data
x_min, x_max, y_min, y_max = 185, 221, -122, -74  # Live data

height, y_speed = 0, abs(y_min)
for ys in range(y_speed):
    height += ys

print('Part 1:', height)

def test_speed(speed_x, speed_y):
    cur_x, cur_y = 0, 0
    while cur_x <= x_max and y_min <= cur_y <= height:
        if speed_x == 0 and cur_x < x_min:
            return False
        if x_min <= cur_x <= x_max and y_min <= cur_y <= y_max:
            return True
        if speed_x:
            cur_x   += speed_x
            speed_x -= 1
        cur_y   += speed_y
        speed_y -= 1
    return False

speed_count = 0
for x in range(x_max + 1):
    for y in range(y_min, abs(y_min) + 1):
        if test_speed(x, y):
            speed_count += 1

print('Part 2:', speed_count)
