from django.urls import reverse_lazy
from django.db.transaction import commit
from django.views.generic import CreateView
from .models import InvoiceModel, ProductDetails
from .forms import InvoiceForm, ProductDetailsFormset
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, request
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf


class InvoiceView(CreateView):
    model = InvoiceModel
    form_class = InvoiceForm
    template_name = 'invoice_generate/home.html'
    
    def get_context_data(self,*args, **kwargs):
        context = super(InvoiceView, self).get_context_data(*args, **kwargs)
        return context


class PDFView(View):
    model = InvoiceModel
    template_name = 'invoice_generate/pdf.html'
    
    def get(self,request, *args, **kwargs):
        template = get_template('invoice_generate/pdf.html')
        bill = get_object_or_404(InvoiceModel, id=self.kwargs['pk'])
        product = ProductDetails.objects.filter(seller_buyer_info=bill)
        print(product)
        context={'bill': bill, 'product':product}

        html = template.render(context)
        pdf = render_to_pdf('invoice_generate/pdf.html', context)
        
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % "12341231"
            content = "inline; filename='%s'" % filename
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % filename
            response['Content-Dispostion'] = content
            return response
        return HttpResponse("Not found")
        
# Create your views here.
