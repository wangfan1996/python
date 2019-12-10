# 安装模块
# pip install redis
import redis
import random


class TestString(object):
    # 字符串相关操作
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

    def test_set(self):
        # 设置单个值
        rest = self.r.set('user1', 'Amy')
        print(rest)

    def test_get(self):
        # 获取单个值
        rest = self.r.get('user1')
        return rest

    def test_mset(self):
        # 设置多个值
        d = {
            'name': 'name1',
            'age': 21
        }
        rest = self.r.mset(d)
        return rest

    def test_mget(self):
        # 获取多个值
        rest = self.r.mget('name', 'age')
        return rest

    def test_del(self):
        # 删除
        rest = self.r.delete('name')
        return rest


class TestList(object):
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

    def test_push(self):
        name = "name%s" % random.randint(0, 100)
        rest = self.r.lpush('eat', name)
        print(rest)
        rest = self.r.lrange('eat', 0, -1)
        print(rest)

    def test_pop(self):
        rest = self.r.lpop('eat')
        print(rest)
        rest = self.r.lrange('eat', 0, -1)
        print(rest)


class TestSet(object):
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

    def test_sadd(self):
        rest = self.r.sadd('zoo', 'cat', 'dog')
        print(rest)
        rest = self.r.smembers('zoo')
        print(rest)

    def test_srem(self):
        rest = self.r.srem('zoo', 'dog')
        print(rest)
        rest = self.r.smembers('zoo')
        print(rest)

    def test_sinter(self):
        # 交集
        rest = self.r.sinter('zoo', 'zoo1')
        print(rest)

    def test_sunion(self):
        # 并集
        rest = self.r.sunion('zoo', 'zoo1')
        print(rest)


if __name__ == '__main__':
    # str_obj = TestString()
    # str_obj.test_set()
    # rest = str_obj.test_get()
    # rest = str_obj.test_mset()
    # rest = str_obj.test_mget()
    # rest = str_obj.test_del()
    # print(rest)
    # list_obj = TestList()
    # list_obj.test_pop()
    set_obj = TestSet()
    # set_obj.test_sadd()
    # set_obj.test_srem()
    set_obj.test_sinter()
    set_obj.test_sunion()
