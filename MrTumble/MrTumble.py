import time


def banner():
    """
    Who doesn't love a bit of ASCII?
    :return: Nothing
    """
    print(" ")
    print("              _  _   __   __ _  ____  __  ____  _  _  ____    ____  _  _  _  _  ____  __    ____    ")
    print("             ( \/ ) /  \ (  ( \/ ___)(  )(  __)/ )( \(  _ \  (_  _)/ )( \( \/ )(  _ \(  )  (  __)   ")
    print("             / \/ \(  O )/    /\___ \ )(  ) _) ) \/ ( )   /    )(  ) \/ (/ \/ \ ) _ (/ (_/\ ) _)    ")
    print("             \_)(_/ \__/ \_)__)(____/(__)(____)\____/(__\_)   (__) \____/\_)(_/(____/\____/(____)   ")
    print(" ")
    print("                       Version 0.1 | andrew@ajweir.co.uk                        ")
    print(" ")
    print(" ")


def luhn_checksum(card_number):
    """
    Compute the Luhn checksum algorithm on all digits of the card number, and return whether or not the card number
    is constructed correctly.
    :param card_number:  16-digit card number to verify
    :return: True or False
    """
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10


def is_luhn_valid(card_number):
    """
    Wrapper around the Luhn check.
    :param card_number: 16-digit card number to verify
    :return: True or False
    """
    return luhn_checksum(card_number) == 0


def find_card(first_six, last_four):
    """
    Given the first six and last four digits of a 16-digit card number, find all possible valid card numbers.
    :param first_six:  Six digits
    :param last_four:  Four digits
    :return: A list of dictionaries with the iteration and the card number.
    """
    cards_found = list()

    # Replace 9999 with the number of digits between the first_six and last_four to make up a card number.
    # IE: "400000" + i_in_9999 + "0002"
    #
    card_count = 0

    for i in range(0, 9999):
        # Get me a card number, prefixing the iteration with zeroes
        card_number = first_six + "{:04d}".format(i) + last_four

        # Was the number I generated valid in the first place?
        if is_luhn_valid(card_number):
            # Got a hit, increment the count
            card_count = card_count + 1
            # Print out how many card numbers we've found along with the card number
            cards_found.append({"card_count": card_count, "card_number": card_number})

    return cards_found


# When run as a script, give the user something interesting to do.
if __name__ == "__main__":
    banner()

    # Ask the user to enter in the card range they want to find
    first_six = input("Enter in the first six digits of the card > ")
    last_four = input("Enter in the last four digits of the card > ")

    # Generation of possible card numbers begins now.
    # How long did it take to generate?
    before = time.time()

    # how many did it find?
    cards_found = find_card(first_six, last_four)

    for d in cards_found:
        print("[{:-7d}] ".format(d["card_count"]) + d["card_number"])

    # how long did it take to finish?
    after = time.time()

    # Total execution time was
    print("-- Mr. Tumble took [ {0} ] seconds.".format(after-before))
