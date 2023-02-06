import math


def iter_pi(epsilon):
    start = 1
    total = 1
    iterations = 1
    while abs((total - math.pi)) > epsilon:
        start = start / start + 2
        total += start
        start += 2
        iterations += 1
    return iterations


if __name__ == "__main__":
    print(iter_pi(0.1))
