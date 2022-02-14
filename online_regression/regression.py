import numpy as np
import gaussian
import bisection


def linear_reg(Xarr, Yarr, special_case=False):
    #model: y = a_0 + a_1 * x
    Xarr = np.array(Xarr)
    Yarr = np.array(Yarr)
    total_points = Xarr.size

    # sums for a_0 and a_1
    sum_X = np.sum(Xarr)
    sum_Y = np.sum(Yarr)
    sumX_sq = np.sum(np.square(Xarr, dtype=np.double))
    sumY_sq = np.sum(np.square(Yarr, dtype=np.double))
    sumXY = np.sum((Xarr * Yarr))

    # co-efficients calculation
    lower = (total_points * sumX_sq - sum_X * sum_X)
    a_1 = (total_points * sumXY - sum_X * sum_Y) / lower
    a_0 = (sumX_sq * sum_Y - sum_X * sumXY) / lower
    special_case_a = (sumXY) / (sumX_sq)

    if (special_case):
        return special_case_a

    # # print(Xarr, Yarr)
    # print(sum_Y)
    # print(sumXY)
    # print(sumX_sq)
    return a_0, a_1


def exponential_reg(Xarr, Yarr):
    #model: y = a * (e ^ (b * x))
    Xarr = np.array(Xarr)
    Yarr = np.array(Yarr)

    error = 0.000000005
    iter = 250

    # co-efficients
    # we have to find upper and lower bound for bisection by plotting given points
    # current bound for book example 🤲
    b = bisection.bisection(-0.120, -0.110, error, iter, Xarr, Yarr)

    e_bxi = np.power(np.exp(Xarr), b, dtype=np.double)
    e_2bxi = np.power(np.exp(Xarr), 2 * b, dtype=np.double)
    Yi_ebxi = np.sum(Yarr * e_bxi)

    e_2bxi = np.sum(e_2bxi)

    a = (Yi_ebxi / e_2bxi)

    return a, b


def polynomial_reg(Xarr, Yarr, order):
    # model: mth order polynomial
    #  y = a_0 + a_1 * x + a_2 * x^2 + a_3 * x^3 + ... + a_m * x^m
    Xarr = np.array(Xarr)
    Yarr = np.array(Yarr)
    total_points = Xarr.size

    coefficient_mat = np.zeros((order+1, order+1), dtype=np.double)
    constant_mat = np.zeros((order + 1, 1), dtype=np.double)

    # fill up coefficient matrix
    # first row special case:
    for row in range(order+1):
        for col in range(order+1):
            if (row == 0 and col == 0):
                coefficient_mat[0][0] = total_points
            else:
                coefficient_mat[row][col] = np.sum(
                    np.power(Xarr, row + col, dtype=np.double))

    # fill up constant matrix
    for row in range(order+1):
        constant_mat[row][0] = np.sum((Yarr * np.power(Xarr, row)))

    # print(coefficient_mat)
    # print(constant_mat)
    # print(np.sum(np.power(Xarr, 2*order, dtype=np.double)))
    return gaussian.GaussianElimination(coefficient_mat, constant_mat, pivot=True, showAll=False)
