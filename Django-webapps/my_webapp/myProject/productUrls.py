from django.urls import path
from . import product_views

urlpatterns=[
    path('create/', product_views.create_view),
    path('list/', product_views.list_view),
    path('detail/<id>', product_views.detail_view),
    path('update/<id>', product_views.update_view),
    path('delete/<id>', product_views.delete_view)
]
