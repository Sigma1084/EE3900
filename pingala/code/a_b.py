from numpy import sqrt

alpha = (1 + sqrt(5)) / 2 + 0j
beta = (1 - sqrt(5)) / 2 + 0j


def a(n: int):
    if n <= 0:
        return 0
    return ((alpha ** n - beta ** n) / (alpha - beta)).real


def b(n: int):
    if n <= 0:
        return 0
    return a(n + 1) + a(n - 1)
