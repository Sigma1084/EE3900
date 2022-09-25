import numpy as np


def h(n):
    ans = 0
    if n >= 0: ans += (-0.5)**n
    if n >= 2: ans += (-0.5)**(n-2)
    return ans


def sum():
    ans = 0
    N = 100000
    for i in range(N):
        ans += h(i)
    return ans


if __name__ == '__main__':
    print(sum())
