import gitlab
gl = gitlab.Gitlab.from_config('gitServer', ['/etc/python-gitlab.cfg'])

userInfo = {
    'email': '253341888@qq.com',
    'username': 'wangyang',
    'password': '12345678',
    'name': '汪洋',
}

try:
    user = gl.users.create(userInfo)
except Exception as e:
    print(e)



