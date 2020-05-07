#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        new_matrix = []
        for i in range(len(matrix)):
            new_matrix_row = []
            for y in range(len(matrix[i])):
                new_matrix_row.append(matrix[i][y]**2)
            new_matrix.append(new_matrix_row)
        return new_matrix
