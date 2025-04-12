from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_doctor = models.BooleanField('Is Doctor', default=False)
    is_assistant = models.BooleanField('Is Assistant', default=False)
    is_patient = models.BooleanField('Is Patient', default=False)
