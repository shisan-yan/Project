from django.shortcuts import render
from django.views import  View
from django.http import  HttpResponse

# Create your views here.


class Manage(View):
    def get(self, request):
        return render(request, 'member-list.html',)

class UserManage(View):
    def get(self, request):
        return  render(request, 'user-manage.html',)

class UserAdd(View):
    def get(self, request):
        return render(request, 'user-add.html',)