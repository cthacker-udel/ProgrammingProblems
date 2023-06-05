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
