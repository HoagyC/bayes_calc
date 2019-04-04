from math import factorial

test_total = 40
test_correct = 25
control_total = 30
control_correct = 15


def comb(n, k):
    return factorial(n) / factorial(k) / factorial(n - k)


def test_bin(n, k, x):
    return comb(n, k)*x**k*(1-x)**(n-k)


def test_diff(x, e, tt, tc, ct, cc):
    return test_bin(tt, tc, x)*test_bin(ct, cc, x-e)


def main_test(n):
    sum()


print (main_test(50))