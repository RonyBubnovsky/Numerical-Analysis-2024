Matrix Operations in Python
Purpose
This Python code is designed to perform various operations on 3x3 matrices, including calculating the determinant, checking if a matrix is an identity matrix, multiplying two matrices, and finding the inverse of a matrix. The code also demonstrates how to calculate the condition number of a matrix, which is a measure of the sensitivity of the solution of a system of linear equations to errors in the data.

Functions
calculate_determinant(matrix)
Calculates the determinant of a given 3x3 matrix.

Parameters:

matrix (list of list of int/float): A 3x3 matrix represented as a list of lists.
Returns:

float: The determinant of the matrix.
multiply_matrix(matrix1, matrix2)
Multiplies two 3x3 matrices.

Parameters:

matrix1 (list of list of int/float): The first 3x3 matrix.
matrix2 (list of list of int/float): The second 3x3 matrix.
Returns:

list of list of int/float: The resulting 3x3 matrix after multiplication.
is_identity_matrix(matrix)
Checks if a given 3x3 matrix is an identity matrix.

Parameters:

matrix (list of list of int/float): The 3x3 matrix to be checked.
Returns:

bool: True if the matrix is an identity matrix, False otherwise.
find_inverse_matrix(matrix)
Finds the inverse of a given 3x3 matrix using elementary row operations.

Parameters:

matrix (list of list of floats): A 3x3 matrix represented as a list of lists.
Returns:

list of list of floats: The inverse of the input matrix if it exists.
Usage
Define the Matrix:

python
Copy code
matrix = [[1, -1, -2], [2, -3, -5], [-1, 3, 5]]
Calculate Determinant:

python
Copy code
matrix_determinant = calculate_determinant(matrix)
Find Inverse Matrix:

python
Copy code
inverse_matrix = find_inverse_matrix(matrix)
Calculate Determinant of Inverse Matrix:

python
Copy code
inverse_matrix_determinant = calculate_determinant(inverse_matrix)
Compute Condition Number:

python
Copy code
print("The Cond is:", inverse_matrix_determinant \* matrix_determinant)
Example
python
Copy code
matrix = [[1, -1, -2], [2, -3, -5], [-1, 3, 5]]

# Calculate determinant of the matrix

matrix_determinant = calculate_determinant(matrix)

# Find inverse of the matrix

inverse_matrix = find_inverse_matrix(matrix)

# Calculate determinant of the inverse matrix

inverse_matrix_determinant = calculate_determinant(inverse_matrix)

# Print the condition number

print("The Cond is:", inverse_matrix_determinant \* matrix_determinant)
