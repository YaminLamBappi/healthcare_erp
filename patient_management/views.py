from django.shortcuts import render, get_object_or_404
from .models import PatientProfile
from django.contrib.auth.decorators import login_required

@login_required
def patient_list(request):
    patients = PatientProfile.objects.all()
    return render(request, 'patient_management/patient_list.html', {'patients': patients})
@login_required
def patient_detail(request, pk):
    patient = get_object_or_404(PatientProfile, pk=pk)
    return render(request, 'patient_management/patient_detail.html', {'patient': patient})
