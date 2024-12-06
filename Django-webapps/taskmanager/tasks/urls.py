from django.urls import path
from . import views

urlpatterns=[
    path('tasks/', views.task_view),
    path('task/update/<id>', views.update_view, name="update_task"),
    path('task/delete/<id>', views.delete_view, name="delete_task")
]
