from django.urls import  path
from .views import  Manage, UserManage, UserAdd

urlpatterns = [
    path('manage/', Manage.as_view()),
    path('userManage/', UserManage.as_view()),
    path('UserAdd/', UserAdd.as_view())
]