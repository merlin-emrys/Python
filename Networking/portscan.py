import threading
from queue import Queue
import socket
from datetime import datetime

host = input('Enter Host Address To Scan: ')
ip = socket.gethostbyname(host)
print_lock = threading.Lock()
def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((ip, port))
        with print_lock:
            print('port', port, 'is open')
        con.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

q = Queue()

for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()
    
for worker in range(1,500):
        q.put(worker)
q.join
