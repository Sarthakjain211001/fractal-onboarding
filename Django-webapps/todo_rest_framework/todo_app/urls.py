from django.urls import re_path
from todo_app import views

urlpatterns=[
    re_path(r'^api/tasks$', views.tasks_list),
    re_path(r'^api/tasks/(?P<pk>[0-9]+)$', views.task_details)
]