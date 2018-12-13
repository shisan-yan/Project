from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.


class Index(View):
    """首页视图"""

    def get(self, request, *args, **kwargs):
        # return HttpResponse('你现在已经进入到首页来了！')


