import random
from PIL import Image

def roll_dice():
    return random.randint(1, 6)


def potential_moves():
    duplicated_moves = []
    for i in range(1, 7):
        for j in range(1, 7):
            duplicated_moves.append(i*j)

    valid_moves = sorted(set(duplicated_moves))
    return valid_moves


if __name__ == "__main__":
    # ===========
    # Demo to check I can do random dice rolls
    dice_moves = roll_dice()
    dice_multipler = roll_dice()
    moves = dice_moves * dice_multipler
    print("You rolled [ {} | {} ], so your piece moves [ {} ] around the board.".format(dice_moves, dice_multipler, moves))


    # ============
    # Let's draw out the potential squares you can land on. Created a lookup table of coordinates, starting from
    # bottom-right of the monopoly board, and working clockwise, as you would go if you were playing it.
    # Generated the coords with an algorithm, and decided for speed to LUT instead.
    monopoly = [
        (352, 352),
        (16+(33*9), 352),
        (16+(33*8), 352),
        (16+(33*7), 352),
        (16+(33*6), 352),
        (16+(33*5), 352),
        (16+(33*4), 352),
        (16+(33*3), 352),
        (16+(33*2), 352),
        (16+(33*1), 352),
        (10, 352),
        (10, (48 + (33 * 8))),
        (10, (48 + (33 * 7))),
        (10, (48 + (33 * 6))),
        (10, (48 + (33 * 5))),
        (10, (48 + (33 * 4))),
        (10, (48 + (33 * 3))),
        (10, (48 + (33 * 2))),
        (10, (48 + (33 * 1))),
        (10, (48 + (33 * 0))),
        (10, 10),
        (16 + (33 * 1), 10),
        (16 + (33 * 2), 10),
        (16 + (33 * 3), 10),
        (16 + (33 * 4), 10),
        (16 + (33 * 5), 10),
        (16 + (33 * 6), 10),
        (16 + (33 * 7), 10),
        (16 + (33 * 8), 10),
        (16 + (33 * 9), 10),
        (352, 10),
        (352, 48 + (33 * 0)),
        (352, 48 + (33 * 1)),
        (352, 48 + (33 * 2)),
        (352, 48 + (33 * 3)),
        (352, 48 + (33 * 4)),
        (352, 48 + (33 * 5)),
        (352, 48 + (33 * 6)),
        (352, 48 + (33 * 7)),
        (352, 48 + (33 * 8)),
    ]

    # Loading the template image file to see where you can and can't move to.
    template = Image.open("templates/actual_board.jpg")

    # Load the tick and cross symbols
    tick = Image.open("templates/tick.png")
    cross = Image.open("templates/cross.png")

    # Anywhere that you can potentially move to on the first roll, mark as a tick.
    for move in potential_moves():
        template.paste(tick, monopoly[move], tick)

    # Show the image
    template.show()