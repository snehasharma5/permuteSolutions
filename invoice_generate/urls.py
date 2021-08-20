from django.urls import path
from .views import InvoiceView, PDFView


urlpatterns = [
    path('', InvoiceView.as_view(), name="home"), 
    path('pdf/<int:pk>', PDFView.as_view(), name="pdf"),
]
