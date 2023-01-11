#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in range(len(matrix)):
        new_row = []
        for col in range(len(matrix[row])):
            new_row.append(matrix[row][col] * matrix[row][col])
        new_matrix.append(new_row)
    return (new_matrix)
