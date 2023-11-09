#!/usr/bin/python3
""" contains function that draws pascal triangle"""


def pascal_triangle(n):
    """ Draws pascal triangle """
    superlis = [[1]]

    for a in range(n - 1):
        row = [1]
        try:
            for j in range(len(superlis[-1]) - 1):
                row.insert(j + 1, superlis[-1][j] + superlis[-1][j + 1])
        except IndexError:
            row.append(superlis[-1][j])
        row.append(1)
        superlis.append(row)

    return superlis
