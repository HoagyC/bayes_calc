from math import factorial

test_total = 40
test_correct = 25
control_total = 30
control_correct = 15

def frange(x, y, jump):
  while x < y:
    yield x
    x += jump

def comb(n, k):
    return factorial(n) / factorial(k) / factorial(n - k)


def test_bin(n, k, x):
    return comb(n, k)*x**k*(1-x)**(n-k)


def test_diff(x, e, tt, tc, ct, cc):
    return test_bin(tt, tc, x)*test_bin(ct, cc, x-e)


def hyp_test(n, e, tt, tc, ct, cc):
    total = 0
    total += test_diff(1, e, tt, tc, ct, cc)
    for i in frange(e, 1, (1-e)/n):
        total += test_diff(i, e, tt, tc, ct, cc)
    total -= test_diff(e, e, tt, tc, ct, cc)
    return total


def main_test(n, m, tt, tc, ct ,cc):
    for i in frange(-1, 1, 1/m):
        print('posterior for difference of', i, 'is', hyp_test(n, i, tt, tc, ct, cc))

# n = fidelity of integral approximation
# m = number of potential differences checked

main_test(20, 20, test_total, test_correct, control_total, control_correct)