import numpy as np


def pivoting(A: np.ndarray,
             k: int) -> np.ndarray:
    """
    Performs pivoting on matrix A for k-th step. For row version pivot comes
    from k-th column (from k-th row downwards), for column version it comes
    from k-th row (from k-th column rightwards).
    :param A: matrix to find pivot for
    :param k: algorithm step, row / column for pivoting
    :return: matrix A after pivoting, i.e. exchanging rows for optimal
    (largest) pivot
    """

    A = A.copy()
    n = A.shape[0]

    max_i = k
    for i in range(k, n):
        if abs(A[i, k]) > abs(A[max_i, k]):
            max_i = i

    if max_i != k:
        tmp_row = A[k, k:].copy()
        A[k, k:] = A[max_i, k:]
        A[max_i, k:] = tmp_row


    return A