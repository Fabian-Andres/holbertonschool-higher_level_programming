def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for row in range(len(matrix[i])):
            if row != (len(matrix) - 1):
                print("{:d}".format(matrix[i][row]), end=" ")
            else:
                print("{:d}".format(matrix[i][row]), end="")
        print()
