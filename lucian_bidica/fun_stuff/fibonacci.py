# Exemplu de generator al numerelor Fibonacci

def fib(numar):
    a = 0
    b = 1
    for i in range(numar):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fib(100):
    print(x)

