from django.shortcuts import render

from .models import *

def test1(request):
    return render(request, 'testtree/test1.html', {'rubrics': Rubric.objects.all()})

def get_rubric(request):
    pass


