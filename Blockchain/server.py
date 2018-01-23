# coding=utf-8

import socket

IPServ = "localhost"
PortServ = 4242
BuffSize = 32
QueuedCo = 3

'''Listening Socket'''
SKL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SKL.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
SKL.bind((IPServ, PortServ))
SKL.listen(QueuedCo)

'''Serving socket'''
(SKS, Add) = SKL.accept()
print("Connection established with", Add)

while(True):
	data = SKS.recv(BuffSize)
	if not data:
		print("No more data, end of connection with", Add)
		break
	print(">>>", bytes.decode(data))
	SKS.send(data) #Echo ON


SKS.shutdown(socket.SHUT_RDWR)
SKS.close()
SKL.shutdown(socket.SHUT_RDWR)
SKL.close()

