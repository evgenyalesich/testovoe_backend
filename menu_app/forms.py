from django import forms
from .models import MenuItem, Menu

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['title', 'menu']  # Изменили 'name' на 'title', чтобы соответствовать модели MenuItem

    def __init__(self, *args, **kwargs):
        super(MenuItemForm, self).__init__(*args, **kwargs)
        # При желании можете ограничить выбор меню
        self.fields['menu'].queryset = Menu.objects.all()
