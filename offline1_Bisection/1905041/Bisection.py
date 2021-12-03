import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# Plot f(x)
x = np.array(np.arange(0, .12, .001))
y = np.array((x**3) - 0.18 * (x**2) + 4 * (0.06**3) * 0.55)

plt.plot(x, y)
plt.xlabel("x = [0, 0.12], step = 0.001")
plt.ylabel("y = (x**3) - 0.18 * (x**2) + 4 * (0.06 ** 3) * 0.55")
plt.title("Plot of f(x) = (x**3) - 0.18 * (x**2) + 4 * (0.06 ** 3) * 0.55 = 0")
plt.show()


# f(x) method
def fx(x):
    return (x**3) - 0.18 * (x**2) + 4 * (0.06**3) * 0.55


# Bisection method
def bisection(lower_bound, upper_bound, approx_error, max_iter):
    root = 0
    error = 100
    iter = 0

    while ((error > approx_error) | (iter <= max_iter)):
        iter += 1

        root = (lower_bound + upper_bound) / 2.0
        if(iter > 1):
            error = abs((root - prev_root) / root) * 100     

        prev_root = root

        if (fx(root) * fx(lower_bound) < 0):
            upper_bound = root
        elif (fx(root) * fx(lower_bound) > 0):
            lower_bound = root
        else:
            break
        
    return root

# Bisection with table
def bisection_table(lower_bound, upper_bound, approx_error, max_iter):
    root = 0
    error = 100
    iter = 0

    error_table = []

    while ((error > approx_error) | (iter <= max_iter)):
        iter += 1

        root = (lower_bound + upper_bound) / 2.0
        if(iter > 1):
            error = abs((root - prev_root) / root) * 100
        prev_root = root

        if(iter <= 20):
            error_table.append([iter,error])

        if (fx(root) * fx(lower_bound) < 0):
            upper_bound = root
        elif (fx(root) * fx(lower_bound) > 0):
            lower_bound = root
        else:
            break

    return root, error_table


print("Value of x is(absolute relative approximation error < 0.5 ): ", bisection(0, 0.12, 0.5, 100))

(root, table) = bisection_table(0, 0.12, 0.5, 20)
print(tabulate(table, headers=["Iteration","Absolute Relative Approximation Error"]))
