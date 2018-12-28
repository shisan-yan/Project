from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, request
from django.views import  View
from .forms import SignUpForm
from django.contrib.auth import authenticate


# Create your views here.


class Index(View):

    def get(self, request):
        return render(request, 'index.html')

class register(View):

    #登陆请求方法，也就是登陆页面的视图方法
    def get(self, request):

        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):

        form = SignUpForm(request.POST)

        if form.is_valid():

            user = form.save()
            return render('success.html')
            # return redirect('/auth_user/')
        else:
            return render(request, 'register.html', {'form': form})

class login(View):
    #登陆请求方法，也就是登陆页面
    def get(self, request):
        form = SignUpForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):

        usernameIn = request.POST['username']
        passwordIn = request.POST['password']
        user = authenticate(username=usernameIn, password=passwordIn)

        if user is not None:
            pass
        else:
            return render(request, 'login.html', {'form': form})

class Welcome(View):
    def get(self, request):
        return render(request, 'welcome.html')