from django.shortcuts import render
from .models import Graphic

def my_graphics(request):
    graphics= Graphic.objects.all()
    return render(request, 'graphics/my_graphics.html',{'graphics':graphics})
