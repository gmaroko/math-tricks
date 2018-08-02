def func():
    from itertools import combinations_with_replacement as c
    TARGET = 17
    #prime numbers >=17
    numbers = set(range(TARGET, 1, -1))
    _primes = []
    while numbers:
        _p = numbers.pop()
        _primes.append(_p)
        numbers.difference_update(set(range(_p*2, TARGET+1, _p)))
    #sums
    true_sums, done, index = [], False, 0
    while not done:
        main_list = [list(item) for item in c(_primes, index)]
        for a_sub_list in main_list:
            if sum(a_sub_list) == TARGET:
                true_sums.append(a_sub_list)
            else:
                pass
        index+=1
        if index > len(_primes)+1:
            done = True
    assert len(true_sums) == TARGET
    for true_s in true_sums:
        temp = ''
        for i in true_s:
            temp = temp+str(i)+'+'
        print("{} = {}".format(temp[:len(temp)-1], TARGET))
    print("\nCount: {}\nAgreed".format(len(true_sums)))

if __name__ =="__main__":
    from timeit import Timer
    exe_time = Timer("func()", setup="from __main__ import func")
    print("Execution time: {}s".format(round(exe_time.timeit(1), 4)))
