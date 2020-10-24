import math


class StatisticsCalculator:
    @staticmethod
    def mean(data):
        return sum(data) / data.__len__()

    @staticmethod
    def variance(data):
        m = StatisticsCalculator.mean(data)
        s = 0
        for i in data:
            s += math.pow((i - m), 2)
        return s / float(data.__len__() - 1)

    @staticmethod
    def standard_deviation(data):
        return math.sqrt(StatisticsCalculator.variance(data))
