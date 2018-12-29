from django.shortcuts import render
from django.views import  View
from .models import user, info
from django.http import  HttpResponse
from django.contrib.auth.hashers import  check_password, make_password
import gitlab
import json


# Create your views here.

class Manage(View):
    def get(self, request):
        return render(request, 'member-list.html',)

class UserManage(View):
    def get(self, request):
        return  render(request, 'user-manage.html',)

class UserAdd(View):
    #
    def get(self, request):
        return render(request, 'user-add.html',)

    def post(self, request):
        gitUsername = request.POST['username']
        gitEmail = request.POST['email']
        password = request.POST['pass']
        repass = request.POST['repass']
        name = request.POST['name']

        if repass != password:
            returnMsg = {'code': '400', 'message': '两次输入的密码不一致'}
            return HttpResponse('这里不对了！')
        gl = gitlab.Gitlab.from_config('gitServer', ['/etc/python-gitlab.cfg'])
        user = gl.users.list(username=gitUsername)

        if user:
            returnData = json.dumps({'code': '400', 'message': '用户已经存在！！'})
            return HttpResponse(returnData)
        try:
            userInfo = {
                'email':gitEmail,
                'password': password,
                'username': gitUsername,
                'name': name,
                        }
            gl.users.create(userInfo)
        except Exception as e:
            if e.response_code == '409':
                resData = {'code':e.esponse_code, 'message': e.error_message}
        resData = {'code': '200', 'message': '创建成功！'}

        return HttpResponse('创建成功了！')














