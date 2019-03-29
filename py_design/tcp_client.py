import socket

ip_port = ('127.0.0.1',9999)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect_ex(ip_port)
while True:
    send_msg = input('>>:').strip()
    if len(send_msg) == 0:continue
    client.send(send_msg.encode('utf-8'))

    recv_server_msg = client.recv(1024)
    print(recv_server_msg.decode('utf-8'))

# 服务端套接字函数
# s.bind()
# 绑定(主机, 端口号)
# 到套接字
# s.listen()
# 开始TCP监听
# s.accept()
# 被动接受TCP客户的连接, (阻塞式)
# 等待连接的到来
#
# 客户端套接字函数
# s.connect()
# 主动初始化TCP服务器连接
# s.connect_ex()
# connect()
# 函数的扩展版本, 出错时返回出错码, 而不是抛出异常
#
# 公共用途的套接字函数
# s.recv()
# 接收TCP数据
# s.send()
# 发送TCP数据(send在待发送数据量大于己端缓存区剩余空间时, 数据丢失, 不会发完)
# s.sendall()
# 发送完整的TCP数据(本质就是循环调用send, sendall在待发送数据量大于己端缓存区剩余空间时, 数据不丢失, 循环调用send直到发完)
# s.recvfrom()
# 接收UDP数据
# s.sendto()
# 发送UDP数据
# s.getpeername()
# 连接到当前套接字的远端的地址
# s.getsockname()
# 当前套接字的地址
# s.getsockopt()
# 返回指定套接字的参数
# s.setsockopt()
# 设置指定套接字的参数
# s.close()
# 关闭套接字
#
# 面向锁的套接字方法
# s.setblocking()
# 设置套接字的阻塞与非阻塞模式
# s.settimeout()
# 设置阻塞套接字操作的超时时间
# s.gettimeout()
# 得到阻塞套接字操作的超时时间
#
# 面向文件的套接字的函数
# s.fileno()
# 套接字的文件描述符
# s.makefile()
# 创建一个与该套接字相关的文件