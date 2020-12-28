# Проблема в том, что разные потоки используют одну и ту же переменную, которая в них же и изменяется.
# Поэтому если какой-то поток не завершил работу, то другой поток может взять переменную, которая не успела измениться.
# В случаях, 1,2,3 counter = 10, в первом случае время работы слишком мало, чтобы не успеть завершить работу, в 3,4
# представлен код, который блокирует возможность выполнять функцию thread_job() потокам, пока его выполняет какой-то
# другой. Во втором коде такой блокировки нет, и есть вероятность того, что переменная counter не успела измениться до
# начала работы другого потока.
#__________№1____________________________
import threading
import sys


def thread_job():
    global counter
    old_counter = counter
    counter = old_counter + 1
    print('{} '.format(counter), end='')
    sys.stdout.flush()


counter = 0
threads = [threading.Thread(target=thread_job) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(counter)

#__________№2____________________________
import threading
import random
import time
import sys


def thread_job():
    global counter
    old_counter = counter
    time.sleep(random.randint(0, 1))
    counter = old_counter + 1
    print('{} '.format(counter), end='')
    sys.stdout.flush()


counter = 0
threads = [threading.Thread(target=thread_job) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(counter)
#__________№3____________________________
import threading
import random
import time
import sys


def thread_job():
    lock.acquire()  # mutex
    global counter
    old_counter = counter
    time.sleep(random.randint(0, 1))
    counter = old_counter + 1
    print('{} '.format(counter), end='')
    sys.stdout.flush()
    lock.release()


lock = threading.Lock()
counter = 0
threads = [threading.Thread(target=thread_job) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(counter)
#__________№4____________________________
import threading
import random
import time
import sys


def thread_job():
    with lock:
        global counter
        old_counter = counter
        time.sleep(random.randint(0, 1))
        counter = old_counter + 1
        print('{} '.format(counter), end='')
        sys.stdout.flush()


lock = threading.Lock()
counter = 0
threads = [threading.Thread(target=thread_job) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(counter)
