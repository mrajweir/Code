import time


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def banner():
    print(" ")
    print("              _  _  ____       ____  _  _  ____  _  _  __    ____               ")
    print("             ( \/ )(  _ \     (_  _)/ )( \(  _ \( \/ )(  )  (  __)              ")
    print("             / \/ \ )   / _     )(  ) \/ ( ) _ (/ \/ \/ (_/\ ) _)               ")
    print("             \_)(_/(__\_)(_)   (__) \____/(____/\_)(_/\____/(____)              ")
    print(" ")
    print("                       Version 0.1 | andrew@ajweir.co.uk                        ")
    print(" ")
    print(" ")


def luhn_checksum(card_number):
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
    return luhn_checksum(card_number) == 0


def main():
    banner()

    # Ask the user to enter in the card range they want to find
    first_six = input("Enter in the first six digits of the card > ")
    last_four = input("Enter in the last four digits of the card > ")

    # Generation of possible card numbers begins now.
    # How long did it take to generate?
    before = time.time()

    # how many did it find?
    card_count = 0

    # Replace 9999 with the number of digits between the first_six and last_four to make up a card number.
    # IE: "400000" + i_in_9999 + "0002"
    #
    for i in range(0, 9999):
        # Get me a card number, prefixing the iteration with zeroes
        card_number = first_six + "{:04d}".format(i) + last_four

        # Was the number I generated valid in the first place?
        if is_luhn_valid(card_number):
            # Got a hit, increment the count
            card_count = card_count + 1
            # Print out how many card numbers we've found along with the card number
            print("[{:-7d}] ".format(card_count) + card_number)

    # how long did it take to finish?
    after = time.time()

    # Total execution time was
    print("-- Mr. Tumble took [ {0} ] seconds.".format(after-before))


main()