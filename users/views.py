from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User

def mypage(request, id):
    user=get_object_or_404(User, pk=id)
    context = {
        'user' :user
    }
    return render(request, 'users/mypage.html', context)
