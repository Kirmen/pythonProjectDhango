from django.urls import path, include

from .views import *

urlpatterns = [
    path('', test1, name='test1'),
    path('rubrics/<int:pk>', get_rubric, name='rubric'),
]

