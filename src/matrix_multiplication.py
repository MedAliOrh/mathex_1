import numpy as np

def matrix_multiply():

    # Define the matrices
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[10, 11], [13, 14], [16, 17]])

    # Perform the multiplication
    result = np.dot(A, B)

    return result
