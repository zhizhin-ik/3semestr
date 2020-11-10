def fib(x):
    a=1
    b=1
    while x>0:
        yield a
        a,b =b, a+b
        x-=1

n=int(input())
for i in fib(n):
    print(i)