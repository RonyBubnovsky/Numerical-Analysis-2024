# Matrix Operations in Python

This Python script demonstrates various operations on 3x3 matrices, including calculating determinants, multiplying matrices, checking identity matrices, and finding inverse matrices using elementary matrices.

## Purpose

The purpose of this script is to illustrate:

- **Matrix Determinant Calculation**: Calculates the determinant of a 3x3 matrix.
- **Matrix Multiplication**: Multiplies two 3x3 matrices.
- **Identity Matrix Check**: Checks if a given 3x3 matrix is an identity matrix.
- **Matrix Inversion**: Finds the inverse of a 3x3 matrix using elementary row operations.
- **Condition Number Calculation**: Computes the condition number (Cond) of a matrix using its determinant and the determinant of its inverse.

## Usage

To use the functions provided:

1. Ensure Python 3.x is installed on your system.
2. Clone or download the repository.
3. Modify the `matrix` variable in the script with your desired 3x3 matrix.
4. Run the script.

## Example

```python
# Example usage of the functions
matrix = [[1, -1, -2], [2, -3, -5], [-1, 3, 5]]

# Calculate the determinant of the matrix
matrix_determinant = calculate_determinant(matrix)

# Find the inverse of the matrix
inverse_matrix = find_inverse_matrix(matrix)

# Calculate the determinant of the inverse matrix
inverse_matrix_determinant = calculate_determinant(inverse_matrix)

# Calculate the condition number (Cond)
condition_number = inverse_matrix_determinant * matrix_determinant

print("The Condition Number is:", condition_number)
```
