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


def plot_off(vertices, faces, title=""):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    mesh = Poly3DCollection([vertices[face] for face in faces],
                            alpha=0.7, edgecolor='k', facecolor='tab:blue')
    ax.add_collection3d(mesh)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title(title)

    ax.auto_scale_xyz(vertices[:, 0], vertices[:, 1], vertices[:, 2])
    plt.show()

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

def apply(vertices, rotate_fn, theta):
    Y, A = rotate_fn(vertices.T, theta)
    return Y.T, A


vertices, faces = read_off("/Users/ai/.cache/kagglehub/datasets/balraj98/modelnet40-princeton-3d-object-dataset/versions/1/ModelNet40/airplane/test/airplane_0627.off")
print(vertices.shape)
print(faces[:3])

plot_off(vertices, faces, "Original")

new_vertices, A = apply(vertices, rotate_xy, np.pi / 4)
plot_off(new_vertices, faces, "rotate_xy, 45 deg")
print(np.round(A, 4))

new_vertices, A = apply(vertices, rotate_yz, np.pi / 4)
plot_off(new_vertices, faces, "rotate_yz, 45 deg")
print(np.round(A, 4))

new_vertices, A = apply(vertices, rotate_xz, np.pi / 4)
plot_off(new_vertices, faces, "rotate_xz, 45 deg")
print(np.round(A, 4))