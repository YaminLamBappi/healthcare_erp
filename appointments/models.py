from django.db import models
from user_management.models import User
from patient_management.models import PatientProfile

class Appointment(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_doctor': True})
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return f"Appointment with Dr. {self.doctor.username} for {self.patient.user.username} on {self.date}"
