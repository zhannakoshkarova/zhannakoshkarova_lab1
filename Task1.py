import numpy as np

def stretch(X,a,b):
    X = np.array(X, copy = True)
    A = np.array([[a, 0],
                  [0, b]])
    return A @ X

def shear(X,a,b):
    X = np.array(X, copy = True)
    A = np.array([[1, a],
                  [b, 1]])
    return A @ X

def reflection(X,a,b):
    if a == 0 and b == 0:
        raise ValueError("(a,b) must be a nonzero vector")
    X = np.array(X, copy = True)
    A = np.array([[a ** 2 - b ** 2, 2 * a * b],
                  [2 * a * b, b ** 2 - a ** 2]]) / (a ** 2 + b ** 2)
    return A @ X

def rotation(X,theta):
    X = np.array(X, copy = True)
    A = np.array([[np.cos(theta), - np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])
    return A @ X

X = np.array([[1, 0, 1],
              [0, 1, 1]])
Y = rotation(X, np.pi/2)
print(np.round(Y, 10))