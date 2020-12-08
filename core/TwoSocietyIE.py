import math
from core.IntervalEstimation import IntervalEstimation


class TwoSocietyIE(IntervalEstimation):
    def interval_estimation_for_ratio(self, x1, n1, x2, n2, alpha):
        alpha = alpha / 2
        p1_hat = x1 / n1
        p2_hat = x2 / n2
        q1_hat = 1 - p1_hat
        q2_hat = 1 - p2_hat
        return str((p1_hat - p2_hat) - (self._z(alpha) * math.sqrt(
            ((p1_hat * q1_hat) / n1) + ((p2_hat * q2_hat) / n2)))) + ' <= p1-p2 <= ' + str(
            (p1_hat - p2_hat) + (self._z(alpha) * math.sqrt(
                ((p1_hat * q1_hat) / n1) + ((p2_hat * q2_hat) / n2))))
