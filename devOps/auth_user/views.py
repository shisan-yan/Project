from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, request
from django.views import  View
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


class Index(View):

    def get(self, request):
        return HttpResponse('这就已经进入到首页了！')


class login(View):

    #请求方法，也就是登陆页面的视图方法
    def get(self, request):

        form = SignUpForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):

        form = SignUpForm(request.POST)

        if form.is_valid():

            user = form.save()
            return render('success.html')
            # return redirect('/auth_user/')
        else:
            return render(request, 'login.html', {'form': form})
