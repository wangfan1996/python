import socket

# 创建socket对象
# 绑定地址（host,port）到套接字， 在AF_INET下,以元组（host,port）的形式表示地址
# 套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机名
host = socket.gethostname()
port = 9999
# 绑定端口号
serversocket.bind((host, port))
# 设置最大连接数，超过后排队
serversocket.listen(2)
while True:
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()
    msg = str(addr) + '说:' + clientsocket.recv(1024).decode('utf-8')
    print(msg)
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()




