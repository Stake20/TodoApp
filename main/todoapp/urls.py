from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('updated_list/<str:pk>/', views.updateList, name="update_list"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),


]
