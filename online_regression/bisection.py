import numpy as np


# fx method for exponential regression
def fx(x, Xarr, Yarr):
    Xarr = np.array(Xarr)
    Yarr = np.array(Yarr)

    # co-efficient of exponential model eqn
    e_bxi = np.power(np.exp(Xarr), x, dtype=np.double)
    e_2bxi = np.power(np.exp(Xarr), 2 * x, dtype=np.double)
    XiYi_ebxi = np.sum((Xarr*Yarr) * e_bxi)

    Xi_e2bxi = np.sum(Xarr * e_2bxi)

    Yi_ebxi = np.sum(Yarr * e_bxi)

    e_2bxi = np.sum(e_2bxi)

    return XiYi_ebxi - (Yi_ebxi / e_2bxi) * Xi_e2bxi


# Bisection method
def bisection(lower_bound, upper_bound, approx_error, max_iter, Xarr, Yarr):
    root = 0
    error = 100
    iter = 0

    Xarr = np.array(Xarr)
    Yarr = np.array(Yarr)

    while ((error > approx_error) and (iter <= max_iter)):
        iter += 1

        root = (lower_bound + upper_bound) / 2.0
        if(iter > 1):
            error = abs((root - prev_root) / root) * 100

        prev_root = root

        if (fx(root, Xarr, Yarr) * fx(lower_bound, Xarr, Yarr) < 0):
            upper_bound = root
        elif (fx(root, Xarr, Yarr) * fx(lower_bound, Xarr, Yarr) > 0):
            lower_bound = root
        else:
            break

    return root
