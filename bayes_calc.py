from math import factorial
from matplotlib import pyplot as plt

test_total = 100
test_correct = 80
control_total = 5
control_correct = 2


# range function that can deal with floats
def frange(x, y, jump):
    while round(x, 5) < round(y, 5):
        yield x
        x += jump


# n choose k for binomial calculations
def comb(n, k):
    return factorial(n) / (factorial(k)*factorial(n - k))


# probability of k out n, with x probability per test
def test_bin(n, k, x):
    return comb(n, k)*x**k*(1-x)**(n-k)


# tests combined likelihood that test is binomial with param x, control is binomial with parameter x-e
def test_diff(x, e, tt, tc, ct, cc):
    return test_bin(tt, tc, x)*test_bin(ct, cc, x-e)


# approximates an integral of the likelihood of x, x-e as params by trying n evenly spaced possible values of x
def hyp_test(n, e, tt, tc, ct, cc):
    total = 0
    if e > 0:
        total += test_diff(1, e, tt, tc, ct, cc)
        for i in frange(e, 1, (1-e)/n):
            total += 2*test_diff(i, e, tt, tc, ct, cc)
        total -= test_diff(e, e, tt, tc, ct, cc)
    else:
        total += test_diff(1+e, e, tt, tc, ct, cc)
        for i in frange(0, 1+e, (1+e)/n):
            total += 2*test_diff(i, e, tt, tc, ct, cc)
        total -= test_diff(0, e, tt, tc, ct, cc)
    return total


# gets an integral of likelihood of x, x-e as binomial params for m values of e, evenly spaced between -1 and 1
def main_test(n, m, tt, tc, ct, cc):
    chances = []
    for i in frange(-1, 1, (1/m)*2):
        chances.append((i, hyp_test(n, i, tt, tc, ct, cc)))
    normalize_factor = 1/sum(n for _, n in chances)
    print(normalize_factor)
    posterior = [(round(i, 3), n*normalize_factor) for i, n in chances]
    print(*posterior, sep='\n')
    return posterior


# first arg = fidelity of integral approximation
# second arg = number of potential differences
data = main_test(100, 100, test_total, test_correct, control_total, control_correct)

diff, probability = zip(*data)
plt.plot(diff, probability)
plt.xlabel('Improvement in p(correct answer)')
plt.ylabel('Relative likelihood')
plt.title('Posterior from uniform prior')
plt.show()
