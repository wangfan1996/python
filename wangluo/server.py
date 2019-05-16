# 导入 socket、sys 模块
import socket
import sys
import time
# 创建 socket 对象
# family: 套接字家族可以使AF_UNIX或者AF_INET
# type: 套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM
# protocol: 一般不填默认为0.
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# 获取本地主机名
host = socket.gethostname()

port = 9999

# 绑定端口号
# 绑定地址（host,port）到套接字， 在AF_INET下,以元组（host,port）的形式表示地址。
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(2)

while True:
    # 建立客户端连接
    clientsocket,addr = serversocket.accept()      
    print("连接地址: %s" % str(addr))
    msg='欢迎访问菜鸟教程！'+ "\r\n"
    time.sleep(5)
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()
