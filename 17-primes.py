def primes(target):
    numbers = set(range(target, 1, -1))
    _primes = []
    while numbers:
        _p = numbers.pop()
        _primes.append(_p)
        numbers.difference_update(set(range(_p*2, target+1, _p)))
    return _primes

def x(n):
    while True:
        for i in range(n):
            yield i
    x(n-1)

def main():
    from itertools import combinations_with_replacement as c
    TARGET = 17
    _pri = [2,3,5,7,11,13,17] #primes(TARGET)
    true_sums = []
    done = False
    index = 0
    while not done:
        list_item = [list(item) for item in c(_pri, index)]
        for a_sub_list in list_item:
            if sum(a_sub_list) == 17:
                print(a_sub_list)
                true_sums.append(a_sub_list)
            else:
                pass
        index+=1
        if index>len(_pri)+1:
            done = True
    assert len(true_items) == 17
    print("Agreed")

main()
