from django.db import models
from patient_management.models import PatientProfile

class MedicalRecord(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()
    prescription = models.TextField()

    def __str__(self):
        return f"Record for {self.patient.user.username} on {self.date}"
