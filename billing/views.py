from django.shortcuts import render, get_object_or_404
from .models import Invoice
from django.contrib.auth.decorators import login_required

@login_required
def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'billing/invoice_list.html', {'invoices': invoices})

@login_required
def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return render(request, 'billing/invoice_detail.html', {'invoice': invoice})
