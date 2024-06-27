"""
Rony Bubnovsky 314808825
Bar Levi 314669664
Aviel Esperansa 324062116
"""

matrix = [[1, -1, -2], [2, -3, -5], [-1, 3, 5]] 


def calculate_determinant(matrix):
    """
    Calculate the determinant of a 3x3 matrix.
    
    Parameters:
    matrix (list of list of int/float): A 3x3 matrix represented as a list of lists.

    Returns:
    float: The determinant of the matrix.
    """
    # Extract elements from the matrix for easier reference
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    
    # Calculate the determinant
    determinant = (a * (e * i - f * h) 
                   - b * (d * i - f * g) 
                   + c * (d * h - e * g))
    
    return determinant  # Return the determinant of the matrix

matrix_determinant = calculate_determinant(matrix)

if not matrix_determinant:
    print("The matrix is not invertible.")
    exit()


def multiply_matrix(matrix1, matrix2):
    """
    Multiply two 3x3 matrices.

    Parameters:
    matrix1 (list of list of int/float): The first 3x3 matrix.
    matrix2 (list of list of int/float): The second 3x3 matrix.

    Returns:
    list of list of int/float: The resulting 3x3 matrix after multiplication.
    """
    # Initialize the result matrix with zeros
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    # Perform matrix multiplication
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += matrix1[i][k] * matrix2[k][j]  # Accumulate the product of the corresponding elements
    
    return result  # Return the resulting matrix



def is_identity_matrix(matrix):
    """
    Check if a 3x3 matrix is an identity matrix.

    Parameters:
    matrix (list of list of int/float): The 3x3 matrix to be checked.

    Returns:
    bool: True if the matrix is an identity matrix, False otherwise.
    """
    
    for i in range(3):
        for j in range(3):
            if i == j:  # Check diagonal elements
                if matrix[i][j] != 1:  # Diagonal elements should be 1
                    return False
            else:  # Check off-diagonal elements
                if matrix[i][j] != 0:  # Off-diagonal elements should be 0
                    return False

    return True  # Return True if all checks are passed


       

def find_inverse_matrix(matrix):
    """
    Find the inverse of a given 3x3 matrix using elementary row matrices.
    
    Parameters:
    matrix (list of list of floats): A 3x3 matrix represented as a list of lists.
    
    Returns:
    list of list of floats: The inverse of the input matrix if it exists.
    """
    inverse_matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]  
    
    
    for j in range(3):
        for i in range(3):
            elementary_matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]  
            if i != j and matrix[i][j] != 0: 
                elementary_matrix[i][j] = -matrix[i][j] / matrix[j][j]  
                inverse_matrix = multiply_matrix(elementary_matrix, inverse_matrix) 
                matrix = multiply_matrix(elementary_matrix, matrix)  
                
                    
                    
    for i in range(3):
        elementary_matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]] 
        if matrix[i][i] != 1:  
            elementary_matrix[i][i] = 1 / matrix[i][i]    
            inverse_matrix = multiply_matrix(elementary_matrix, inverse_matrix)  
            matrix = multiply_matrix(elementary_matrix, matrix)
            
     
                    
     
    return inverse_matrix  
                                    
    
inverse_matrix = find_inverse_matrix(matrix)

print(f'The inverse matrix is: {inverse_matrix}\n')



            
            



                    
                
                
                               
                
                
                
                
                 










 





