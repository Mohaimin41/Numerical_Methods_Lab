import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate


def absRelApproxError(curr, prev):
    return abs((curr - prev) / curr) * 100


def func(x):
    C_me = 5e-4
    upper = 6.73 * x + 6.725e-8 + 7.26e-4 * C_me
    lower = 3.62e-12 * x + 3.908e-8 * x * C_me
    return - upper/lower


def trapezoidal(start, end, intervals):
    h = (end - start) / intervals

    ans = (h / 2) * (func(start) + func(end))

    for i in range(1, intervals):  # 1 to n-1
        ans += (h/2) * 2 * func(start + i * h)

    return ans


def simpsons(start, end, intervals):
    intervals *= 2
    h = (end - start) / intervals

    ans = h * (func(start) + func(end))

    for i in range(1, intervals):  # 1 to n-1

        if (i % 2 == 1): # if i odd
            ans += h * 4 * func(start + i * h)
        else:
            ans += h * 2 * func(start + i * h)

    return ans / 3.0


init_conc = 1.22e-4

print("\n\t\t\t\tProblem 1\nPlease enter number of sub-intervals: ")

user_interval = int(input())

print("Time required for 50 percent of initial oxygen to be consumed: ",
      trapezoidal(init_conc, init_conc/2.0, user_interval), "seconds")


results = []

print("\nResults and absolute relative approximate errors for n = 1 to 5\n")

for i in range(5):

    if (i == 0):
        results.append([i+1, trapezoidal(init_conc, init_conc/2.0, i + 1),
                        ])
    else:
        results.append([i+1, trapezoidal(init_conc, init_conc/2.0, i + 1),
                        absRelApproxError(trapezoidal(init_conc, init_conc/2.0, i + 1),
                                          trapezoidal(init_conc, init_conc / 2.0, i))
                        ]
                       )

print(tabulate(results,
               headers=["n", "Result", "Absolute Relative Approximation Error"]))

#               PROBLEM 2

print("\n\t\t\t\tProblem 2\nPlease enter number of sub-intervals (n): ")

user_interval = int(input())

print("Time required for 50 percent of initial oxygen to be consumed: ",
      simpsons(init_conc, init_conc/2.0, user_interval), "seconds")


results = []

print("\nResults and absolute relative approximate errors for n = 1 to 5\n")

for i in range(5):

    if (i == 0):
        results.append([i+1, simpsons(init_conc, init_conc/2.0, i + 1),
                        ])
    else:
        results.append([i+1, simpsons(init_conc, init_conc/2.0, i + 1),
                        absRelApproxError(simpsons(init_conc, init_conc/2.0, i + 1),
                                          simpsons(init_conc, init_conc / 2.0, i))
                        ]
                       )

print(tabulate(results,
               headers=["n", "Result", "Absolute Relative Approximation Error"]))


#                           PROBLEM 3
print("\n\t\t\t\tProblem 3\n")

oxygen_conc = np.array([1.22, 1.20, 1.0, 0.8, 0.6, 0.4, 0.2]) * 1e-4

time = []

for i in range(len(oxygen_conc)):
    time.append(simpsons(init_conc, oxygen_conc[i], 10))

time = np.array(time)
# print(time)
# print(oxygen_conc)

plt.plot(oxygen_conc, time, marker = 'o')
plt.xlabel("Oxygen concentration (moles/cm^3)")
plt.ylabel("Time (seconds)")
plt.title("Consumption of oxygen over time in methanol-based fuel cell")
plt.grid()
plt.show()
