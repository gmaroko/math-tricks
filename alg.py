from math import factorial as f
import time
def func():
    n = 0
    x = n

    t1 =time.time()
    while n<100000000000:
        if n == sum(f(int(d)) for d in str(n)):
            print("{}: {}".format(n, True))
            n+=1
        else:
            n+=1
        y = n
    t2 = time.time()
    print("\nFirst item: {}".format(x))
    print("Last item checked: {}".format(y))

    print("Time taken: {}s".format(round(t2-t1, 4)))

func()
