from django.urls import path
from . import views #from this folder go to views

urlpatterns = [
    path('', views.home, name ='home'),#home page
    path('about/', views.about, name ='about'), #about
    path('cats/', views.cats_index, name='index'), # route for cats index
]

# views home page
# we are going to call this the home page


