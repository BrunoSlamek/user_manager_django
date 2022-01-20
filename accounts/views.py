from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import User


def index(request):
    return render(request, 'index.html')


class UserList(ListView):
    models = User
    template_name = 'user_list.html'
    queryset = User.objects.all()
    context_object_name = 'users'
