from django.urls import path
from . import views

urlpatterns=[
    path('create/', views.create_view),
    path('list/', views.list_view),
    path('detail/<id>', views.detail_view),
    path('update/<id>', views.update_view),
    path('delete/<id>', views.delete_view)
]
