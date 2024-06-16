from django.db import models
from patient_management.models import PatientProfile

class Invoice(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"Invoice for {self.patient.user.username} on {self.date}"
