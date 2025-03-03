"""Define URLs pattern for task!"""

from django.urls import path

from . import views


app_name = 'task_manager'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Update task status
    path('update_status/<int:task_id>/', views.update_status, name='update_status'),

    # Add a new task
    path('new_task/', views.new_task, name='new_task'),

    # Delete a task
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),

    # Edit a task
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
]