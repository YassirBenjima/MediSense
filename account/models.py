from django.db import models
from django.contrib.auth.models import AbstractUser
import os

# Create your models here.

class User(AbstractUser):
    is_doctor = models.BooleanField('Is Doctor', default=False)
    is_assistant = models.BooleanField('Is Assistant', default=False)
    is_patient = models.BooleanField('Is Patient', default=False)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    blood_group = models.CharField(max_length=3, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    address_line1 = models.CharField(max_length=255, blank=True, null=True)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    landmark = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='cover_images/', blank=True, null=True)
    def __str__(self):
        return f"{self.user.username} Profile"
    def full_address(self):
        address_parts = [
            self.address_line1,
            self.address_line2,
            self.landmark,
            self.street,
            self.city,
            self.state,
            self.pincode,
            self.country
        ]
        return ', '.join([part for part in address_parts if part])

def delete_old_file(file_field):
    if file_field and os.path.isfile(file_field.path):
        os.remove(file_field.path)

