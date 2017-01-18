def fib(a, b, n):
    if n == 0: return b
    else:
        return fib(b, a + b, n - 1)

def fib1(n):
    return fib(0, 1, n)

for i in range(0, 10):
    print "fib " + str(i)
    print fib1(i)
