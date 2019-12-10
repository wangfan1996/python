# 安装模块
# pip install sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
import random
import string


# 连接数据库
# 默认会使用MySQLdb，修改如下使用pymysql
engine = create_engine('mysql+pymysql://root:root@localhost:3306/python_test', encoding='utf-8', echo=False)
# 获取基类
Base = declarative_base()


class User(Base):  # 继承基类
    __tablename__ = 'user'
    Id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
    age = Column(Integer, nullable=False)


Base.metadata.create_all(engine)  # 创建表格

Session_class = sessionmaker(bind=engine)
Session = Session_class()

# 新增数据
name = "name%s" % random.randint(0, 100)
password = ''.join(random.sample(string.ascii_letters + string.digits, 8))
age = random.randint(0, 100)
user_obj = User(name=name, password=password, age=age)
Session.add(user_obj)
Session.commit()
print('Id:%d,name:%s,password:%s,age:%d' % (user_obj.Id, user_obj.name, user_obj.password, user_obj.age))
# 查询数据
# 查询所有满足条件的all
# 查询所有满足条件的第一个first
user_obj_list = Session.query(User).filter(User.age > 20).all()
for user_obj in user_obj_list:
    print('Id:%d,name:%s,password:%s,age:%d' % (user_obj.Id, user_obj.name, user_obj.password, user_obj.age))

# 按照主键查询
user_obj = Session.query(User).get(3)
print('Id:%d,name:%s,password:%s,age:%d' % (user_obj.Id, user_obj.name, user_obj.password, user_obj.age))

# 更新数控
user_obj = Session.query(User).filter(User.Id == 1).first()
print('Id:%d,name:%s,password:%s,age:%d' % (user_obj.Id, user_obj.name, user_obj.password, user_obj.age))
name = '张三%s' % random.randint(0, 100)
user_obj.name = name
Session.commit()
user_obj = Session.query(User).filter(User.Id == 1).first()
print('Id:%d,name:%s,password:%s,age:%d' % (user_obj.Id, user_obj.name, user_obj.password, user_obj.age))
