from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'), 
  path('about/', views.about, name='about'), 
  path('trees/', views.trees_index, name='index'),
  path('trees/<int:tree_id>/', views.trees_detail, name='detail')
]