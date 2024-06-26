from django.shortcuts import render, get_object_or_404
from .models import MedicalRecord
from django.contrib.auth.decorators import login_required


@login_required
def medical_record_list(request):
    records = MedicalRecord.objects.all()
    return render(request, 'emr/medical_record_list.html', {'records': records})

@login_required
def medical_record_detail(request, pk):
    record = get_object_or_404(MedicalRecord, pk=pk)
    return render(request, 'emr/medical_record_detail.html', {'record': record})
