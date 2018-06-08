def tail_fib(n, a=0, b=1):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return tail_fib(n - 1, b, a + b)

