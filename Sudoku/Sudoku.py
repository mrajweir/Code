UNSOLVED_PUZZLE = [
    0, 2, 6,  8, 7, 1,  3, 4, 0,
    4, 0, 3,  2, 0, 6,  8, 0, 1,
    8, 5, 0,  3, 0, 9,  0, 2, 6,

    3, 4, 2,  0, 1, 0,  6, 8, 7,
    5, 0, 8,  4, 0, 7,  9, 0, 3,
    1, 9, 7,  0, 8, 0,  2, 5, 4,

    6, 8, 0,  1, 3, 2,  0, 7, 9,
    7, 0, 4,  5, 0, 8,  1, 0, 2,
    0, 1, 9,  7, 6, 4,  0, 3, 0
]


def convert_coordinate_to_offset(x, y):
    # Convert the cartesian coordinate to an offset in a 1D list. To do that, the y-coordinate must be multipled by the
    # number of values in a row, and the x-coordinate is added to this. Subtract one from x and y coordinates to
    # account for zero-indexing.
    #
    # @param x The x-coordinate
    # @param y The y-coordinate
    # @return The offset necessary one a 1D list, for the given cartesian coordinate
    #
    return ((x-1)*9)+(y-1)


def get_value_at_coordinate(x, y):
    # @param x The x-coordinate
    # @param y The y-coordinate
    # @return The value of the sudoku grid for the given coordinate
    #
    return UNSOLVED_PUZZLE[convert_coordinate_to_offset(x, y)]


def get_missing_numbers_for_cell(x, y):
    # Sanity checking the input values.
    #
    if x < 1 or x > 9:
        print("[error] The x-coordinate value [ {} ] is out of bounds.".format(x))
        return

    if y < 1 or y > 9:
        print("[error] The y-coordinate value [ {} ] is out of bounds.".format(y))
        return

    if get_value_at_coordinate(x, y) is not 0:
        print("[error] The coordinate [ {},{} ] is already solved.".format(x, y))
        return

    # =================================================================================================================
    # SOLVING STRATEGY
    #
    # For the given cell, we need to calculate what values are missing in the following sets:
    #  * the row,
    #  * the column
    #  * the block.
    #
    # This is a brute-force strategy by analysing missing values for each set. To do this we need to do two lookups. For
    # each set, we need to perform a backwards count through the row, a forward count from that position in the row,
    # and a count for all cells in that block.
    #

    # -----------------------------------------------------------------------------------------------------------------
    # MISSING VALUES IN ROW
    #
    numbers_in_row = list()

    # Backwards count
    for i in range(1, y):
        numbers_in_row.append(get_value_at_coordinate(x, i))

    # Forwards count
    for i in range(y, 10):
        numbers_in_row.append(get_value_at_coordinate(x, i))

    # -----------------------------------------------------------------------------------------------------------------
    # MISSING VALUES IN COLUMN
    #
    numbers_in_column = list()

    for i in range(1, x):
        numbers_in_column.append(get_value_at_coordinate(i, y))

    for i in range(x, 10):
        numbers_in_column.append(get_value_at_coordinate(i, y))

    # -----------------------------------------------------------------------------------------------------------------
    # MISSING VALUES IN BLOCK
    #
    numbers_in_block = list()

    """
        print(1 % 3) ==> 1
        print(2 % 3) ==> 2
        print(3 % 3) ==> 0
    """
    if x % 3 == 1:
        if y % 3 == 1:
            # (1, 1)
            numbers_in_block.append(get_value_at_coordinate(x+1, y+1))  # 2, 2
            numbers_in_block.append(get_value_at_coordinate(x+1, y+2))  # 2, 3
            numbers_in_block.append(get_value_at_coordinate(x+2, y+1))  # 3, 2
            numbers_in_block.append(get_value_at_coordinate(x+2, y+2))  # 3, 3
        elif y % 3 == 2:
            # (1, 2)
            numbers_in_block.append(get_value_at_coordinate(x+1, y-1))  # 2, 1
            numbers_in_block.append(get_value_at_coordinate(x+2, y-2))  # 3, 1
            numbers_in_block.append(get_value_at_coordinate(x+1, y+1))  # 2, 3
            numbers_in_block.append(get_value_at_coordinate(x+2, y+1))  # 3, 3
        elif y % 3 == 0:
            # (1, 3)
            numbers_in_block.append(get_value_at_coordinate(x+1, y-2))  # 2, 1
            numbers_in_block.append(get_value_at_coordinate(x+1, y-1))  # 2, 2
            numbers_in_block.append(get_value_at_coordinate(x+2, y-2))  # 3, 1
            numbers_in_block.append(get_value_at_coordinate(x+2, y-1))  # 3, 2

    elif x % 3 == 2:
        if y % 3 == 1:
            # (2, 1)
            numbers_in_block.append(get_value_at_coordinate(x-1, y+1))  # 1, 2
            numbers_in_block.append(get_value_at_coordinate(x-1, y+2))  # 1, 3
            numbers_in_block.append(get_value_at_coordinate(x+1, y+1))  # 3, 2
            numbers_in_block.append(get_value_at_coordinate(x+1, y+2))  # 3, 3
        elif y % 3 == 2:
            # (2, 2)
            numbers_in_block.append(get_value_at_coordinate(x-1, y-1))  # 1, 1
            numbers_in_block.append(get_value_at_coordinate(x-1, y+1))  # 1, 3
            numbers_in_block.append(get_value_at_coordinate(x+1, y-1))  # 3, 1
            numbers_in_block.append(get_value_at_coordinate(x+1, y+1))  # 3, 3
        elif y % 3 == 0:
            # (2, 3)
            numbers_in_block.append(get_value_at_coordinate(x-1, y-2))  # 1, 1
            numbers_in_block.append(get_value_at_coordinate(x-1, y-1))  # 1, 2
            numbers_in_block.append(get_value_at_coordinate(x+1, y-2))  # 3, 1
            numbers_in_block.append(get_value_at_coordinate(x+1, y-1))  # 3, 2

    elif x % 3 == 0:
        if y % 3 == 1:
            # (3, 1)
            numbers_in_block.append(get_value_at_coordinate(x-2, y+1))  # 1, 2
            numbers_in_block.append(get_value_at_coordinate(x-2, y+2))  # 1, 3
            numbers_in_block.append(get_value_at_coordinate(x-1, y+1))  # 2, 2
            numbers_in_block.append(get_value_at_coordinate(x-1, y+2))  # 2, 3
        elif y % 3 == 2:
            # (3, 2)
            numbers_in_block.append(get_value_at_coordinate(x-2, y-1))  # 1, 1
            numbers_in_block.append(get_value_at_coordinate(x-2, y+1))  # 1, 3
            numbers_in_block.append(get_value_at_coordinate(x-1, y-1))  # 3, 1
            numbers_in_block.append(get_value_at_coordinate(x-1, y+1))  # 3, 3
        elif y % 3 == 0:
            # (3, 3)
            numbers_in_block.append(get_value_at_coordinate(x-2, y-2))  # 1, 1
            numbers_in_block.append(get_value_at_coordinate(x-2, y-1))  # 1, 2
            numbers_in_block.append(get_value_at_coordinate(x-1, y-2))  # 2, 1
            numbers_in_block.append(get_value_at_coordinate(x-1, y-1))  # 2, 2

    # Determine which numbers are not in the set of known numbers.
    #
    set_of_integers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    set_of_known_integers = set(numbers_in_row + numbers_in_column + numbers_in_block)
    set_of_unknown_integers = set(set_of_integers) - set(set_of_known_integers)

    # What values possibly fit in the sudoku cell?
    #
    if len(set_of_unknown_integers) == 0:
        print("[ info] The cell [ {},{} ] has no potential solution.".format(x, y))
    else:
        print("[ info] The potential unknown numbers for [ {},{} ] are [ {} ]".format(x, y, list(set_of_unknown_integers)))


for i in range(1, 10):
    for j in range(1, 10):
        get_missing_numbers_for_cell(i, j)
