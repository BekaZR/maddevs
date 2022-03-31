from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)


class Diagnoses(models.Model):
    name_diagnos = models.CharField(verbose_name="Диагноз", max_length=127)

    def __str__(self):
        return self.name_diagnos


class Pacient(models.Model):
    date_of_birth = models.DateField()
    diagnoses = models.ManyToManyField(Diagnoses, related_name="diagnos")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.id} - {self.date_of_birth}"
