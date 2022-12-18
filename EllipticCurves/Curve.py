import matplotlib.pyplot as plt
import numpy as np

def main():
    a = -1
    b = 1

    y, x = np.ogrid[-5:5:100j, -5:5:100j]
    plt.contour(
        x.ravel(),
        y.ravel(),
        pow(y, 2) - pow(x, 3) - x * a - b,
        [0]
    )
    plt.plot(1, 1, 'ro')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()