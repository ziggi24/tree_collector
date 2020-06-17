from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'), 
  path('about/', views.about, name='about'), 
  path('trees/', views.trees_index, name='index'),
  path('trees/<int:tree_id>/', views.trees_detail, name='detail'),
  path('trees/<int:tree_id>/delete', views.trees_delete, name='delete'), 
  path('trees/<int:tree_id>/edit', views.trees_edit, name='edit'), 
  path('trees/<int:tree_id>/add_watering', views.add_watering, name='add_watering'),
  path('trees/<int:tree_id>/assoc_worker/<int:worker_id>', views.assoc_worker, name='assoc_worker'),
  path('trees/<int:tree_id>/deassoc_worker/<int:worker_id>', views.deassoc_worker, name='deassoc_worker'),
]