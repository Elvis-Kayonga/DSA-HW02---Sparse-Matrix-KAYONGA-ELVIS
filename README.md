# SparseMatrix - README

## Introduction

This repository contains a Python class `SparseMatrix` for performing operations on sparse matrices. Sparse matrices are matrices in which most of the elements are zero. This class allows you to load matrices from files, perform operations such as addition, subtraction, and multiplication, and save the resulting matrix to a file.

## Features

- **Load matrix**: Load a sparse matrix from a file.
- **Matrix operations**: Perform matrix addition, subtraction, and multiplication.
- **Save matrix**: Save the resulting sparse matrix to a file.
- **Efficient memory usage**: Only non-zero values are stored, saving memory in large sparse matrices.

## File Format

Input matrix files should follow this format:
- The first line contains the number of rows (e.g., `rows=3`).
- The second line contains the number of columns (e.g., `cols=3`).
- The following lines contain non-zero elements in the format `(row, col, value)`.

### Example:
```
rows=3
cols=3
(0, 1, 5)
(1, 2, 8)
```

## Class Methods

- **`load_matrix(file_path)`**: Loads a sparse matrix from a file.
- **`get_element(row, col)`**: Returns the element at the specified row and column, or 0 if the element is not present.
- **`set_element(row, col, value)`**: Sets a value at a specific position in the matrix.
- **`add(other_matrix)`**: Adds two matrices and returns the result.
- **`subtract(other_matrix)`**: Subtracts one matrix from another and returns the result.
- **`multiply(other_matrix)`**: Multiplies two matrices and returns the result.
- **`save_to_file(file_path)`**: Saves the current matrix to a file in the required format.

## Usage

1. **Load Matrices**:  
   Matrices are loaded from files using the `SparseMatrix` constructor. The file should follow the defined input format.

   ```python
   matrix1 = SparseMatrix(matrix_file='matrix1.txt')
   matrix2 = SparseMatrix(matrix_file='matrix2.txt')
   ```

2. **Perform Operations**:  
   You can perform addition, subtraction, or multiplication between two matrices.

   ```python
   result_add = matrix1.add(matrix2)
   result_subtract = matrix1.subtract(matrix2)
   result_multiply = matrix1.multiply(matrix2)
   ```

3. **Save Result**:  
   After performing an operation, save the result to a file.

   ```python
   result_add.save_to_file('result.txt')
   ```

## Running the Script

To execute the script, run the following command:

```bash
python sparse_matrix.py
```

You will be prompted to load two matrices from files, choose an operation (addition, subtraction, multiplication), and then save the result to an output file.

### Example Execution:

```
Choose a matrix operation:
1. Add Matrices
2. Subtract Matrices
3. Multiply Matrices
Enter your choice (1/2/3): 1
Enter the output file path to save the result: result.txt
Result saved to result.txt.
```

## Error Handling

- If matrices are incompatible for the chosen operation (e.g., multiplication requires matching dimensions), a `ValueError` will be raised with a helpful message.
- If the input file format is incorrect, a `ValueError` is raised, informing the user of the format issue.

## License

This project is licensed under the MIT License.

## Author

This project was developed as part of a Python learning exercise on sparse matrix operations.
