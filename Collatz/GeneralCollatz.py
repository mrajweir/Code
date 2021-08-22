import pprint


def collatz(x, m):
    """
    Recursively find the values of the Collatz operation for a given number, x
    :param x:   The number to solve for
    :return:    Returns the result list (despite it being global, whatever)
    """
    if x % 2 == 0:
        x = int(x / 2)
    else:
        x = int((x*m) + 1)

    return x


m = 21
max = 1000
results = dict()

for i in range(1, 17):
    results[i] = list()
    next_term = i

    while True:
        next_term = collatz(next_term, m)
        loop_detected = next_term in results[i]
        end_found = next_term == 1

        results[i].append(next_term)

        if len(results[i]) > max:
            results[i].clear()
            results[i].append("∞")
            break

        if loop_detected or end_found:
            break

pprint.pprint(results)