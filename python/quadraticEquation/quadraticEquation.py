import math

"""
    Generates the root value from the quadratic equation given a, b, and c

    @param a - A in the quadratic equation
    @param b - B in the quadratic equation
    @param c - C in the quadratic equation
    @returns The root of the quadratic equation given a, b, and c

"""


def quadraticEquation(a, b, c):
    upper_half = (-1 * b) + math.sqrt((b * b) - 4 * a * c)
    lower_half = 2 * a
    return upper_half / lower_half
