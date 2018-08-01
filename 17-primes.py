def main():
    from itertools import combinations_with_replacement as c
    TARGET = 17
    numbers = set(range(TARGET, 1, -1))
    _primes = []
    while numbers:
        _p = numbers.pop()
        _primes.append(_p)
        numbers.difference_update(set(range(_p*2, TARGET+1, _p)))

    true_sums, done, index = [], False, 0
    while not done:
        list_item = [list(item) for item in c(_primes, index)]
        for a_sub_list in list_item:
            if sum(a_sub_list) == TARGET:
                true_sums.append(a_sub_list)
            else:
                pass
        index+=1
        if index>len(_primes)+1:
            done = True
    assert len(true_sums) == TARGET
    print("Agreed")

main()
