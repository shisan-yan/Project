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
        gl = gitlab.Gitlab.from_config('gitServer', ['/etc/python-gitlab.cfg'])
        userList = gl.users.list(page=1, per_page=10)
        return render(request, 'user-manage.html', {'userList': userList})

class UserAdd(View):
    #
    def get(self, request):
        gl = gitlab.Gitlab.from_config('gitServer', ['/etc/python-gitlab.cfg'])
        proList = gl.projects.list()
        proInfo = []
        for project in proList:
            dit = {}
            dit['name'] = project.name
            dit['id'] = project.id
            proInfo.append(dit)
        return render(request, 'user-add.html', {'project': proInfo})

    def post(self, request):
        gitUsername = request.POST['username']
        gitEmail = request.POST['email']
        password = request.POST['pass']
        repass = request.POST['repass']
        name = request.POST['name']
        project = request.POST['project'].split(',')

        if repass != password:
            returnMsg = {'code': '400', 'message': '两次输入的密码不一致'}
            return HttpResponse(returnMsg)

        gl = gitlab.Gitlab.from_config('gitServer', ['/etc/python-gitlab.cfg'])
        user = gl.users.list(username=gitUsername)

        if user:
            returnData = json.dumps({'code': '400', 'message': '用户已经存在！！'})
            return HttpResponse(returnData)
        try:
            userInfo = {
                'email': gitEmail,
                'password': password,
                'username': gitUsername,
                'name': name,
                        }
            gl.users.create(userInfo)
        except Exception as e:
            retDit = json.dumps({'code': '400', 'message': '创建用户:%s' % str(e)})
            return HttpResponse(retDit)

        # 如果有指定项目，在创建用户完成后，给指定的用户添加项目权限
        if len(project) > 0:
            try:
                userID = gl.users.list(username=gitUsername)[0].id  # 获取到刚才创建用户后的用户ID
                for proId in project:
                    if int(proId) > 0:
                        projectObj = gl.projects.get(proId)
                        projectObj.members.create({'user_id': userID, 'access_level': gitlab.DEVELOPER_ACCESS})
            except Exception as e:
                resData = json.dumps({'code': '500', 'message': '添加项目权限 %s' % e})
                return HttpResponse(resData)

        resData = json.dumps({'code': '200', 'message': '创建成功！'})
        return HttpResponse(resData)

class UserStatus(View):
    def post(self, request):
        id = request.POST['id']
        status = request.POST['flg']

        gl = gitlab.Gitlab.from_config('gitServer', ['/etc/python-gitlab.cfg'])
        try:
            user = gl.users.get(id)
            if status == 'enable':
                user.unblock()
                message = '启用成功'
            elif status == 'disable':
                user.block()
                message = '禁用成功'
            reArr = {'code': 200, 'message': message}
        except Exception as e:
            reArr = {'code': 400, message: e}

        return HttpResponse(json.dumps(reArr))






















