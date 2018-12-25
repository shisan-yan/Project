from django.urls import  path, include
from . import views as v

urlpatterns = [
    path('', v.Index.as_view()),
    path('login/', v.login.as_view()),
]
