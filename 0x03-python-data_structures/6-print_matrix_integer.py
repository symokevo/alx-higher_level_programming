#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]),
                  end=" " if matrix[i][j] != matrix[i][-1] else "")
        print()
