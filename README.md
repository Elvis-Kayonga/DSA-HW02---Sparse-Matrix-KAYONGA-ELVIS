
# SparseMatrix Class

## Overview

The `SparseMatrix` class provides a Python implementation to handle operations on sparse matrices, which contain mostly zero values. This implementation optimizes memory usage by storing only the non-zero values and allows common matrix operations such as addition, subtraction, and multiplication.

## Features

- **Matrix Loading**: Load sparse matrices from files containing the matrix dimensions and non-zero values.
- **Matrix Operations**: Supports addition, subtraction, and multiplication of two sparse matrices.
- **Matrix Manipulation**: Set and get elements of the sparse matrix efficiently.
- **File Output**: Save the resulting sparse matrix back to a file after performing operations.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

Simply download or clone the repository containing the `SparseMatrix` class. No additional libraries are required for basic functionality.

### Usage

You can create instances of `SparseMatrix` either by loading data from a file or by initializing an empty matrix with given dimensions.

#### 1. Loading a matrix from a file

```python
matrix = SparseMatrix(file_path='matrix_file.txt')
```

The file should contain:
- The number of rows and columns in the matrix.
- Non-zero elements in the format `(row, column, value)`.

Example file content:
```
rows=3
cols=3
(0, 0, 5)
(1, 2, 9)
```

#### 2. Performing Matrix Operations

You can add, subtract, or multiply two matrices. Here's how:

```python
matrix1 = SparseMatrix(file_path='matrix1.txt')
matrix2 = SparseMatrix(file_path='matrix2.txt')

# Add matrices
result = matrix1.add(matrix2)

# Subtract matrices
result = matrix1.subtract(matrix2)

# Multiply matrices
result = matrix1.multiply(matrix2)
```

#### 3. Saving a Matrix to a File

You can save the resulting matrix back to a file:

```python
result.save('result_matrix.txt')
```

### Command-line Interaction

A basic command-line interface is provided to let users select matrix operations interactively.

#### Steps:
1. Load two matrices from files.
2. Choose an operation: Add, Subtract, or Multiply.
3. Save the result to a file.

Example:
```
python sparse_matrix.py
Choose an operation:
1. Add Matrices
2. Subtract Matrices
3. Multiply Matrices
Enter 1, 2, or 3: 1
Matrices added.
Enter file name to save the result: result.txt
Result saved to result.txt
```

### Matrix File Format

The input file should adhere to the following format:

```
rows=<number_of_rows>
cols=<number_of_columns>
(row, column, value)
(row, column, value)
...
```

For example:
```
rows=3
cols=3
(0, 0, 5)
(1, 2, 9)
```

### Example

Suppose you have two sparse matrices in `matrix1.txt` and `matrix2.txt`. You can load them, perform an operation, and save the result like this:

```python
matrix1 = SparseMatrix(file_path='matrix1.txt')
matrix2 = SparseMatrix(file_path='matrix2.txt')

result = matrix1.add(matrix2)
result.save('added_matrix.txt')
```

### Exception Handling

- If matrix dimensions do not match for addition or subtraction, the program raises a `ValueError`.
- If you try to multiply matrices with incompatible sizes, a `ValueError` is raised.
- If there is a format error in the matrix input file, an appropriate exception is raised with a descriptive error message.

## By: KAYONGA ELVIS - e.kayonga@alustudent.com
