import math
import numpy as np
from core import StatisticsCalculator


class CorrelationCoefficient:
    @staticmethod
    def pearson(x, y):
        n = x.__len__()
        if n != y.__len__():
            raise IndexError('The length of vector x and y are not equal.')
        mean_x = StatisticsCalculator.mean(x)
        mean_y = StatisticsCalculator.mean(y)
        numerator_sum = 0
        denominator_as_x_sum_temp = 0
        denominator_as_y_sum_temp = 0
        for i in range(0, n):
            numerator_sum += ((x[i] - mean_x) * (y[i] - mean_y))
            denominator_as_x_sum_temp += (x[i] - mean_x) ** 2
            denominator_as_y_sum_temp += (y[i] - mean_y) ** 2
        return numerator_sum / math.sqrt(denominator_as_x_sum_temp * denominator_as_y_sum_temp)

    @staticmethod
    def spearman_rank(x, y):
        n = x.__len__()
        if n != y.__len__():
            raise IndexError('The length of vector x and y are not equal.')
        op_x = np.array(x)
        op_y = np.array(y)
        sorted_x = np.sort(op_x)
        sorted_y = np.sort(op_y)
        r = np.zeros((n,), dtype=int)
        s = np.zeros((n,), dtype=int)
        for i in range(0, n):
            for j in range(0, n):
                if sorted_x[j] == op_x[i]:
                    r[i] = j
        for i in range(0, n):
            for j in range(0, n):
                if sorted_y[j] == op_y[i]:
                    s[i] = j
        d = np.zeros((n,), dtype=int)
        for i in range(0, n):
            d[i] = r[i] - s[i]
        for i in range(0, n):
            d[i] = d[i] ** 2
        return 1 - ((6 * d.sum()) / (n * ((n ** 2) - 1)))

    @staticmethod
    def partial(x, y, z, kind='pearson'):
        if kind == 'pearson':
            rXY = CorrelationCoefficient.pearson(x, y)
            rXZ = CorrelationCoefficient.pearson(x, z)
            rYZ = CorrelationCoefficient.pearson(y, z)
            rZY = CorrelationCoefficient.pearson(z, y)
            rYX = CorrelationCoefficient.pearson(y, x)
            rZX = CorrelationCoefficient.pearson(z, x)
            return {
                'XY.Z': ((rXY - (rXZ * rYZ)) / (math.sqrt((1 - rXZ ** 2) * (1 - rYZ ** 2)))),
                'XZ.Y': ((rXZ - (rXY * rZY)) / (math.sqrt((1 - rXY ** 2) * (1 - rZY ** 2)))),
                'YZ.X': ((rYZ - (rYX * rZX)) / (math.sqrt((1 - rYX ** 2) * (1 - rZX ** 2))))
            }
        if kind == 'spearman':
            rXY = CorrelationCoefficient.spearman_rank(x, y)
            rXZ = CorrelationCoefficient.spearman_rank(x, z)
            rYZ = CorrelationCoefficient.spearman_rank(y, z)
            rZY = CorrelationCoefficient.spearman_rank(z, y)
            rYX = CorrelationCoefficient.spearman_rank(y, x)
            rZX = CorrelationCoefficient.spearman_rank(z, x)
            return {
                'XY.Z': ((rXY - (rXZ * rYZ)) / (math.sqrt((1 - rXZ ** 2) * (1 - rYZ ** 2)))),
                'XZ.Y': ((rXZ - (rXY * rZY)) / (math.sqrt((1 - rXY ** 2) * (1 - rZY ** 2)))),
                'YZ.X': ((rYZ - (rYX * rZX)) / (math.sqrt((1 - rYX ** 2) * (1 - rZX ** 2))))
            }
        raise NameError("Undefined kind: " + kind)
