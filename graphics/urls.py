from django.urls import path
from .import views

app_name = 'graphics'
urlpatterns = [
    path('', views.my_graphics, name='my_graphics'),
]