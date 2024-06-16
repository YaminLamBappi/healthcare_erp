from django.urls import path
from . import views

urlpatterns = [
    path('', views.medical_record_list, name='medical_record_list'),
    path('<int:pk>/', views.medical_record_detail, name='medical_record_detail'),
]
