from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

def users(request):
    if request.session.get('user_id'):      
        users = User.objects.all()
        return render (request, 'users.html',{'users': users})
    else:
        return redirect('/login/')


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
    if request.session.get('user_id'):
        id = request.session.get('user_id')
        l = request.session.get('login')
        u = User.objects.get(id=id)
        return render(request, 'index.html', {'login': l, 'user': u})
    else:
        return redirect('/login/')


#авторизация
def login(request):
    if request.method=="GET":
        return render(request, 'login.html')
    else:
        login = request.POST.get('login')
        password = request.POST.get('pass')
        try:
            user = User.objects.get(login=login)
        except User.DoesNotExist:
            print("ПОЛЬЗОВАТЕЛЬ НЕ НАЙДЕН!!!!")
            return redirect('/login')

        if password != user.password:
            print('ПАРОЛЬ НЕВЕРНЫЙ!')
            return redirect('/login')
            
        request.session['user_id'] = user.id
        request.session['login'] = user.login
        print('ВСЁ ОК')
        return redirect('/')

#выход из системы
def logout_view(request):
    request.session.flush()
    return redirect('/login')