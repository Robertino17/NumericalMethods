import numpy as np

def solve_linear_system(A, B):
    for l in range(0, len(A) - 1):
        T = abs(A)
        a = T[l:, l].argmax()
        A[[l, l + a]] = A[[l + a, l]]
        B[[l, l + a]] = B[[l + a, l]]
        for i in range(l + 1, len(A)):
            B[i] = B[i] - (B[l] * A[i, l]) / A[l, l]
            for j in range(l + 1, len(A)):
                A[i, j] = A[i, j] - ((A[i, l] * A[l, j]) / A[l, l])
        X = np.zeros((len(B)))
        X[-1] = B[-1] / A[-1, -1]
        for i in range(len(X) - 2, -1, -1):
            for j in range(len(X) - 1, i, -1):
                B[i] = B[i] - X[j] * A[i, j]
            X[i] = B[i] / A[i, i]
    return X