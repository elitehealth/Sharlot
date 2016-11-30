from django.contrib import admin

# Register your models here.

from .models import add_inventory, inventory, supplier,product_type
admin.site.register(inventory)
admin.site.register(product_type)
admin.site.register(add_inventory)
admin.site.register(supplier)


