from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from .views import edit_menu_item, check_url

urlpatterns = [
    path('edit/<int:pk>/', edit_menu_item, name='edit_menu_item'),
    path('check-url/', check_url, name='check_url'),  # Добавили новый путь
    path('signup/', views.signup_view, name='signup'),  # Страница регистрации
    path('login/', views.login_view, name='login'),      # Страница входа
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # Страница выхода с перенаправлением на страницу входа
    path('profile/', views.profile_view, name='profile'),  # Страница профиля пользователя
    path('create/', views.create_menu_item, name='create_menu_item'),  # Страница создания элемента меню (добавлено)
    path('edit/<int:pk>/', views.edit_menu_item, name='edit_menu_item'),  # Страница редактирования элемента меню (добавлено)
]
