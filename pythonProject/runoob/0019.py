import socket

# 创建socket对象
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机名
host = socket.gethostname()
port = 999
# 绑定主机名端口号
serverSocket.bind((host, port))
# 设置最大连接数，超过后排队
serverSocket.listen(3)
while True:
    # 建立客户端连接
    clientSocket, address = serverSocket.accept()
    print("连接地址：%s" % str(address))
    msg = "欢迎连接，%s" % str(address)
    clientSocket.send(msg.encode('utf-8'))
    clientSocket.close()

