from django import forms
from .models import InvoiceModel, ProductDetails
from django.db import transaction
from django.forms import modelformset_factory

class InvoiceForm(forms.ModelForm):
    product_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    price = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    tax = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    total_price = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = InvoiceModel
        fields = ["seller_name", "seller_address", "seller_mob", "buyer_name", "buyer_address", "buyer_mob"]
        
    @transaction.atomic
    def save(self):
        invoice= super().save(commit=False) 
        invoice.save()
        product = ProductDetails.objects.create(seller_buyer_info=invoice)
        product.product_name = self.cleaned_data.get('product_name')
        product.tax = self.cleaned_data.get('tax')
        product.price = self.cleaned_data.get('price')
        product.quantity = self.cleaned_data.get('quantity')
        product.total_price = self.cleaned_data.get('total_price')
        product.save()
        return product
    
    
ProductDetailsFormset = modelformset_factory(ProductDetails, fields=("product_name", "tax", "price", "quantity", "total_price"), extra=1)