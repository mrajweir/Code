square = [
    0, 0, 0,
    0, 0, 0,
    0, 0, 0
]

search_limit = 10

sum_diag_a = square[2] + square[4] + square[6]
sum_diag_b = square[0] + square[4] + square[8]

sum_row_a = square[0] + square[1] + square[2]
sum_row_b = square[3] + square[4] + square[5]
sum_row_c = square[6] + square[7] + square[8]

sum_col_a = square[0] + square[3] + square[6]
sum_col_b = square[1] + square[4] + square[7]
sum_col_c = square[2] + square[5] + square[8]

for i in range(0, 9):
    # pass
    pass


print("                   {0:<5}".format(sum_diag_a))
print(" ")
print("{0:<5} {0:<5} {0:<5} | {0:<5}".format(square[0], square[1], square[2], sum_row_a))
print(" ")
print("{0:<5} {0:<5} {0:<5} | {0:<5}".format(square[3], square[4], square[5], sum_row_b))
print(" ")
print("{0:<5} {0:<5} {0:<5} | {0:<5}".format(square[6], square[7], square[8], sum_row_c))
print(" ")
print("{0:<5} {0:<5} {0:<5} | {0:<5}".format(sum_col_a, sum_col_b, sum_col_c, sum_diag_b))