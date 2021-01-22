import socket,sys

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

payload = "GET / HTTP/1.0\r\nHOST: www.google.com\r\n\r\n"

def connect(addr):
	while True: 
		conn, addr = proxy_start.accept()
		print("Connected by", addr)

		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
			print("Connecting to Google")
			remote_ip = get_remote_ip(host)

			proxy_end.connect()