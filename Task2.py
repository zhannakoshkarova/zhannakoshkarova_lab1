import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def read_off(filename: str):
    with open(filename, 'r') as f:
        if 'OFF' != f.readline().strip():
            raise ValueError('Not a valid OFF header')
        n_verts, n_faces, _ = map(int, f.readline().strip().split())
        verts = [list(map(float, f.readline().strip().split())) for _ in range(n_verts)]
        faces = [list(map(int, f.readline().strip().split()[1:])) for _ in range(n_faces)]
    return np.array(verts), faces

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