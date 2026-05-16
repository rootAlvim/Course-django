from django.urls import path 
from recipes import views

urlpatterns = [
    path('', views.home, name="library-home"),
    path('recipes/<int:id>/',views.recipe,name="library-library"),
    
]