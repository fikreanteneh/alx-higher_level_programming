#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        k = len(i)
        for j in range(k):
            if j <  k - 1:
                print(i[j], end = ' ')
                continue
            print(i[j])