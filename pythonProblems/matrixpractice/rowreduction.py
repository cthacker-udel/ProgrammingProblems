mat1 = [[5, 1], [4, -3]]
mat2 = [[1, 0.2], [0, 1]]

# x + y = 4
# -6x + 2y = 16


# x -2y/6 = 16


# x - y/3 = 16/-6

# x - y/3 = -2.6

# x -1/3y = -26

#     x - y = -26/3
# -   x - y = -4
# ---------------------


#       -2y = -12/3 + 26/3
#       -2y = -38/3
#         y = 6.3

# x + 6.3 = 4
# x = -2.3


mat1 = [[4, -3], [7, -8]]

dt_1 = mat1[0][0] * mat1[1][1]
dt_2 = mat1[0][1] * mat1[1][0]

dt_one = dt_1 - dt_2

print(dt_one)


mat1 = [[-3, -8, 1], [2, 2, -1], [-5, 6, 2]]

dt_1_1 = mat1[0][0] * mat1[1][1] * mat1[2][2]
dt_1_2 = mat1[0][1] * mat1[1][2] * mat1[2][0]
dt_1_3 = mat1[0][2] * mat1[1][0] * mat1[2][1]

dt_anti_1 = mat1[0][2] * mat1[1][1] * mat1[2][0]
dt_anti_2 = mat1[0][1] * mat1[1][0] * mat1[2][2]
dt_anti_3 = mat1[0][0] * mat1[1][2] * mat1[2][1]

dt_1_full = dt_1_1 * dt_1_2 * dt_1_3
dt_1_anti_full = dt_anti_1 * dt_anti_2 * dt_anti_3

print(dt_1_full - dt_1_anti_full)

# [[1, 1], [2, 3]]

# a + 2b + z = 260


# a/2 + b + z/2 = 130


# x + y = 4
# -6x + 2y = 16

# x + y = 4
# x + -1/3y = 16/-6

# x + -1/3y = -2.6
# - x + y = 4


# -4/3y = -6.6
# y = 5.0

# x + 5 = 4
# x = -1


# x + 2x + z = 3x + z = 10000

# z = 10000 - 3x

# 0.02(2x) + 0.03(x) + 0.04(z) = 0.04x + 0.03x + 0.04z = 0.07x + 0.04z

# # total interest earned is 260

# 0.07x + 0.04z = 260

# 3x + z = 10000
# 0.07x + 0.04z = 260


# multiply second by 3
# 0.21x + 0.12z = 780

# subtract second from first


#   3x + z = 10000
# - 0.21x - 0.12z = -780

# 2.79x + 0.12z

# mat1 = [[5, 1], [-1, 3]]

# dt_1 = mat1[0][0] * mat1[1][1]
# dt_2 = mat1[0][1] * mat1[1][0]


# print(dt_1 - dt_2)


# mat1 = [[2, -1], [-6, 3]]

# dt_1 = mat1[0][0] * mat1[1][1]
# dt_2 = mat1[0][1] * mat1[1][0]

# print(dt_1 - dt_2)


# mat1 = [[7, 5, 3], [3, 2, 5], [1, 2, 1]]

# dt_1_first = mat1[0][0] * mat1[1][1] * mat1[2][2]
# dt_1_second = mat1[0][1] * mat1[1][2] * mat1[2][0]
# dt_1_third = mat1[0][2] * mat1[1][0] * mat1[2][1]

# dt_anti_1_first = mat1[0][2] * mat1[1][1] * mat1[2][0]
# dt_anti_1_second = mat1[0][1] * mat1[1][0] * mat1[2][2]
# dt_anti_1_third = mat1[0][0] * mat1[1][2] * mat1[2][1]

# dt_1_front = dt_1_first + dt_1_second + dt_1_third
# dt_1_anti = dt_anti_1_first + dt_anti_1_second + dt_anti_1_third

# print(dt_1_front - dt_1_anti)


# 7f + 5a + 3c = 120
# 3f + 2a + 5c = 70
# f + 2a + c = 20

# [[3, 1], [1, 2]] # [[a, b], [c, d]] with the identity matrix [[1, 0], [0, 1]] (which returns the same matrix)

# [[3, 1]] * [[a, c]]
# [[3, 1]] * [[b, d]]
# [[1, 2]] * [[a, c]]
# [[1, 2]] * [[b, d]]


# 3a + 1c = 1
# 3b + 1d = 0
# 1a + 2c = 0
# 1b + 2d = 1


# [[5, 2], [1, 2]] # [[a, b], [c, d]] with the identity matrix [[1, 0], [0, 1]]

# [5, 2] * [a, c]
# [5, 2] * [b, d]
# [1, 2] * [a, c]
# [1, 2] * [b, d]


# 5a + 2c = 1 # a + 2/5c = 1/5

# 5b + 2d = 0 # b + 2/5d = 0
# 1a + 2c = 0
# 1b + 2d = 1


#   a + 2c = 0
# - a + 2/5c = 1/5
# ------------------
#     10/5 - 2/5c = -1/5
#     8/5c = -1/5


# c = (-1/5) * (5/8)
# c = -5/40

# c = -1/8 ## found it

# 5a + 2(-1/8) = 1
# 5a + -2/8 = 1
# 5a = 1 + 2/8
# 5a = 10/8
# 5a = 5/4
# a = 5/4 * (1/5)
# a = 5/20

# a = 1/4 ## found it


#   b + 2d =   1
# - b + 2/5d = 0
# ----------------

#     10/5 - 2/5d = 1
# --------------------
#     8/5d = 1

# d = 5/8 ## found it


# 5b + 2(5/8) = 0
# 5b + 10/8 = 0
# 5b = -10/8
# b = -10/8 * 1/5
# b = -10/40
# b = -1/4


# [[1, 1], [2, 2]]  # [[a, b], [c, d]] ## [[1, 0], [0, 1]]


# [1, 1] * [a, c] = 1
# [1, 1] * [b, d] = 0
# [2, 2] * [a, c] = 0
# [2, 2] * [b, d] = 1


# 1a + 1c = 1
# 1b + 1d = 0
# 2a + 2c = 0
# 2b + 2d = 1


#    a + c = 0
# -  a + c = 1
# -------------------------
#     Impossible to solve
