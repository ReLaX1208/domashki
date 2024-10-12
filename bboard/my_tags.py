from django import template
from django.db.models import Count

register = template.Library()

@register.simple_tag
def total_posts():
    from django.contrib.auth.models import User
    return User.objects.count()

@register.simple_tag
def hello_world():
    return "Hello, World!"
