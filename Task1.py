import numpy as np
import matplotlib.pyplot as plt

def stretch(X,a,b):
    X = np.array(X, copy = True)
    A = np.array([[a, 0],
                  [0, b]])
    return A @ X, A

def shear(X,a,b):
    X = np.array(X, copy = True)
    A = np.array([[1, a],
                  [b, 1]])
    return A @ X, A

def reflection(X,a,b):
    if a == 0 and b == 0:
        raise ValueError("(a,b) must be a nonzero vector")
    X = np.array(X, copy = True)
    A = np.array([[a ** 2 - b ** 2, 2 * a * b],
                  [2 * a * b, b ** 2 - a ** 2]]) / (a ** 2 + b ** 2)
    return A @ X, A

def rotation(X,theta):
    X = np.array(X, copy = True)
    A = np.array([[np.cos(theta), - np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])
    return A @ X, A



def show(X, Y, A, title, color='tab:blue'):
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.fill(X[0], X[1], color='gray', alpha=0.4, label='original')
    ax.fill(Y[0], Y[1], color=color, alpha=0.5, label='transformed')
    ax.axhline(0, color='k', lw=0.5); ax.axvline(0, color='k', lw=0.5)
    ax.set_aspect('equal'); ax.legend(); ax.set_title(title)
    plt.show()
    print(title)
    print(np.round(A, 4))
    print()

if __name__ == "__main__":
    batman = np.array([[0, 0], [1, 0.2], [0.4, 1], [0.5, 0.4], [0, 0.8], [-0.5, 0.4], [-0.4, 1], [-1, 0.2], [0, 0]])
    batman = batman.T
    show(batman, batman, np.eye(2), "Original", color='gray')
    Y, A = stretch(batman, 1.5, 0.7);
    show(batman, Y, A, "Stretch (1.5, 0.7)")
    Y, A = shear(batman, 0.5, 0);
    show(batman, Y, A, "Shear (0.5, 0)")
    Y, A = reflection(batman, 1, 1);
    show(batman, Y, A, "Reflection (line y = x)")
    Y, A = rotation(batman, np.pi / 4);
    show(batman, Y, A, "Rotation (45 deg)")