import os
import socket
import gevent

from gevent import monkey
monkey.patch_all()


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def server(ip_port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(ip_port)
    sock.listen(5)
    while True:
        client_conn,address = sock.accept()
        print(address[0],address[1])
        gevent.spawn(request_handler,client_conn)

def request_handler(conn):
    while True:
        client_data = conn.recv(1024)
        cmd,file_name,file_size = str(client_data,'utf-8').split("|")
        save_path = os.path.join(BASE_DIR,'save_data',file_name)
        recv_size = 0
        with open(save_path,'wb') as f:
            while recv_size != int(file_size):
                data = conn.recv(1024)
                f.write(data)
                recv_size += len(data)
                print('\r'+'[保存进度]:%s%.02f%%'%(('>'*int(recv_size/float(file_size))*50),float(recv_size/float(file_size)*100)),end='')
        print()
        print('%s保存成功'%file_name)



if __name__ == "__main__":
    IP_PORT = ('127.0.0.1', 8080)
    server(IP_PORT)