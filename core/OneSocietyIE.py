import math
from core.IntervalEstimation import IntervalEstimation


class OneSocietyIE(IntervalEstimation):
    def interval_estimation_for_ratio(self, x, n, alpha):
        alpha = alpha / 2
        p_hat = x / n
        q_hat = 1 - p_hat
        return str(p_hat - (self._z(alpha) * math.sqrt((p_hat * q_hat) / n))) + ' <= p <= ' + str(
            p_hat + (self._z(alpha) * math.sqrt((p_hat * q_hat) / n)))

    def interval_estimation_for_ratio_left(self, x, n, alpha):
        p_hat = x / n
        q_hat = 1 - p_hat
        return str(p_hat - (self._z(alpha) * math.sqrt((p_hat * q_hat) / n))) + ' <= p'

    def interval_estimation_for_ratio_right(self, x, n, alpha):
        p_hat = x / n
        q_hat = 1 - p_hat
        return 'p <= ' + str(p_hat + (self._z(alpha) * math.sqrt((p_hat * q_hat) / n)))

    def interval_estimation_for_mean(self, x_hat, n, standard_deviation, is_sigma, alpha):
        alpha = alpha / 2
        if n >= 30 or is_sigma is True:
            return str(x_hat - ((self._z(alpha) * standard_deviation) / math.sqrt(n))) + ' <= u <= ' + str(
                x_hat + ((self._z(alpha) * standard_deviation) / math.sqrt(n)))
        return str(x_hat - ((self._t((n - 1, alpha)) * standard_deviation) / math.sqrt(n))) + ' <= u <= ' + str(
            x_hat + ((self._t((n - 1, alpha)) * standard_deviation) / math.sqrt(n)))
