from django.contrib import admin
from .models import InvoiceModel, ProductDetails


admin.site.register(InvoiceModel)
admin.site.register(ProductDetails)

# Register your models here.
