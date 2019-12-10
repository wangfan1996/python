# 集合
# 可以使用大括号 { } 或者 set() 函数创建集合
# 创建空集合set()不能使用{}，{}是创建空字典

# 去重功能
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
basket.add('苹果')
print(basket)
basket.update([11, 5])
print(basket)
basket.remove(11)
print(basket)
# 移除集合中的元素，且如果元素不存在，不会发生错误
basket.discard(11)
print(basket)
# 随机删除集合中的一个元素
a = basket.pop()
print(a)
print(basket)

