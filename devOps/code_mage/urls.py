from django.urls import  path
from .views import  *

urlpatterns = [
    path('manage/', Manage.as_view()),
    path('userManage/', UserManage.as_view()),
    path('UserAdd/', UserAdd.as_view()),
    path('UserStatus/', UserStatus.as_view()),
]