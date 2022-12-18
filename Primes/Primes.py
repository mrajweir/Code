import matplotlib.pyplot as plt
import time
from math import floor, sqrt
import multiprocessing


def primes(i, j):
    """
    Plot the prime numbers from 1 to n.
    """
    primes = []
    iteration = []
    iteri = 0

    # Introduce threading to improve performance.
    cpu_count = multiprocessing.cpu_count()
    print("{0}".format(cpu_count))

    for m in range(i, j):
        # For every even integer being tested (greater than two), skip because we know it can't be prime
        if m > 2 and m % 2 == 0:
            continue

        # For every integer as a multiple of five, skip because we know it can't be prime. (15, 25, etc. where
        # parity doesn't count.)
        if m > 5 and m % 5 == 0:
            continue

        # Trial division for every possible integer between 1 and n itself.
        n = 1
        factorizations_found = 0

        while n <= m:
            if m % n == 0:
                factorizations_found += 1
            n += 1

        # Primes only have two factorizations, n/1 and n/n - so therefore, we've found a prime
        if factorizations_found == 2:
            iteri += 1
            iteration.append(iteri)
            primes.append(m)

    # x axis values
    x = iteration
    # corresponding y axis values
    y = primes

    # plotting the points
    plt.scatter(x, y, label="Distribution of the Primes")

    # naming the x axis
    plt.xlabel('Iteration')
    plt.ylabel('Prime Number')

    # giving a title to my graph
    plt.title('Prime Numbers')

    plt.legend()

    # function to show the plot
    plt.show()

    print(primes)


start = time.time()
primes(2, 10000)
end = time.time()

print("Execution Time: {0}".format(end - start))