import math


class MyMath:

    @staticmethod
    def max_of_four(a, b, c, d):
        return max(a, b, c, d)

    @staticmethod
    def min_of_four(a, b, c, d):
        return min(a, b, c, d)

    @staticmethod
    def avg_of_four(a, b, c, d):
        return sum((a, b, c, d)) / 4

    @staticmethod
    def factorial(n):
        return math.factorial(n)