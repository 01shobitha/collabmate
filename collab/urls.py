from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('details/<slug:username>/',views.details,name= 'details'),
]

