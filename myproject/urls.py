# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from menu_app import views  # Импортируем views для доступа к представлениям

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),  # Добавьте этот маршрут для корневого URL
    path('profile/', views.profile_view, name='profile'),
    path('create_menu_item/', views.create_menu_item, name='create_menu_item'),
    path('edit_menu_item/<int:pk>/', views.edit_menu_item, name='edit_menu_item'),
    path('menu_app/', include('menu_app.urls')),  # Если у вас есть отдельный urls.py в приложении
]
