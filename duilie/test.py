import sys
if sys.version > '3':
    import queue as Queue
else:
    import Queue
print(sys.version)
# 队列先进先出
a = [1,2,3]
b = [3,2,1]
device_que = Queue.Queue()
for i in range(1,101):
        device_que.put(i)

