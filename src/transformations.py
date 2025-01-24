import numpy as np

def second_transformation(C1, D1):

    # Normalize the direction vector D1
    D1_normalized = D1 / np.linalg.norm(D1)

    # Project C1 onto the line D1
    projection_length = np.dot(C1, D1_normalized)
    projection = projection_length * D1_normalized

    # Calculate the orthogonal component
    orthogonal_component = C1 - projection

    # Reflect the orthogonal component
    reflected_orthogonal_component = -orthogonal_component

    # The new color C2 is the projection plus the reflected orthogonal component
    C2 = projection + reflected_orthogonal_component

    # Clip the values to be within the valid RGB range [0, 255]
    C2 = np.clip(C2, 0, 255)

    # Round the values to the nearest integer
    C2 = np.round(C2).astype(int)

    return C2

def transformation_matrix(D1):

    # Normalize the direction vector D1
    D1_normalized = D1 / np.linalg.norm(D1)

    # Create the reflection matrix
    I = np.eye(3)
    reflection_matrix = I - 2 * np.outer(D1_normalized, D1_normalized)

    return reflection_matrix
