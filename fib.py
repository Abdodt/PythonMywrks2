def fib(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a + b
fib(100)

def fib2(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a = b
        b = a + b
fib2(100)

def whilop(n):
    x = 0
    while x <= n:
        print(x)
        x += 1
whilop(6)