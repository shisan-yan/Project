from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import  User

# Create your views here.

def index(request):
    data = User.objects

    # return render(request, 'DevOps/index.html', data)
    template = loader.get_template('DevOps/index.html')
    returndata = {
        'returndata' : data
    }
    return HttpResponse(template.render(returndata, request))