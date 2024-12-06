from django import forms
from .models import EmployeeModel, ProductModel


#employee form
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = [
            'emp_name',
            'emp_feedback'
        ]

#Product From
class ProductForm(forms.ModelForm):
     class Meta:
        model = ProductModel
        fields = [
            'product_name', 
            'product_category',
            'product_price',
            'product_description',
            'product_quantity'
        ]