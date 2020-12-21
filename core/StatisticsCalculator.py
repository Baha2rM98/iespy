import math
import numpy as np


class StatisticsCalculator:
    @staticmethod
    def mean(data):
        return np.mean(np.array(data))

    @staticmethod
    def variance(data):
        op_data = np.array(data)
        mean = StatisticsCalculator.mean(op_data)
        s = 0
        for i in op_data:
            s += math.pow((i - mean), 2)
        return s / float(data.__len__() - 1)

    @staticmethod
    def standard_deviation(data):
        return math.sqrt(StatisticsCalculator.variance(np.array(data)))
