import numpy as np

mat1 = [[1, 1], [2, 2]]
mat2 = [[1, 1], [1, 2]]

first_frac = mat1[0][0] / mat1[1][0]
second_frac = mat1[0][1] / mat1[1][1]

print(first_frac, second_frac)

twofirst = mat2[0][0] / mat2[1][0]
twosecond = mat2[0][1] / mat2[1][1]

print(twofirst, twosecond)

ff1 = mat1[0][0] * mat1[1][1]
ff2 = mat1[0][1] * mat1[1][0]

print(ff1, ff2, ff1 - ff2)

ff11 = mat2[0][0] * mat2[1][1]
ff22 = mat2[1][0] * mat2[0][1]

print(ff11, ff22, ff11 - ff22)


mat3 = [[5, 1], [-1, 3]]


first3 = mat3[0][0] * mat3[1][1]
second3 = mat3[0][1] * mat3[1][0]

print(first3, second3, first3 - second3)  ## singular

mat4 = [[2, -1], [-6, 3]]

first4 = mat4[0][0] * mat4[1][1]
second4 = mat4[0][1] * mat4[1][0]

print(first4, second4, first4 - second4)

mat5 = [[2, 3], [2, 4]]

first5 = mat5[0][0] * mat5[1][1]
second5 = mat5[0][1] * mat5[1][0]

print(first5, second5, first5 - second5)

mat1 = [[1, 0, 1], [0, 1, 0], [3, 3, 3]]

dt_1_first_diag = mat1[0][0] * mat1[1][1] * mat1[2][2]
dt_1_second_diag = mat1[0][1] * mat1[1][2] * mat1[2][0]
dt_1_third_diag = mat1[0][2] * mat1[1][0] * mat1[2][1]

dt_1_anti_first_diag = mat1[0][2] * mat1[1][1] * mat1[2][0]
dt_1_anti_second_diag = mat1[0][1] * mat1[1][0] * mat1[2][2]
dt_1_anti_third_diag = mat1[0][0] * mat1[1][2] * mat1[2][1]

dt_1 = (dt_1_first_diag + dt_1_second_diag + dt_1_third_diag) - (
    dt_1_anti_first_diag - dt_1_anti_second_diag - dt_1_anti_third_diag
)

print(dt_1)


mat2 = [[1, 1, 1], [1, 1, 2], [0, 0, -1]]


dt_2_first_diag = mat2[0][0] * mat2[1][1] * mat2[2][2]
dt_2_second_diag = mat2[0][1] * mat2[1][2] * mat2[2][0]
dt_2_third_diag = mat2[0][2] * mat2[1][0] * mat2[2][1]

dt_2_anti_first_diag = mat2[0][2] * mat2[1][1] * mat2[2][0]
dt_2_anti_second_diag = mat2[0][1] * mat2[1][0] * mat2[2][2]
dt_2_anti_third_diag = mat2[0][0] * mat2[1][2] * mat2[2][1]

dt_2 = (dt_2_first_diag + dt_2_second_diag + dt_2_third_diag) + (
    dt_2_anti_first_diag - dt_2_anti_second_diag - dt_2_anti_third_diag
)

print(dt_2)


mat3 = [[1, 1, 1], [0, 2, 2], [0, 0, 3]]

dt_3_first_diag = mat3[0][0] * mat3[1][1] * mat3[2][2]
dt_3_second_diag = mat3[0][1] * mat3[1][2] * mat3[2][0]
dt_3_third_diag = mat3[0][2] * mat3[1][0] * mat3[2][1]

dt_3_anti_first_diag = mat3[0][2] * mat3[1][1] * mat3[2][0]
dt_3_anti_second_diag = mat3[0][1] * mat3[1][0] * mat3[2][2]
dt_3_anti_third_diag = mat3[0][0] * mat3[1][2] * mat3[2][1]

dt_3_first = dt_3_first_diag + dt_3_second_diag + dt_3_third_diag
dt_3_second = dt_3_anti_first_diag - dt_3_anti_second_diag - dt_3_anti_third_diag

dt_3 = dt_3_first + dt_3_second

print(dt_3)

mat4 = [[1, 2, 5], [0, 3, -2], [2, 4, 10]]

dt_4_first_diag = mat4[0][0] * mat4[1][1] * mat4[2][2]
dt_4_second_diag = mat4[0][1] * mat4[1][2] * mat4[2][0]
dt_4_third_diag = mat4[0][2] * mat4[1][0] * mat4[2][1]

dt_4_anti_first_diag = mat4[0][2] * mat4[1][1] * mat4[2][0]
dt_4_anti_second_diag = mat4[0][1] * mat4[1][0] * mat4[2][2]
dt_4_anti_third_diag = mat4[0][0] * mat4[1][2] * mat4[2][1]

print(
    "first = {} {} {} second = {} {} {}".format(
        dt_4_first_diag,
        dt_4_second_diag,
        dt_4_third_diag,
        dt_4_anti_first_diag,
        dt_4_anti_second_diag,
        dt_4_anti_third_diag,
    )
)

dt_4_first = dt_4_first_diag + dt_4_second_diag + dt_4_third_diag
dt_4_second = dt_4_anti_first_diag + dt_4_anti_second_diag + dt_4_anti_third_diag

dt_4 = dt_4_first - dt_4_second

print("dt4 = {}".format(dt_4))


# 4a + 3b = 6
# 1a - 5b = 8

# a = 0 b = 2

# Solution is non-singular, as the second row cannot be replicated from the first row,
# so therefore, the first row is linearly independent.

# 4a + 3b + 1c = 6
# 1a - 5b + 7c = 8
# 5a - 2b + 8c = 14

# 4a + 3b + 1c
# 1a - 5b + 7c


# 5a + - 2b + 8c

# Since row 3 can be replicated from row 1 by adding them together, the
# system is singular, and is redundant, therefore the third row
# is linearly dependant


# divide by coefficient of a
# 5a + b = 17
# 4a - 3b = 6

# Dividing first equation by 5 and second one by 4 gives us

# a + b/5 = 3.4
# a - 0.75b = 1.5

# subtract first equation from the second one to remove a

#   a - 0.75b = 1.5
# - a + 0.2b  = 3.4

#   0a - 0.95b = -1.9 # Divide by -0.95 on both sides to get
#   b = 2

# to find A
# a + 0.2(2) = 3.4
# a + 0.4 = 3.4
# a = 3


# 2a + 5b = 46
# 8a + b = 32

# Eliminate a from the equation

# Divide by coefficient of a
# a + 2.5b = 23
# a + .125b = 4

# Subtract first from second

#    a + .125b = 4
# -  a + 2.5b = 23
#      - 2.375b = -19
#     b = 8.0


# a + 2.5(8) = 23
# a + 20 = 23
# a = 3

# 5a + b = 11
# 10a + 2b = 22


# a + b/5 = 2.2
# a + b/5 = 2.2


# a = x
# b = (2.2 - x) / 5

# a  +  b  +   2c = 12
# 3a - 3b - c     = 3
# 2a - b  +  6c   = 24

# # Divide each row by the coefficient of a
# # a + b + 2c =   12
# # a - b - c/3 =  1
# # a - b/2 + 3c = 12

#   a - b/2 + 3c = 12
# - a + b   + 2c = 12
# ---------------------
#   0a -1.5b + c = 0


#   a - b - c/3 = 1
# - a + b + 2c  = 12
# --------------------
#   0a -2b -2.3c = -11

# 1st:
# -2b - 2.3c = -11

# 2nd:
# -1.5b + c = 0

# # Divide by the coefficients

# 1st:

# b -2.3/-2c = -11/-2
# b + 7/6c = 11/2

# 2nd:
# b - c/1.5 = 0

# Subtract 1st from 2nd

#   b - 2/3c = 0
# - b + 7/6c = 11/2
# -------------------------------
#     -1 * (2/3 + 7/6)c = -11/2

# -11/6c = -11/2
# c = 3

# b + 7/6(3) = 11/2
# b = 2

# a + 2 + 2(3) = 12
# a = 4
