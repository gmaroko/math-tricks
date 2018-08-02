def isprime(n, r):
    numbers = set(range(r, 1, -1))
    _primes = []
    while numbers:
        _p = numbers.pop()
        _primes.append(_p)
        numbers.difference_update(set(range(_p*2, r+1, _p)))
    if n in _primes:
        return True
    else:
        return False
trials = 1000
def func():
    import math
    global trials
    for n in range(0, trials, 1):
        prev = n-1
        if isprime(prev, trials):
            try:
                assert (int(math.pow(n, 1./3.)))**3 == n, "Not cube"
                print("{} for {}".format(True, prev))
            except AssertionError:
                pass

if __name__ == "__main__":
    import timeit
    t = timeit.Timer("func()", setup="from __main__ import func")
    print("Execution time: {}s\nNumbers tried: {}".format(round(t.timeit(1), 4), trials))
