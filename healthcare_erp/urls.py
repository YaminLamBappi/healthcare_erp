# healthcare_erp/urls.py

from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user_management.urls')),
    path('patients/', include('patient_management.urls')),
    path('emr/', include('emr.urls')),
    path('appointments/', include('appointments.urls')),
    path('billing/', include('billing.urls')),
    path('inventory/', include('inventory.urls')),
    path('hr/', include('hr_management.urls')),
    path('', home, name='home'),  # Add this line
]
