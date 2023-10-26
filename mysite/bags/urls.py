from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('user_login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    # path('', index, name='home'),
    # path('', cache_page(60)(HomeBags.as_view()), name='home'), #кешування
    path('', HomeBags.as_view(), name='home'),
    # path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', BagsByCategory.as_view(extra_context={'title': 'Якийсь тайтл'}),
         name='category'),
    # path('bags/<int:bags_id>/', view_bag, name='view_bag'),
    path('bags/<int:pk>/', ViewBag.as_view(), name='view_bag'),
    # path('bags/add_bag/', add_bag, name='add_bag'),
    path('bags/add_bag/', CreateBag.as_view(), name='add_bag'),
    path('pagitest/', pagitest, name='pagitest'),
    path('contact_us/', contact_us, name='contact_us'),
]
