from django.shortcuts import render, get_object_or_404
from .models import PatientProfile

def patient_list(request):
    patients = PatientProfile.objects.all()
    return render(request, 'patient_management/patient_list.html', {'patients': patients})

def patient_detail(request, pk):
    patient = get_object_or_404(PatientProfile, pk=pk)
    return render(request, 'patient_management/patient_detail.html', {'patient': patient})
