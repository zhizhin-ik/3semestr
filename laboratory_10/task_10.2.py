import os, re
import threading
import sys


def thread_job(suffix):
    with lock:
        ip = "192.168.178." + str(suffix)
        ping_out = os.popen("ping -q -c2 " + ip, "r")  # получение вердикта
        print("... pinging ", ip)
        while True:
            line = ping_out.readline()
            if not line:
                break
            n_received = received_packages.findall(line)
            if n_received:
                print(ip + ": " + status[int(n_received[0])])
            sys.stdout.flush()

lock = threading.Lock()
received_packages = re.compile(r"(\d) received")
status = ("no response", "alive but losses", "alive")
threads = [
    threading.Thread(target=thread_job, args=(i,))
    for i in range(20, 30)
]
for thread in threads:
    thread.start()