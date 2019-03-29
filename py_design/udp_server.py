'''服务端'''
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('127.0.0.1',8080))
while True:
    recv_client_msg,addr = server.recvfrom(1024)
    print(recv_client_msg.decode('utf-8'),addr)
    server.sendto('客户端发的消息'.encode('utf-8'),addr)