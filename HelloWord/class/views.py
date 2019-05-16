from django.http import JsonResponse
from django.views.generic.base import View
from .models import classes
from django.core import serializers
class IndexView(View):

    def get(self, request):
        course = classes.objects.all()
        data = []
        for i in course:
            item = {'name':i.name,'age':i.age}
            data.append(item)
        course = serializers.serialize("json",course)
        res = {"result": 0, "msg": "执行成功"+request.method, "data": data, "data1": course}
        res = {"result": 0, "msg": "执行成功"+request.method, "data": data,}
        return JsonResponse(res)

    def post(self, request):
        res = {"result": 1, "msg": "执行成功"+request.method}
        return JsonResponse(res)

    def delete(self, request):
        res = {"result": 1, "msg": "执行成功"+request.method}
        return JsonResponse(res)

    def put(self, request):
        res = {"result": 1, "msg": "执行成功"+request.method}
        return JsonResponse(res)
