from a_b import *


def verify_a():
    # Runs into round off errors for bigger values
    N = int(70)

    # Verifying for the first N terms
    sn = round(a(0))
    for n in range(1, N+1):
        sn += round(a(n))
        assert (sn == round(a(n+2)) - 1)

    print(f"Summation a(k) = a(n+2) - 1 verified for the first {N} terms")
    print()


def verify_a_sum():
    lhs = 0
    N = int(100)
    for k in range(1, N+1):
        lhs += a(k) / 10**k
    rhs = 10 / 89
    print(f"Summation a(k)/10^k ({N} terms):", lhs)
    print(f"10/89:", rhs)
    print(f"Difference:", lhs - rhs)
    print()


def verify_b():
    # Runs into round off errors for bigger values
    N = int(70)

    # Verifying for the first N terms
    for n in range(1, N+1):
        assert (round(b(n)) == round((alpha**n + beta**n).real))

    print(f"Summation b(k) = a(n+1) + a(n-1) verified for the first {N} terms")
    print()


def verify_b_sum():
    lhs = 0
    N = int(100)
    for k in range(1, N+1):
        lhs += b(k) / 10**k
    rhs = 12 / 89
    print(f"Summation b(k)/10^k ({N} terms):", lhs)
    print(f"12/89:", rhs)
    print(f"Difference:", lhs - rhs)
    print()


if __name__ == '__main__':
    verify_a()
    verify_a_sum()
    verify_b()
    verify_b_sum()
