def add(*args):
    # Test for shape of matrices
    matrix_width_set = {len(mat) for mat in args}
    matrix_height_set = {len(row) for mat in args for row in mat}
    if len(matrix_width_set) > 1 or len(matrix_height_set) > 1:
        raise ValueError("Given matrices are not the same size.")

    # Add matrices together
    output = []
    # Create groups of rows that need to be added together and iterate trough them
    for group in zip(*args):
        output.append([sum(p) for p in zip(*group)])
    return output


if __name__ == "__main__":
    print(add([[1, 2, 3], [3, 2, 1]], [[4, 8, 16], [16, 8, 4]], [[1, 1, 1], [1, 1, 1]]))
