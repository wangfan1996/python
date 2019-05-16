from django.db import models
# setting 注册一波INSTALLED_APPS
# python manage.py makemigrations
# python manage.py migrate 文件夹名字
class classes(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
