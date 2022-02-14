from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import regression as reg


# linear regression example
angle = [0.698132, 0.959931, 1.134464, 1.570796, 1.919862]
torque = [0.188224, 0.209138, 0.230052, 0.250965, 0.313707]
# (k_1, k_2) = reg.linear_reg(angle, torque)
# print(k_1, k_2)

# exponential regression example
time = [0, 1, 3, 5, 7, 9]
radiation = [1.000, 0.891, 0.708, 0.562, 0.447, 0.355]
# (a, b) = reg.exponential_reg(time, radiation)
# plt.title("Experimental Datas vs Solved Curve")
# plt.xlabel("time")
# plt.ylabel("Relative Radiation")

# plt.scatter(np.array(time), np.array(radiation), color="green")
# # plt.plot(np.array(time), np.array(radiation), color="green")

# plt.plot(np.array(time), a * np.exp(b * np.array(time)), color="red")

# plt.show()


# transformation to linear
ln_radiation = np.log(np.array(radiation))
(lna, b) = reg.linear_reg(time, ln_radiation)
# a = np.exp(lna)
# print(a, b)

# polynomial regression example
temp = [80, 40, -40, -120, -200, -280, -340]
coeff_thermal_expansion = np.array(
    [6.47, 6.24, 5.72, 5.09, 4.30, 3.33, 2.45]) * 1e-6
result = reg.polynomial_reg(temp, coeff_thermal_expansion, 2)
print(result)

plt.title("Experimental Datas vs Solved Curve")
plt.xlabel("temp")
plt.ylabel("thermal expansion coefficient")

plt.scatter(np.array(temp), np.array(coeff_thermal_expansion), color="green")
# plt.plot(np.array(time), np.array(radiation), color="green")

plt.plot(np.array(temp), result[0][0] + result[1][0] * np.array(temp) 
                        + result[2][0] * np.array(temp) * np.array(temp),
                         color="red")

plt.show()
