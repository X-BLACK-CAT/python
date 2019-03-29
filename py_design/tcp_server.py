import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#加入一条socket配置，重用ip和端口
# 请深入研究1.tcp三次握手，四次挥手 2.syn洪水攻击 3.服务器高并发情况下会有大量的time_wait状态的优化方法
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #就是它，在bind前加
server.bind(('127.0.0.1',9999))
server.listen(5)

while True:
    conn,addr = server.accept()
    print("来自%s的消息"%addr[0])
    while True:
        client_msg = conn.recv(1024)
        print(client_msg.decode('utf-8'))
        conn.send("来自服务的消息".encode('utf-8'))
    conn.close()


