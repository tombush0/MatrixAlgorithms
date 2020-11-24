import numpy as np

from Pivoting import pivoting

def gauss_elimination_row(A: np.ndarray) -> np.ndarray:

    """
    Performs Gaussian elimination on matrix A row-wise with pivoting.
    :param A: square matrix of shape (n, n)
    :return: matrix A after Gaussian elimination
    """

    A = A.copy()
    n = A.shape[0]
    for k in range(n):
        A = pivoting(A, k)
        A[k, k:] = A[k, k:] / A[k, k]
        for j in range(k + 1, n):
            A[j, k:] -= A[k, k:] * A[j, k]
    return A


B = np.array([1,-1,2,2,2,-2,1,0,-1,2,1,-2,2,-1,4,1],dtype='float32').reshape(4,4)

B_solved = gauss_elimination_row(B.copy())


print(B)
print()
print(B_solved)
