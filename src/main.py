import numpy as np
import matrix_multiplication
import rotation_matrix
import transformations

if __name__ == "__main__":
    
    #EX 1
    print("multiplying[[1, 2, 3], [4, 5, 6]] by [[10, 11], [13, 14], [16, 17]] : \n Result : \n", matrix_multiplication.matrix_multiply(), end='\n')
    
    #EX 2
    theta = np.pi / 4  # 45 degrees

    result1 = rotation_matrix.calculate_rotation_matrix_1(theta)    
    direction = np.array([1, 1, 1])
    result2 = rotation_matrix.calculate_rotation_matrix_2(theta, direction)
    print("\nFirst code\n", result1, "\nSecond code\n", result2)
    
    #Bonus
    C0 = np.array([100, 150, 200])
    print("\nColor rotation :\nC0: ", C0,"\nC1: ", rotation_matrix.apply_rotation_to_color(result2, C0))

    #EX 3

    C1 = rotation_matrix.apply_rotation_to_color(result2, C0)
    D1 = np.array([255, 255, 255])

    result3 = transformations.second_transformation(C1, D1)
    print("Result 4:\n", result3)

    result4 = transformations.transformation_matrix(D1)
    print("Result 5:\n", result4)
