from django.shortcuts import render, get_object_or_404
from .models import EmployeeProfile
from django.contrib.auth.decorators import login_required

@login_required
def employee_list(request):
    employees = EmployeeProfile.objects.all()
    return render(request, 'hr_management/employee_list.html', {'employees': employees})

@login_required
def employee_detail(request, pk):
    employee = get_object_or_404(EmployeeProfile, pk=pk)
    return render(request, 'hr_management/employee_detail.html', {'employee': employee})
