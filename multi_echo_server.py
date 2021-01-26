#!/usr/bin/env python3
import socket
from multiprocessing import Process
import time

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

# helper function - lab ta code
def handle_echo(addr, conn):
    print("Connected by", addr)
    full_data = conn.recv(BUFFER_SIZE)
    conn.sendall(full_data)
    conn.shutdown(socket.SHUT_WR)
    conn.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)

        #continuously listen for connections
        # from lab ta code
        while True:
            conn, addr = s.accept()
            p = Process(target=handle_echo, args=(addr, conn))
            p.daemon = True
            p.start()
            print("started proccess ", p)


if __name__ == "__main__":
    main()
