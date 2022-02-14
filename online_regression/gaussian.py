import numpy as np


def pivotForwardElimination(mat_a, mat_b, pivotRow, numOfVar):

    largestRow = pivotRow

    # find index of largest abs value of mat_a[pivotRow -> numOfVar][pivotRow]
    for currRow in range(pivotRow, numOfVar):
        if (abs(mat_a[currRow][pivotRow]) > abs(mat_a[largestRow][pivotRow])):
            largestRow = currRow

    # swap pivotRow with largestRow
    mat_a[[pivotRow, largestRow]] = mat_a[[largestRow, pivotRow]]
    mat_b[[pivotRow, largestRow]] = mat_b[[largestRow, pivotRow]]

    return mat_a, mat_b


def BackSubstitution(mat_a, mat_b, mat_res, numOfVar):

    # back substitution loop, we loop for numOfVar time, from back, 0 index so -1
    for variable in range(numOfVar):
        curr_row = numOfVar - 1 - variable

        divider = mat_a[curr_row][curr_row]

        upper_one = mat_b[curr_row][0]
        upper_two = 0

        if (curr_row < numOfVar - 1):
            for moreRow in range(curr_row + 1, numOfVar):
                upper_two += mat_a[curr_row][moreRow] * mat_res[moreRow][0]

        mat_res[curr_row][0] = (upper_one - upper_two) / divider

    return mat_res


def ForwardElimination(mat_a, mat_b, numOfVar, pivot=True, showall=True):
    for row in range(numOfVar - 1):
        # track variable for printing information
        subStep = 0

        if (showall):
            print("Step: ", row + 1)

        if (pivot):
            mat_a, mat_b = pivotForwardElimination(mat_a, mat_b, row, numOfVar)

        for nextRow in range(row + 1, numOfVar):
            subStep += 1

            multipler = mat_a[nextRow][row] / mat_a[row][row]

            currA_row = mat_a[row] * multipler
            currB_row = mat_b[row] * multipler

            mat_a[nextRow] -= currA_row
            mat_b[nextRow] -= currB_row

            if (showall):
                print("Sub Step: ", subStep)
                with np.printoptions(precision=4, suppress=True):
                    print("Co-efficient Matrix")
                    print(mat_a)
                    print("Constant matrix")
                    print(mat_b)
                print("\n")

    return mat_a, mat_b


def GaussianElimination(mat_a, mat_b, pivot=True, showAll=True):

    mat_a = np.array(mat_a, dtype=np.double)
    mat_b = np.array(mat_b, dtype=np.double)

    numOfVar, numOfCol = mat_a.shape
    mat_res = np.zeros((numOfVar, 1))

    mat_a, mat_b = ForwardElimination(mat_a, mat_b, numOfVar, pivot, showAll)

    mat_res = BackSubstitution(mat_a, mat_b, mat_res, numOfVar)

    return mat_res


def inputMatrix(rows, cols):
    mat_res = np.zeros((rows, cols))

    for r in range(rows):
        # for c in range(cols):
        mat_res[r] = np.array((input().split()))

    return mat_res
