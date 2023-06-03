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
