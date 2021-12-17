x_min, x_max, y_min, y_max =  20,  30,  -10,  -5  # Test data
x_min, x_max, y_min, y_max = 185, 221, -122, -74  # Live data

max_height = sum([ys for ys in range(abs(y_min))])
print('Part 1:', max_height)

def test_speed(speed_x, speed_y):
    cur_x, cur_y = 0, 0
    while cur_x <= x_max and y_min <= cur_y <= max_height:
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

print('Part 2:', sum([1 for x in range(x_max + 1) for y in range(y_min, abs(y_min) + 1) if test_speed(x, y)]))
