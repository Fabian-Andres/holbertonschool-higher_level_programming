def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in range(0, len(matrix)):
            for row in range(0, len(matrix[i])):
                if row != (len(matrix) - 1):
                    print("{:d}".format(matrix[i][row]), end=" ")
                else:
                    print("{:d}".format(matrix[i][row]), end="")
            print()
