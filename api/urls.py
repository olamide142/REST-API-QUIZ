from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('task-list/', views.task_list_view, name='task-list'),
    path('task-detail/<str:id>/', views.details_view, name='details-list'),
    path('task-create/', views.create_view, name='create-task'),
    path('task-update/<str:id>/', views.update_view, name='update-task'),
    path('task-delete/<str:id>/', views.delete_view, name='delete-task'),
]