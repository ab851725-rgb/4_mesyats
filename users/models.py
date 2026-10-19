from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Мужской'),
        ('F', 'Женский'),
    )

    phone_number = models.CharField(max_length=20, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.username