import numpy as np

# IJP matrix multiplication

def matmul_1b(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    m = A.shape[0]
    k = A.shape[1]  # B.shape[0]
    n = B.shape[1]

    C = np.zeros((m, n))

    A_T = A.T

    for i in range(m):
        C[0:n, i] = np.dot(A_T[0:k, i], B)

    return C.T

A = np.array([[1, 0, 2],
              [-1, 3, 1]])

B = np.array([[3, 1],
              [2, 1],
              [1, 0]])

C = matmul_1b(A, B)

target = np.array([[5, 1],
                   [4, 2]])


assert (C == target).all()