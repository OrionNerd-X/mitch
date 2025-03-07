from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add_task/', views.add_task, name='add_task'),
    path('update_task/<int:task_id>/', views.update_task, name='update_task'),
]
