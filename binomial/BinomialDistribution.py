import math

class BinomialDistribution:
    """
        Distribution: P(X = k) = (n choose k) * p^k * (1 - p)^(n - k)

        Class to represent a given number of binary independent, number of successes, and probability of success

        Parameters:
            n: number of trials
            k: number of successful trials
            p: probability of success

        Functions:
            public:
                calc_prob: returns probability P of getting K successes in n independent trials
                coeff: returns number of n events with k chosen

            private:

    """

    def __init__(self, n: int, k: int, p: float):
        self.n = n
        self.k = k
        self.p = p

    def calculate(self) -> float:
        """
            Calculates probability of distribution

        :return:
            The probability of distribution
        """

        coeff = self.coeff(self.n, self.k)
        q = 1.0 - self.p # q is often represented as prob of failure

        return coeff * pow(self.p, self.k) * pow(q, (self.n - self.k))

    def coeff(self, n: int, k: int) -> int:
        """
            function to calculate Binomial Coefficient
        :param n: number of elements
        :param k: number of chosen
        :return: number of combinations
        """
        return math.factorial(n) / (math.factorial(n - k) * math.factorial(k))