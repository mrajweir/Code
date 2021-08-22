import matplotlib.pyplot as plt

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


x_axis = list()
y_axis = list()

# Returns the number of operations needed for the first thousand solutions to the Collatz formula
#
for i in range(1, 1000000):
    x_axis.append(i)
    collatz(i)

    counter = 0
    for n in results:
        counter += 1

    y_axis.append(counter)
    #print("For the number {0}, there were {1} operations to reach the end.".format(i, counter))
    #print(results)
    #print(" ")
    results = list()


width_in_inches = 13
height_in_inches = 11
dots_per_inch = 70

plt.figure(
    figsize=(width_in_inches, height_in_inches),
    dpi=dots_per_inch)


plt.xlabel("Iteration")
plt.ylabel("Number of Collatz operations")
plt.plot(x_axis, y_axis, 'b.')
plt.show()

