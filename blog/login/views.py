from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

def users(request):
    users = User.objects.all()
    return render (request, 'users.html',{'users': users})


def add_user(request):
    if request.method == "POST":
        user = UserForm(request.POST)
        if user.is_valid():
            user.save()
        return redirect('/users/')
    else: 
        form = UserForm()
        return render(request, "add_user.html", {'form': form})

#гл страница
def index(request):
    return render(request, 'index.html')

#авторизация
def login(request):
    if request.method=="get":
        return render(request, 'login.html')
        else:
            return redirect('/')