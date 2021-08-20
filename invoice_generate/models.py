from django.db import models
from django.utils import timezone
from django.urls import reverse

class InvoiceModel(models.Model):
    seller_name = models.CharField(max_length=100)
    seller_address = models.CharField(max_length=200)
    seller_mob = models.CharField(max_length=10)
    
    buyer_name = models.CharField(max_length=100)
    buyer_address = models.CharField(max_length=200)
    buyer_mob = models.CharField(max_length=10)
    
    def __str__(self):
        return self.seller_name + " | " + self.buyer_name

    def get_absolute_url(self):
        return reverse('pdf', args=[str(self.pk)])
    
class ProductDetails(models.Model):
    seller_buyer_info = models.ForeignKey(InvoiceModel, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    tax = models.FloatField(default=0)
    price = models.FloatField(default=0)
    total_price = models.FloatField(default=0, null=True, blank=True)
    date = models.DateField(default=timezone.now)
    
    def __str__(self):
        return str(self.seller_buyer_info)
    
    def get_absolute_url(self):
        return reverse('pdf', args=[str(self.pk)])
     
    
    