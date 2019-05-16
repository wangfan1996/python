from django.conf.urls import url, include
from .views import IndexView

urlpatterns = [
    url(r'^index/', IndexView.as_view()),
]
