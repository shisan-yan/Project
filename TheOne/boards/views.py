from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse, Http404
from boards.models import  Board, Topic, Post
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    boards = Board.objects.all()

    return render(request, 'boards/home.html', {'boards':boards})

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'boards/topics.html', {'board':board})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first() #临时使用一个账号作为登录用户

        topic = Topic.objects.create(
            subject = subject,
            board = board,
            starter = user
        )

        post = Post.objects.create(
            message = message,
            topic = topic,
            created_by = user
        )

        return redirect('board_topics', pk=pk)
    return render(request, 'boards/new_topics.html',{'board':board})