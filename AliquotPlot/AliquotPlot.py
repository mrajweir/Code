import math
import time
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def aliquot_sum(x, memo={}):
    """
    Calculate the aliquot sum of a given integer
    :param x: Integer
    :param memo: Memoization dictionary to store calculated values
    :return: The sum of the factors, except the number itself
    """
    if x in memo:
        return memo[x]
    factors_sum = 1  # 1 is always a factor of x
    sqrt_x = math.isqrt(x)

    # Only need to go to the square root of the number to find all the viable primes
    for i in range(2, sqrt_x + 1):
        if x % i == 0:
            factors_sum += i
            if i != x // i:  # Avoid double counting if i and x//i are the same
                factors_sum += x // i
    memo[x] = factors_sum
    return factors_sum


def aliquot_sequence(n):
    """
    Generate the aliquot sequence for a given integer
    :param n: Integer
    :return:~ List representing the aliquot sequence
    """
    seq = []
    while n != 1 and n not in seq and math.log10(n) < 18:
        seq.append(n)
        n = aliquot_sum(n)
    if n in seq:  # If a loop is detected, mark the sequence as repeating
        seq.append(n)
        seq = seq[seq.index(n):]
    return seq


if __name__ == '__main__':
    start_time = time.perf_counter()

    aliquot_sequences = list()

    low = 1
    high = 100
    for i in range(low, high):
        aq_seq = aliquot_sequence(i)
        aq_seq.append(1)
        log_aq_seq = [math.log10(num) for num in aq_seq]

        aliquot_sequences.append({
            str(i): aq_seq,
            "integer": i
        })

        print(aq_seq)

        plt.rcParams['figure.figsize'] = [14, 14]
        plt.text(0.5, 0.5, "Max number: " + str(max(aq_seq)))
        plt.margins(0)
        plt.plot(log_aq_seq)

        plt.xlabel("Step in Sequence")
        plt.ylabel("Log 10 - Integer Reached")

        plt.title(f"Aliquot Sequences: {low}-{high}")

        plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

    plt.show()
    end_time = time.perf_counter()

    print(f"Time taken [ {(end_time-start_time)} ] seconds.")