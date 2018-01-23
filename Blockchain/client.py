import socket
import sys


SK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IPServ = '127.0.0.1'
PortServ = 4242
BuffSize = 128


SK.connect((IPServ, PortServ))
SK.send(str.encode(sys.argv[1]))
data = SK.recv(BuffSize)

SK.shutdown(socket.SHUT_RDWR)
SK.close()

print("Echo >>>", bytes.decode(data))