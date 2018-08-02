def func():
    a,b = 0,1
    while True:
        yield a
        a,b = b, a + b

for index, fib_no in zip(range(10), func()):
    print("{}\t{}".format(index, fib_no))
