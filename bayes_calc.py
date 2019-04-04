from math import factorial

test_total = 40
test_correct = 25
control_total = 30
control_correct = 15


# range function that can deal with floats
def frange(x, y, jump):
  while x < y:
    yield x
    x += jump


# n choose k for binomial calculations
def comb(n, k):
    return factorial(n) / factorial(k) / factorial(n - k)


# probability of k out n, with x probability per test
def test_bin(n, k, x):
    return comb(n, k)*x**k*(1-x)**(n-k)


# tests combined likelihood that test is binomial with param x, control is binomial with parameter x-e
def test_diff(x, e, tt, tc, ct, cc):
    return test_bin(tt, tc, x)*test_bin(ct, cc, x-e)


# approximates an integral of the likelihood of x, x-e as params by trying n evenly spaced possible values of x
def hyp_test(n, e, tt, tc, ct, cc):
    total = 0
    total += test_diff(1, e, tt, tc, ct, cc)
    for i in frange(e, 1, (1-e)/n):
        total += 2*test_diff(i, e, tt, tc, ct, cc)
    total -= test_diff(e, e, tt, tc, ct, cc)
    return total


# gets an integral of likelihood of x, x-e as binomial params for m values of e, evenly spaced between -1 and 1
def main_test(n, m, tt, tc, ct, cc):
    chances = []
    for i in frange(-1, 1, 1/m):
        chances.append((i, hyp_test(n, i, tt, tc, ct, cc)))
    print(chances)
    normalize_factor = 1/sum(n for _, n in chances)
    print(normalize_factor)
    posterior = [(i, n*normalize_factor) for i, n in chances]
    print(posterior)

# n = fidelity of integral approximation
# m = number of potential differences checked

main_test(20, 20, test_total, test_correct, control_total, control_correct)
