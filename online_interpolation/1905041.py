import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def absoluteRelativeApproxError(currentVal, prevVal):
    return abs((currentVal - prevVal)/currentVal) * 100


def nearestPoints(pointsArray, givenPoint, orderOfInterpolation):
    nearest = []

    nearestIdx = -1

    for idx in range(len(pointsArray)):
        if givenPoint < pointsArray[idx][0]:
            nearestIdx = idx - 1
            break

    if (nearestIdx - int(orderOfInterpolation / 2) < 0 or nearestIdx + int(orderOfInterpolation / 2) > len(pointsArray)-1):
        if nearestIdx - int(orderOfInterpolation / 2) < 0:
            for idx in range(orderOfInterpolation):
                nearest.append(pointsArray[idx])

        else:
            for idx in range(orderOfInterpolation):
                nearest.append(
                    pointsArray[len(pointsArray) - orderOfInterpolation + idx])
    else:
        if orderOfInterpolation % 2 != 0:
            nearest.append(
                pointsArray[nearestIdx - int(orderOfInterpolation / 2)])

        for idx in range(0, int(orderOfInterpolation / 2)):
            nearest.append(
                pointsArray[nearestIdx - int(orderOfInterpolation / 2) + idx + 1])

        for idx in range(0, int(orderOfInterpolation / 2)):
            nearest.append(pointsArray[nearestIdx + idx + 1])

    return nearest


def coefficients(leftIndex, rightIndex, points):
    # coef = np.zeros(len(points))
    if leftIndex == rightIndex:
        return points[leftIndex][1]
    else:
        returnVal = coefficients(leftIndex, rightIndex - 1, points) - \
            coefficients(leftIndex + 1, rightIndex, points)
        returnVal /= (points[leftIndex][0] - points[rightIndex][0])

        return returnVal


def newton(points, abscissa):
    order = len(points)
    functionSum = 0.0

    for i in range(order):
        temp = coefficients(0, i, points)

        for j in range(i):
            temp *= (abscissa - points[j][0])

        functionSum += temp

    return functionSum


# fileData = pd.read_csv("dissolveO2.csv")
# fileData['temparature', 'solubility_1', 'solubility_2'].values

df = pd.read_csv('dissolveO2.csv')

data_list = df.T.values.tolist()

data_list = np.transpose(np.array(data_list))

inputPointsArray1 = data_list[:, [0, 1]]
inputPointsArray2 = data_list[:, [0, 2]]

abscissaOfPoint = int(input())
# print(inputPointsArray1, inputPointsArray2)

ans1bar = newton(nearestPoints(
    inputPointsArray1, abscissaOfPoint, 4), abscissaOfPoint)

ans2bar = newton(nearestPoints(
    inputPointsArray2, abscissaOfPoint, 4), abscissaOfPoint)

print("For pressure 1 bar: ",ans1bar )


print("For pressure 2 bar: ", ans2bar)


print("Absolute relative approximate error with cubic interpolation\n")
print("Pressure 1 bar: ", absoluteRelativeApproxError(ans1bar,
                                                      newton(nearestPoints(inputPointsArray1, abscissaOfPoint, 3), abscissaOfPoint)))
print("Pressure 2 bar:", absoluteRelativeApproxError(ans2bar,
                                                     newton(nearestPoints(inputPointsArray2, abscissaOfPoint, 3), abscissaOfPoint)))


xaxis = inputPointsArray2[:, [0]]
yaxis1 = inputPointsArray1[:, [1]]
yaxis2 = inputPointsArray2[:, [1]]

plt.plot(abscissaOfPoint, ans2bar, 'ro')
plt.plot(abscissaOfPoint, ans1bar, 'ro')
# plt.scatter(xaxis, yaxis1)
plt.plot(xaxis,yaxis1)
plt.plot(xaxis, yaxis2)
plt.show()