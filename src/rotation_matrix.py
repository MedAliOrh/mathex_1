import numpy as np

# French version
def calculate_rotation_matrix_1(theta):
    direction = np.array([1, 1, 1]) / np.sqrt(3)
    ux, uy, uz = direction
    
    # Matrice antisymétrique K
    K = np.array([
        [0, -uz, uy],
        [uz, 0, -ux],
        [-uy, ux, 0]
    ])
    
    # Calcul de K^2
    K2 = np.dot(K, K)
    
    # Matrice de rotation avec la formule de Rodrigues
    I = np.eye(3)  # Matrice identité
    R = I + np.sin(theta) * K + (1 - np.cos(theta)) * K2
    return R

def calculate_rotation_matrix_2(theta, direction, point1=None, point2=None):

    if (point1 is None) or (point2 is None):
    # Define the points for the line D1
        point1 = np.array([0, 0, 0])
        point2 = np.array([255, 255, 255])
    
    # Direction vector of the line D1
    direction = direction / np.linalg.norm(direction)  # Normalize the direction vector

    # Rotation matrix
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    ux, uy, uz = direction

    rotation_matrix = np.array([
        [cos_theta + ux**2 * (1 - cos_theta), ux * uy * (1 - cos_theta) - uz * sin_theta, ux * uz * (1 - cos_theta) + uy * sin_theta],
        [uy * ux * (1 - cos_theta) + uz * sin_theta, cos_theta + uy**2 * (1 - cos_theta), uy * uz * (1 - cos_theta) - ux * sin_theta],
        [uz * ux * (1 - cos_theta) - uy * sin_theta, uz * uy * (1 - cos_theta) + ux * sin_theta, cos_theta + uz**2 * (1 - cos_theta)]
    ])

    return rotation_matrix

def apply_rotation_to_color(rotation_matrix, color):
    # Apply the rotation matrix to the color
    rotated_color = np.dot(rotation_matrix, color)
    
    # Clip the values to be within the valid RGB range [0, 255]
    rotated_color = np.clip(rotated_color, 0, 255)

    # Round the values to the nearest integer
    rotated_color = np.round(rotated_color).astype(int)
    
    return rotated_color
