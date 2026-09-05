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
                mean: distribution mean
                std: distribution standard deviation

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

    def coeff(self, n: int = None, k: int = None) -> int:
        """
            function to calculate Binomial Coefficient
        :param n: number of elements
        :param k: number of chosen
        :return: number of combinations
        """
        if n is None: n = self.n
        if k is None: k = self.k

        return math.factorial(n) / (math.factorial(n - k) * math.factorial(k))

    def mean(self, n: int = None, p: float = None) -> float:
        """
            Calculates mean of binomial distribution
            μ = n * p

        :param n: number of trials
        :param p: probability of successful events
        :return: mean of distribution
        """
        if n is None: n = self.n
        if p is None: p = self.p

        return n * p

    def std(self, n: int = None, p: float = None) -> float:
        """
            Calculates standard deviation of binomial distribution
            σ = √(n * p * (1 - p))

        :param n: number of trials
        :param p: probability of successful events
        :return: standard deviation of distribution
        """
        if n is None: n = self.n
        if p is None: p = self.p

        return math.sqrt(n * p * (1 - p))