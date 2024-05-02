from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm                                    
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import Profile

# Главная страница
def index(request):
    user_type = ''
    if request.user.is_authenticated:
        if request.user.profile.user_type == 'customer':
            user_type = 'customer'
        elif request.user.profile.user_type == 'executor':
            user_type = 'executor'
    return render(request, 'main_app/index.html', {'user_type': user_type})


# Представление для авторизации
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'main_app/login.html', {'form': form})

# Представление для регистрации
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, gender=form.cleaned_data.get('gender'), user_type=form.cleaned_data.get('user_type'))
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'main_app/register.html', {'form': form})


# Выход из аккаунта
@login_required
def logout_view(request):
    logout(request)
    return redirect('index')