from django import template

from blog.models import Tags, Posts

register = template.Library()


@register.inclusion_tag('tags/tags_tpl.html')
def tags_tpl():
    tags = Tags.objects.all()
    return {'tags': tags}


@register.inclusion_tag('tags/search_tpl.html')
def search():
    posts = Posts.objects.all()
    return {'posts': posts}


@register.inclusion_tag('tags/popular_tpl.html')
def popular():
    posts = Posts.objects.order_by('-views')[:3]
    return {'posts': posts}


