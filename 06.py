#Day 06

with open('./06.txt') as myinput:
    coords_list = myinput.readlines()

coords = {str(i): tuple(map(int, (coord.strip().split(', ')))) for i, coord in enumerate(coords_list)}

x_coords = sorted(coord[0] for coord in coords.values())
y_coords = sorted(coord[1] for coord in coords.values())

x_range = [x for x in range(x_coords[0], x_coords[-1] + 1)]
y_range = [y for y in range(y_coords[0], y_coords[-1] + 1)]

def get_closest_point(x, y, coords):
    (distance_1, point_1), (distance_2, point_2) = (sorted((abs(x - xc) + abs(y - yc), point) for point, (xc, yc) in coords.items())[i] for i in range(2))
    return point_1 if distance_1 != distance_2 else ''

grid = [[get_closest_point(x, y, coords) for x in x_range] for y in y_range]

points_closest_to_border = [line[0] for line in grid] + [line[-1] for line in grid] + grid[0] + grid[-1]

valid_points = [point for point in coords.keys() if point not in set(points_closest_to_border)]

#Part 1

print(max(sum(line.count(point) for line in grid) for point in valid_points))

#Part 2

def in_region(x, y, coords):
    distances = sum(abs(x - xc) + abs(y - yc) for (xc, yc) in coords.values())
    return distances < 10000

safe_region = [[in_region(x, y, coords) for x in x_range] for y in y_range]

print(sum(map(sum, safe_region)))
