from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('list-users/', UserList.as_view(), name='list-users'),
]
