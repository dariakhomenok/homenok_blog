from django.shortcuts import redirect, render
from .models import User

def login_required(func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('user_id'):
            return redirect('/login')
        return func(request, *args, **kwargs)
    return wrapper

@login_required
def for_authorized(request):
    return render(request, 'page_for_authorized.html')

def is_director(func):

    @login_required
    def wrapper(request, *args, **kwargs):
        id_user = request.session.get('user_id')
        user = User.objects.get(id=id_user)
        if user:
            if user.role.id == 1:
                return func(request, *args, **kwargs)
            else:
                message = 'Пользователь должен быть Менеджером'
        else:
            message = 'Пользователь не найден в базе'
        return render(request, 'error.html', {'message': message})
    return wrapper

@is_director
def for_director(request):
    return render(request, 'page_for_director.html')