# Условие можно трактовать по-разному, поэтому первый случай, когда получается за этих раз сразу набор чисел, второй случай, когда получаем по одному числу
# 1
def func_coroutine():
    print("Starting coroutine")
    average = 0
    dispersion = 0
    quantity = 0
    while True:
        x = yield average, dispersion, quantity
        quantity = len(x)
        average = sum(x)/quantity
        sumkv=0
        for i in x:
            sumkv += i*i
        dispersion = sumkv/quantity - average**2

coroutine = func_coroutine()
next(coroutine)
while True:
    n=input()
    if n:
        print(coroutine.send(list(map(int,n.split()))))
    else:
        break

# 2
def func_coroutine():
    print("Starting coroutine")
    average = 0
    dispersion = 0
    quantity = 0
    summa = 0
    sumkv = 0
    while True:
        x = yield average, dispersion, quantity
        sumkv += x*x
        summa += x
        quantity += 1
        average = summa / quantity
        dispersion = sumkv / quantity - average ** 2
coroutine = func_coroutine()
next(coroutine)
while True:
    n=input()
    if n:
        print(coroutine.send(int(n)))
    else:
        break
