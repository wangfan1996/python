import socket

# 创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机名
host = socket.gethostname()
port = 999
# 连接服务，指定主机和端口
s.connect((host, port))
# 接受小于1024字节的数据
msg = s.recv(1024)
s.close()
print(msg.decode('utf-8'))
