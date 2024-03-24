from django import template

from blog.models import Category

register = template.Library()


@register.inclusion_tag('tags/many_tpl.html')
def menu_tpl(many_tpl='menu'):
    category = Category.objects.all()
    return {'category': category, 'many_tpl': many_tpl}
