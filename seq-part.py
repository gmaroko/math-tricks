def func():
    import math
    import random
    r = 1000
    n = 5 #random.randint(0, r)
    assert n>0
    #n*pi
    sequence_1 = [round(x*math.pi) for x in range(r)]
    #n*pi/(pi-1)
    sequence_2 = [round((x*math.pi)/(math.pi - 1)) for x in range(r)]
    if n in sequence_1:
        assert n not in sequence_2
        print("{} in sequence_1".format(n))
    elif n in sequence_2:
        assert n not in sequence_1
        print("{} in sequence_2".format(n))
    else:
        print("{} neither in sequence_1 nor sequence_2".format(n))
        print("Never printing this anyways")



if __name__ == "__main__":
    from timeit import Timer
    exe_time = Timer("func()", setup="from __main__ import func")
    print(exe_time.timeit(1))
