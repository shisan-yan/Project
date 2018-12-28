from django.urls import  path, include
from . import views as v
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', v.Index.as_view()),
    path('register/', v.register.as_view(), ),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), ),
    path('welcome/', v.Welcome.as_view())
]
