from django import template
from django.db.models import Count, F
from django.core.cache import cache

from bags.models import Category

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('bags/list_categories.html')
def show_categories():
    # categories=Category.objects.all()
    #categories = Category.objects.annotate(cnt=Count('bags')).filter(cnt__gt=0)

    # categories = cache.get('categories')
    # if not categories:
    #     categories = Category.objects.annotate(cnt=Count('bags', filter=F('bags__is_published'))).filter(cnt__gt=0)
    #     cache.set('categories', categories, 30)

    categories = Category.objects.annotate(cnt=Count('bags',filter= F('bags__is_published'))).filter(cnt__gt=0)
    return {'categories': categories}