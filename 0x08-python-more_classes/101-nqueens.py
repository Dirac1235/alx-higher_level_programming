#!/usr/bin/python3
import sys


def list_checker(arr):
    def is_diagonal(point1, point2):
        return abs(point1[0] - point2[0]) == abs(point1[1] - point2[1])

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i][0] == arr[j][0] or arr[i][1] == arr[j][1]:
                return False
            if is_diagonal(arr[i], arr[j]):
                return False
    return True


def create_grid(grid_size):
    result = []
    for i in range(grid_size):
        row = []
        for j in range(grid_size):
            row.append([i, j])
        result.append(row)
    return result


super_list = []
super_super_list = []


def alg2(arr, size):
    global super_list, super_super_list
    i = 0
    if arr == []:
        return super_super_list

    for arr1 in arr:
        for lis in arr1:
            super_list.append(lis)
            if list_checker(super_list):
                if list_checker(super_list) and len(super_list) == size:
                    super_super_list.append(super_list.copy())
                alg2(arr[1:], size)
                super_list.pop()
            elif i < size:
                super_list.pop()
                i += 1
            else:
                super_list.pop()
                return

    return super_super_list


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    for i in alg2(create_grid(int(sys.argv[1])), int(sys.argv[1])):
        print(i)
