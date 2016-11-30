from django.db import models
from django.utils import timezone
from django import forms


class product_type(models.Model):
    name = models.CharField(max_length=75)
    note1 = models.CharField(max_length=100, blank=True)
    note2 = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return '%s' % (self.name)



class inventory(models.Model):
    inventory_type = models.ForeignKey(product_type)
    model = models.CharField(max_length=75)
    conversion_rate = models.FloatField()
    measure = models.CharField(max_length=100, blank=True)
    note1 = models.CharField(max_length=100, blank=True)
    note2 = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return '%s' % (self.model)


class supplier(models.Model):
    name = models.CharField(max_length=75)
    contact_name = models.CharField(max_length=75)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    bank_account = models.CharField(max_length=100, blank=True)
    note1 = models.CharField(max_length=100, blank=True)
    note2 = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return '%s' % (self.name)

class add_inventory(models.Model):
    date = models.DateField(default=timezone.now())
    supplier = models.ForeignKey(supplier)
    product_type = models.ForeignKey(inventory)
    quantity = models.FloatField(blank=True,null=True)
    price = models.FloatField(blank=True,null=True)
    note1 = models.CharField(max_length=100, blank=True)
    note2 = models.CharField(max_length=100, blank=True)
    note3 = models.TextField(blank=True)
    def __str__(self):
        return '%s' % (self.supplier)


