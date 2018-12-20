from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

class Index(View):

    """首页"""
    def get(self, request, *args, **kwargs):
        title = "运维管理-首页"

