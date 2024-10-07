from pydoc import resolve

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from .models import MenuItem
from .forms import MenuItemForm

def check_url(request):
    url = request.GET.get('url', '')
    try:
        match = resolve(url)
        return JsonResponse({'exists': True, 'name': match.view_name})
    except Exception:
        return JsonResponse({'exists': False})

def home_view(request):
    return render(request, 'menu_app/home.html')

@login_required
def profile_view(request):
    menu_items = MenuItem.objects.filter(user=request.user)
    return render(request, 'menu_app/profile.html', {'menu_items': menu_items})

@login_required
def create_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            menu_item = form.save(commit=False)
            menu_item.user = request.user  # Присваиваем текущего пользователя
            menu_item.save()
            return redirect('profile')
    else:
        form = MenuItemForm()
    return render(request, 'menu_app/create_menu_item.html', {'form': form})


@login_required
def edit_menu_item(request, pk):
    menu_item = get_object_or_404(MenuItem, pk=pk, user=request.user)

    if request.method == 'POST':
        form = MenuItemForm(request.POST, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = MenuItemForm(instance=menu_item)

    # Отладочная информация
    print(f"Editing MenuItem: {menu_item}, Form errors: {form.errors if request.method == 'POST' else 'N/A'}")

    return render(request, 'menu_app/edit_menu_item.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Вход после успешной регистрации
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'menu_app/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'menu_app/login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('home')  # Перенаправление на главную страницу после выхода
