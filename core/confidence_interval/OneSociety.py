import math
from core.confidence_interval.ConfidenceInterval import ConfidenceInterval


class OneSociety(ConfidenceInterval):
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
            return str(x_hat - ((self._z(alpha) * standard_deviation) / math.sqrt(n))) + ' <= μ <= ' + str(
                x_hat + ((self._z(alpha) * standard_deviation) / math.sqrt(n)))
        return str(x_hat - ((self._t((n - 1, alpha)) * standard_deviation) / math.sqrt(n))) + ' <= μ <= ' + str(
            x_hat + ((self._t((n - 1, alpha)) * standard_deviation) / math.sqrt(n)))

    def interval_estimation_for_variance(self, standard_deviation, n, alpha):
        alpha = alpha / 2
        return str(((n - 1) * standard_deviation ** 2) / self._x((n - 1, alpha))) + ' <= σ^2 <= ' + str(
            ((n - 1) * standard_deviation ** 2) / self._x((n - 1, 1 - alpha)))

    def interval_estimation_for_standard_deviation(self, standard_deviation, n, alpha):
        alpha = alpha / 2
        return str(math.sqrt(((n - 1) * standard_deviation ** 2) / self._x((n - 1, alpha)))) + ' <= σ <= ' + str(
            math.sqrt(
                ((n - 1) * standard_deviation ** 2) / self._x((n - 1, 1 - alpha))))

    def sample_size_for_ratio(self, E, alpha, p_hat=None, N=None):
        alpha = alpha / 2
        if N is None:
            if p_hat is None:
                return math.floor(0.25 * (self._z(alpha) / E) ** 2) + 1
            q_hat = 1 - p_hat
            return math.floor(p_hat * q_hat * (self._z(alpha) / E) ** 2) + 1
        if p_hat is None:
            return math.floor((N * self._z(alpha) ** 2 * 0.25) / ((N - 1) * E ** 2 + self._z(alpha) ** 2 * 0.25)) + 1
        q_hat = 1 - p_hat
        return math.floor(
            (N * self._z(alpha) ** 2 * p_hat * q_hat) / ((N - 1) * E ** 2 + self._z(alpha) ** 2 * p_hat * q_hat)) + 1

    def sample_size_for_mean(self, E, alpha, sigma, N=None):
        alpha = alpha / 2
        if N is None:
            return math.floor((self._z(alpha) * sigma / E) ** 2) + 1
        return math.floor(
            (N * self._z(alpha) ** 2 * sigma ** 2) / ((N - 1) * E ** 2 + self._z(alpha) ** 2 * sigma ** 2)) + 1
