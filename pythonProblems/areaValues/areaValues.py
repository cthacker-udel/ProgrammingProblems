import math


def calculate_point_diff(pt1, pt2):
    print('[[  {} and {} ]]'.format(pt1, pt2))
    pt1x = pt1[0]
    pt1y = pt1[1]
    pt2x = pt2[0]
    pt2y = pt2[1]
    return math.sqrt((pt2x - pt1x)**2 + (pt2y - pt1y)**2)


def triangle_area(base, height):
    return (base * height) / 2


def area_value(n):
    if n <= 1:
        return 0
    else:
        points = []
        points_ind = 0
        distances = []  # [(height, base)]
        for i in range(1, (n // 2) + 1):
            if n % i == 0:
                points.append((i, n // i))
                if len(points) > 1:
                    distances.append((
                        calculate_point_diff(
                            points[points_ind], points[points_ind + 1]),
                        calculate_point_diff((
                            points[points_ind][0], points[points_ind + 1][1]), points[points_ind + 1])
                    ))
                    points_ind += 1
        print(distances)
        areas = [triangle_area(x[1], x[0]) for x in distances]
        print(areas)


if __name__ == '__main__':
    print(area_value(12))
