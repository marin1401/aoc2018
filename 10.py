#Day 10

with open('./10.txt') as my_input:
    input_lines = my_input.read().replace(' ', '').splitlines()

positions, velocities = [[tuple(map(int, line.split('>')[i][10:].split(',')))
                          for line in input_lines] for i in range(2)]

def message(step, second, appeared):
    min_y, *_, max_y = sorted(y for x, y in step)
    if max_y - min_y < 10:
        min_x, *_, max_x = sorted(x for x, y in step)
        #Part 1
        for y in range(min_y, max_y + 1):
            message_row = ''
            for x in range(min_x, max_x + 1):
                message_row += '#' if (x, y) in step else ' '
            print(message_row)
        #Part 2
        print(second)
        return True

second = 0
appeared = False
while not appeared:
    positions = [(x + vx, y + vy)
                 for (x, y), (vx, vy) in zip(positions, velocities)]
    second += 1
    appeared = message(positions, second, appeared)
