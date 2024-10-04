class SparseMatrix:
    def __init__(self, file_path=None, rows=None, cols=None):
        # Load matrix from file or initialize an empty one
        if file_path:
            self.matrix = self._load_from_file(file_path)
        else:
            self.matrix = {}
            self.row_count = rows
            self.col_count = cols

    def _load_from_file(self, path):
        matrix = {}
        try:
            with open(path, 'r') as f:
                # Extract matrix dimensions
                self.row_count = int(f.readline().split('=')[1].strip())
                self.col_count = int(f.readline().split('=')[1].strip())

                # Parse matrix entries (row, col, value)
                for line in f:
                    if line.strip():  # Skip empty lines
                        row, col, value = self._parse_line(line)
                        if row not in matrix:
                            matrix[row] = {}
                        matrix[row][col] = value

        except Exception as ex:
            raise ValueError(f"File format error: {ex}")
        
        return matrix

    def _parse_line(self, line):
        # Extract row, col, value from line
        content = line.strip()[1:-1].split(',')
        return int(content[0]), int(content[1]), int(content[2])

    def get_value(self, row, col):
        return self.matrix.get(row, {}).get(col, 0)

    def set_value(self, row, col, value):
        if row not in self.matrix:
            self.matrix[row] = {}
        self.matrix[row][col] = value

    def add(self, other):
        result = SparseMatrix(rows=self.row_count, cols=self.col_count)
        
        for r in range(self.row_count):
            for c in range(self.col_count):
                sum_value = self.get_value(r, c) + other.get_value(r, c)
                result.set_value(r, c, sum_value)
        
        return result

    def subtract(self, other):
        result = SparseMatrix(rows=self.row_count, cols=self.col_count)
        
        for r in range(self.row_count):
            for c in range(self.col_count):
                diff_value = self.get_value(r, c) - other.get_value(r, c)
                result.set_value(r, c, diff_value)
        
        return result

    def multiply(self, other):
        if self.col_count != other.row_count:
            raise ValueError("Matrix sizes incompatible for multiplication")
        
        result = SparseMatrix(rows=self.row_count, cols=other.col_count)
        
        for r in self.matrix:
            for c in other.matrix:
                if c in self.matrix[r]:
                    product = sum(self.get_value(r, k) * other.get_value(k, c) for k in range(self.col_count))
                    result.set_value(r, c, product)

        return result

    def save(self, file_path):
        with open(file_path, 'w') as f:
            f.write(f"rows={self.row_count}\n")
            f.write(f"cols={self.col_count}\n")
            for r in self.matrix:
                for c, val in self.matrix[r].items():
                    f.write(f"({r}, {c}, {val})\n")


# Script execution block for user interaction
if __name__ == "__main__":
    # Load matrices from files
    mat1 = SparseMatrix(file_path='./easy_sample_01_3.txt')
    mat2 = SparseMatrix(file_path='./easy_sample_03_1.txt')

    # User selects an operation
    print("Select an operation:")
    print("1. Add Matrices")
    print("2. Subtract Matrices")
    print("3. Multiply Matrices")
    option = int(input("Enter 1, 2, or 3: "))

    # Execute the chosen operation
    if option == 1:
        result_matrix = mat1.add(mat2)
        print("Matrices added.")
    elif option == 2:
        result_matrix = mat1.subtract(mat2)
        print("Matrices subtracted.")
    elif option == 3:
        result_matrix = mat1.multiply(mat2)
        print("Matrices multiplied.")
    else:
        print("Invalid choice.")

    # Save the result to a file
    output = input("Enter file name to save the result: ")
    result_matrix.save(output)
    print(f"Result saved to {output}.")
