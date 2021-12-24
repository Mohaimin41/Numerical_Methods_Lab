import numpy as np

# we set printOption for numpy globally as 4 digits after decimal
# np.set_printoptions(formatter={'float': '{: 0.4f}'.format})
# np.set_printoptions(precision=4)

def pivotForwardElimination(mat_a, mat_b, pivotRow, numOfVar):

    largestRow = pivotRow

    #find index of largest abs value of mat_a[pivotRow -> numOfVar][pivotRow]
    for currRow in range(pivotRow, numOfVar):
        if (abs(mat_a[currRow][pivotRow]) > abs(mat_a[largestRow][pivotRow])):
            largestRow = currRow

    #swap pivotRow with largestRow
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

        if (pivot):
            mat_a, mat_b = pivotForwardElimination(mat_a, mat_b, row, numOfVar)

        for nextRow in range(row + 1, numOfVar):
            multipler = mat_a[nextRow][row] / mat_a[row][row]

            currA_row = mat_a[row] * multipler
            currB_row = mat_b[row] * multipler

            mat_a[nextRow] -= currA_row
            mat_b[nextRow] -= currB_row

        if (showall):
            with np.printoptions(precision=4, suppress=True):
                print(mat_a)
                print(mat_b)

    return mat_a, mat_b


def GaussianElimination(mat_a, mat_b, pivot=True, showAll=True):

    mat_a = np.array(mat_a, dtype=np.double)
    mat_b = np.array(mat_b, dtype=np.double)

    #mat_res = np.array(dtype=np.double )

    numOfVar, numOfCol = mat_a.shape
    mat_res = np.zeros((numOfVar, 1))

    mat_a, mat_b = ForwardElimination(mat_a, mat_b, numOfVar)

    mat_res = BackSubstitution(mat_a, mat_b, mat_res, numOfVar)

    return np.around(mat_res, 4)


def inputMatrix(rows, cols):
    mat_res = np.zeros((rows, cols))

    for r in range(rows):
        # for c in range(cols):
        mat_res[r] = np.array((input().split()))
    
    return mat_res


# mat_a = np.array([[25, 5, 1], [64, 8, 1], [144, 12, 1]])
# # mat_a = np.array([[10, -7, 0], [-3, 2.099, 6], [5, -1, 5]])
# mat_a = np.array([[20, 15, 10], [-3, -2.249, 7], [5, 1, 3]])

# mat_b = np.array([[106.8], [177.2], [279.2]])
# # mat_b = np.array([[7], [3.901], [6]])
# mat_b = np.array([[45], [1.751], [9]])

# print(mat_a, mat_b)
# print(mat_a.shape, mat_b.shape)
variables = int(input())

mat_a = inputMatrix(variables, variables)
mat_b = inputMatrix(variables, 1)

result = GaussianElimination(mat_a, mat_b)


with np.printoptions(formatter={'float': '{: 0.4f}'.format}, suppress=True):
    print("Result\n", result)