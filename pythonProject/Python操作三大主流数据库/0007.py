# 安装模块
# pip install mongoengine

from mongoengine import connect, Document, StringField, IntField, FloatField, ListField, EmbeddedDocument, EmbeddedDocumentField
import random

connect('students')

SEX_CHOICES = (
    ('male', '男'),
    ('female', '女'),
)


class Grade(EmbeddedDocument):
    # 成绩
    name = StringField(required=True)
    score = FloatField(required=True)


class Student(Document):
    # 学生
    name = StringField(max_length=32, required=True)
    age = IntField(required=True)
    sex = StringField(choices=SEX_CHOICES, required=True)
    grade = FloatField()
    address = StringField()
    grades = ListField(EmbeddedDocumentField(Grade))

    meta = {
        'collection': 'students',        # 配置集合名称
        'ordering': ['-age'],       # 按照年级倒序排
    }


class TestMonGoEngine(object):
    def add_one(self):
        language = Grade(name='语文', score=random.randint(0, 100))
        english = Grade(name='英语', score=random.randint(0, 100))
        mathematics = Grade(name='数学', score=random.randint(0, 100))
        name = "name%s" % random.randint(0, 100)
        age = random.randint(0, 50)
        sex = random.sample(['male', 'female'], 1)[0]
        grades = [language, english, mathematics]
        stu_obj = Student(name=name, age=age, sex=sex, grades=grades)
        stu_obj.save()
        return stu_obj

    def get_one(self):
        # 查询一条数据
        return Student.objects.first()

    def get_more(self):
        # 查询多条数据
        return Student.objects.all()

    def get_from_oid(self, oid):
        # 根据ID获取数据
        return Student.objects.filter(pk=oid).first()

    def update(self):
        # 修改一条数据 返回修改成功行数
        # rest = Student.objects.filter(sex='male').update_one(inc__age=10)
        # return rest
        # 修改多条数据 返回修改成功行数
        rest = Student.objects.filter(sex='male').update(inc__age=10)
        return rest

    def delete(self):
        # 删除一条数据
        # rest = Student.objects.filter(sex='female').first().delete()
        # return rest
        # 删除多条数据
        rest = Student.objects.filter(sex='female').delete()
        return rest
        # 删除一条返回None删除多条返回删除的条数


if __name__ == '__main__':
    obj = TestMonGoEngine()
    rest = obj.add_one()
    print(rest)
    print(rest.pk)
    print(rest.id)

    # rest = obj.get_one()
    # print(rest)
    # print(rest.id)
    # print(rest.name)
    # print(rest.age)

    # rows = obj.get_more()
    # for row in rows:
    #     print('id:%s,name%s,age%s,sex:%s' % (row.id, row.name, row.age, row.sex))

    # rest = obj.get_from_oid('5def41adbda4e82ffaf85147')
    # print('id:%s,name%s,age%s,sex:%s' % (rest.id, rest.name, rest.age, rest.sex))

    # 修改和删除
    # rest = obj.update()
    # print(rest)
    # rest = obj.delete()
    # print(rest)

