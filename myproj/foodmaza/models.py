from django.db import models
from django.urls import reverse
from datetime import date
from datetime import time


class Admin(models.Model):
    Name = models.CharField(max_length=30, default=None)
    DOB = models.DateField()
    Email = models.CharField(max_length=20, default=None)
    Password = models.CharField(max_length=20, default=None)
    Phone = models.CharField(max_length=12)
    Gender = models.CharField(max_length=1,
                              choices=(('M', 'Male',),
                                       ('F', 'Female',),
                                       ('X', 'Prefer not to disclose',)))

    def __str__(self):
        """String for representing the Model object."""
        return self.Name

    class Meta:
        db_table = "Admin"


class Customer(models.Model):
    Name = models.CharField(max_length=30, default=None)
    DOB = models.DateField(blank=True)
    Email = models.CharField(max_length=20, default=None)
    Password = models.CharField(max_length=20, default=None)
    Phone = models.CharField(max_length=12)
    Gender = models.CharField(max_length=1,
                              choices=(('M', 'Male',),
                                       ('F', 'Female',),
                                       ('X', 'Prefer not to disclose',)))

    def __str__(self):
        """String for representing the Model object."""
        return self.Name

    class Meta:
        db_table = "customer"


class Category(models.Model):
    C_Id = models.IntegerField(primary_key=True, editable=False)
    Name = models.CharField(max_length=30, default=None)

    def __str__(self):
        """String for representing the Model object."""
        return self.Name

    class Meta:
        db_table = "Category"


class sub_category(models.Model):
    C_Id = models.ForeignKey(
        Category, default=None, verbose_name="Category", on_delete=models.SET_DEFAULT)
    S_Id = models.IntegerField(primary_key=True, editable=False)
    Name = models.CharField(max_length=30, default=None)

    def __str__(self):
        """String for representing the Model object."""
        return self.Name

    class Meta:
        db_table = "sub_category"


class Item(models.Model):
    Item_id = models.IntegerField(primary_key=True, editable=False)
    Item_name = models.CharField(max_length=30, default=None)
    Item_image = models.ImageField(
        upload_to='images/', height_field=None, width_field=None, max_length=100)
    Discription = models.CharField(max_length=100, default=None)
    Item_price = models.CharField(max_length=30, default=None)
    S_Id = models.ForeignKey(
        sub_category, default=None, verbose_name="sub_category", on_delete=models.SET_DEFAULT)

    def __str__(self):
        """String for representing the Model object."""
        return self.Item_name

    class Meta:
        db_table = "Item"
