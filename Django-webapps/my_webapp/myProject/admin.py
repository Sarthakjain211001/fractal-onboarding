from django.contrib import admin
from .models import EmployeeModel, ProductModel
# Register your models here.
admin.site.register(EmployeeModel)
admin.site.register(ProductModel)
