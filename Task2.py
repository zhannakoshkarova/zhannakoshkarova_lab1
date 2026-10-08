import numpy as np
import matplotlib.pyplot as plt

def rotate_xy (X,theta):
    X = np.array(X, copy=True)
    A = np.array([[np.cos(theta), - np.sin(theta), 0],
                  [np.sin(theta), np.cos(theta), 0],
                  [0 , 0, 1]])
    return A @ X, A

def rotate_yz (X,theta):
    X = np.array(X, copy=True)
    A = np.array([[1, 0, 0],
                  [0, np.cos(theta), - np.sin(theta)],
                  [0, np.sin(theta), np.cos(theta)]])
    return A @ X, A

def rotate_xz (X,theta):
    X = np.array(X, copy=True)
    A = np.array([[np.cos(theta),0, - np.sin(theta)],
                  [0, 1, 0],
                  [np.sin(theta),0, np.cos(theta)]])
    return A @ X, A