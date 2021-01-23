#Day 06

with open('./06.txt') as myinput:
    coords = myinput.readlines()

coords = {str(coords.index(coord)): tuple(map(int, (coord.strip().split(', ')))) for coord in coords}

x_range = sorted(coord[0] for coord in coords.values())
y_range = sorted(coord[1] for coord in coords.values())

def get_closest_point(x, y, coords):
    distances = sorted((abs(x - coord[0]) + abs(y - coord[1]), point) for point, coord in coords.items())
    return distances[0][1] if distances[0][0] != distances[1][0] else ''

grid = [[get_closest_point(x, y, coords) for x in range(x_range[0], x_range[-1] + 1)] for y in range(y_range[0], y_range[-1] + 1)]
points_closest_to_border = [line[0] for line in grid] + [line[-1] for line in grid] + grid[0] + grid[-1]
valid_points = [point for point in coords.keys() if point not in set(points_closest_to_border)]

#Part 1

print(max(sum(line.count(point) for line in grid) for point in valid_points))

#Part 2

def in_region(x, y, coords):
    distances = sum(abs(x - coord[0]) + abs(y - coord[1]) for coord in coords.values())
    return 1 if distances < 10000 else 0

safe_region = [[in_region(x, y, coords) for x in range(x_range[0], x_range[-1] + 1)] for y in range(y_range[0], y_range[-1] + 1)]

print(sum(map(sum, safe_region)))