from socket import *
#define the function/method

def createServer(host,port):
    #create the variable and assign it the socket method with the parameters of ipv4,tcp ports.
    serversocket = socket(AF_INET, SOCK_STREAM)
    serversocket.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
    #uses a socket method with our variable to bind the socket to our localhost on port 9000
    serversocket.bind((host,port))
    #enables the variable/socket we made to listen on the port.
    serversocket.listen(5)
    print("HTTP connection on port %s"%port)
    while True:
        clientsocket, address = serversocket.accept()
        request = clientsocket.recv(1024)
        print(request)
        http_response=("""
HTTP/1.1 200 OK

Hello World
""")
        http = str.encode(http_response)
        clientsocket.sendall(http)
        #clientsocket.shutdown(SHUT_WR)
        clientsocket.close()

    serversocket.close

createServer("11",9000)

