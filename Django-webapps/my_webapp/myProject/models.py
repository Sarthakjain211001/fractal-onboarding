from django.db import models

#Employee Model
class EmployeeModel(models.Model):
    emp_name = models.CharField(max_length=200)
    emp_feedback = models.TextField()

    def __str__(self):
        return self.emp_name


#Product Model
class ProductModel(models.Model):
    product_name = models.CharField(max_length=100)
    product_category = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_description = models.TextField()
    product_quantity = models.IntegerField()

    def __str__(self):
        return self.product_name