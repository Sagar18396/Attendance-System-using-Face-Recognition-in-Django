from django.db import models
import os


def get_image_path(instance, filename):
    return os.path.join('profile_images/', str(instance.employee_id), filename)


# Create your models here.
class ProductKey(models.Model):
    product_key = models.CharField(max_length=100, primary_key=True)

    class Meta:
        db_table = 'Product_Key'


class AdminDetail(models.Model):
    product_key = models.ForeignKey(ProductKey, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    organisation = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'Admin_Detail'


class Employee(models.Model):
    product_key = models.CharField(max_length=100)
    employee_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=100, primary_key=True)
    number = models.IntegerField()
    department = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to=get_image_path)

    class Meta:
        db_table = 'employee_details'
