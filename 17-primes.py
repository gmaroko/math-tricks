def primes(target):
    numbers = set(range(target, 1, -1))
    _primes = []
    while numbers:
        _p = numbers.pop()
        _primes.append(_p)
        numbers.difference_update(set(range(_p*2, target+1, _p)))
    return _primes


def main():
    from itertools import combinations_with_replacement as c
    TARGET = 17
    _primes = primes(TARGET)
    for i in range(1, len(_primes)+1):
        temp_item = [list(item) for item in c(_primes, i)]
        x=[]
    print(temp_item)

main()
