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

# combined

    #1
Y, A = stretch(batman, 1.5, 0.7)
show(batman, Y, A, "Stretch", color = 'tab:blue')
Y2, A2 = shear(Y, 0.5, 0);
show(Y, Y2, A2, "Stretch + Shear", color = 'tab:blue')
Y3, A3 = rotation(Y2, np.pi / 4);
show(Y2, Y3, A3, "Stretch + Shear + Rotation", color = 'tab:blue')
M1 = A3 @ A2 @ A
F1 = Y3
print("Combined matrix (S -> SH -> R):\n", np.round(M1, 4))

    #2
Y, A = rotation(batman, np.pi / 4);
show(batman, Y, A, "Rotation", color = 'tab:red')
Y2, A2 = stretch(Y, 1.5, 0.7)
show(Y, Y2, A2, "Rotation + Stretch", color = 'tab:red')
Y3, A3 = shear(Y2, 0.5, 0);
show(Y2, Y3, A3, "Rotation + Stretch + Shear", color = 'tab:red')
M2 = A3 @ A2 @ A
F2 = Y3
print("Combined matrix (R -> S -> SH):\n", np.round(M2, 4))


    #3
Y, A = shear(batman, 0.5, 0);
show(batman, Y, A, "Shear", color = 'tab:green')
Y2, A2 = rotation(Y, np.pi / 4);
show(Y, Y2, A2, "Shear + Rotation", color = 'tab:green')
Y3, A3 = stretch(Y2, 1.5, 0.7)
show(Y2, Y3, A3, "Shear + Rotation + Stretch", color = 'tab:green')
M3 = A3 @ A2 @ A
F3 = Y3
print("Combined matrix (SH -> R -> S):\n", np.round(M3, 4))


fig, ax = plt.subplots(figsize=(6, 6))
for F, label, c in [(F1, "S -> H -> R", 'tab:blue'),
                    (F2, "R -> S -> H", 'tab:red'),
                    (F3, "H -> R -> S", 'tab:green')]:
    ax.fill(F[0], F[1], color=c, alpha=0.35, label=label)
ax.axhline(0, color='k', lw=0.5); ax.axvline(0, color='k', lw=0.5)
ax.set_aspect('equal'); ax.legend(); ax.set_title("Same transformations, different order")
plt.show()



