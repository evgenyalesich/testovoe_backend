# menu_app/admin.py

from django.contrib import admin
from .models import Menu, MenuItem

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Показать поле 'name' для модели Menu

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu', 'user', 'order')  # Убедитесь, что поля здесь соответствуют вашей модели MenuItem

admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
