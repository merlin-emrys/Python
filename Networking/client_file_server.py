import socket

s = socket.socket()
hsot = socket.gethostname()
port = 60000

s.connect((host,port))
s.send("ehlo")

with open('key_log.txt', 'wb') as f:
    print('file opened')
    while True:
        print('receiving file data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        f.write(data)

f.close()
print('got file')
s.close()
print('connection closed')
