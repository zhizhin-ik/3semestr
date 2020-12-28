import threading
import sys
import random
import time


def thread_job(number):
    global amount_using_streams
    amount_using_streams += spisok[number]
    sys.stdout.flush()


def run_threads(n):
    threads = [
        threading.Thread(target=thread_job, args=(i,))
        for i in range(0, n)
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

n = int(input())
spisok=[]
summa=0
amount_using_streams=0
for i in range(n):
    spisok.append(random.randint(0,10))
start = time.time()
summa = sum(spisok)
resultat_1=time.time()-start
start = time.time()
run_threads(n)
resultat_2=time.time()-start
print('Без потоков', summa, resultat_1)
print('С использованием потоков', amount_using_streams, resultat_2)