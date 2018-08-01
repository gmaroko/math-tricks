def primes(target):
    numbers = set(range(target, 1, -1))
    _primes = []
    while numbers:
        _p = numbers.pop()
        _primes.append(_p)
        numbers.difference_update(set(range(_p*2, target+1, _p)))
    return _primes
