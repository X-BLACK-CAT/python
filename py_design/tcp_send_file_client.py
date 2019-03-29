import os
import socket

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def client(ip_port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect_ex(ip_port)
    while True:
        try:

                msg = input('>>:').strip()
                cmd,file_name = msg.split()
                path = os.path.join(BASE_DIR,'send_data',file_name)
                file_size = os.stat(path).st_size
                file_data = '%s|%s|%s'%(cmd,file_name,file_size)
                sock.sendall(bytes(file_data,'utf-8'))
                send_size = 0

                with open(path,'rb') as f:
                    while send_size != file_size:
                        data = f.read(1024)
                        sock.sendall(data)
                        send_size += len(data)
                        print('\r'+'[保存进度]:%s%.02f%%'%(('>'*int(send_size/float(file_size))*50),float(send_size/float(file_size)*100)),end='')
                print()
                print('%s发送成功'%file_name)
        except Exception as e:
            print('参数错误')
            continue
            print(e)



if __name__ == '__main__':
    IP_PORT = ('127.0.0.1', 8080)
    client(IP_PORT)