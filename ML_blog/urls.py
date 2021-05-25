from django.urls import path
from . import views # . means current directory

urlpatterns = [
    path('', views.home,name="blog-home"), # we want to go to home function(views.home)
    path('about/',views.about,name="blog-about")
]