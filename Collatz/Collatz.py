results = list()


def collatz(x):
    """
    Recursively find the values of the Collatz operation for a given number, x
    :param x:   The number to solve for
    :return:    Returns the result list (despite it being global, whatever)
    """
    if x % 2 == 0:
        x = int(x / 2)
    else:
        x = int((x*3) + 1)

    results.append(x)

    if x != 1:
        collatz(x)


# Returns the number of operations needed for the first thousand solutions to the Collatz formula
#
for i in range(1,1000):
    collatz(i)

    counter = 0
    for n in results:
        counter += 1

    print("For the number {0}, there were {1} operations to reach the end.".format(i, counter))
    print(results)
    print(" ")
    results = list()
