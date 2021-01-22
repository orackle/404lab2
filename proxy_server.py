import socket,sys

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

payload = f'GET / HTTP/1.0\r\nHOST: www.google.com\r\n\r\n'



#get host information
def get_remote_ip(host):
	print(f'Getting IP for {host}')
	try:
		remote_ip = socket.gethostbyname( host )
	except socket.gaierror:
		print ('Hostname could not be resolved. Exiting')
		sys.exit()

	print (f'Ip address of {host} is {remote_ip}')
	return remote_ip

def main():

	#define address info, payload, and buffer size
	host = 'www.google.com'
	port = 80
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
		print("\n\nStarting proxy server")
		proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		proxy_start.bind((HOST, PORT))
		proxy_start.listen(1)
		while True:
			conn, addr = proxy_start.accept()
			print("Connected by proxy client:", addr)
			with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
				print(f'Connecting to Google')
				remote_ip = get_remote_ip(host)

				proxy_end.connect((remote_ip, port))

				full_data = conn.recv(BUFFER_SIZE) # received from client
				print(f'Sending recieved {full_data} to google')
				proxy_end.sendall(full_data) # send the data
				proxy_end.shutdown(socket.SHUT_WR)

				data = proxy_end.recv(BUFFER_SIZE)
				print(f'Sending recieved data {data} to client')
				conn.send(data)

			conn.close()



if __name__ == "__main__":
	main()
