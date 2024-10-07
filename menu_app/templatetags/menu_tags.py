from django import template

register = template.Library()

@register.inclusion_tag('menu_app/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    from myproject.menu_app.models import Menu, MenuItem  # Переносим импорт внутрь функции
    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        return {'menu': None, 'items': []}

    items = MenuItem.objects.filter(menu=menu, parent=None).order_by('order')

    # Активный пункт меню
    request = context['request']
    active_url = request.path
    for item in items:
        item.active = (active_url == item.url)
        for child in item.children.all():
            child.active = (active_url == child.url)

    return {'menu': menu, 'items': items}


register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    menu_items = MenuItem.objects.filter(name=menu_name)  # Получите пункты меню по имени
    request = context['request']

    menu_html = '<ul>'
    for item in menu_items:
        active_class = 'active' if request.path == item.url else ''
        menu_html += f'<li class="{active_class}"><a href="{item.url}">{item.name}</a></li>'
    menu_html += '</ul>'

    return menu_html