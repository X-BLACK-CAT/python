import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    send_msg = input('>>:')
    client.sendto(send_msg.encode('utf-8'),('127.0.0.1',8080))
    recv_client_msg,addr = client.recvfrom(1024)
    print(addr,recv_client_msg.decode('utf-8'))
