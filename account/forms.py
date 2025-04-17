from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Profile

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'form-control'},)
    )

    password = forms.CharField(
        widget= forms.PasswordInput(attrs={'class': 'form-control'},)
    )
    
    
class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    
    is_doctor = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    
    is_assistant = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    
    is_patient = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_doctor', 'is_assistant', 'is_patient']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'first_name', 'last_name', 'birth_date', 'blood_group', 'weight',
            'address_line1', 'address_line2', 'landmark', 'street', 'country',
            'pincode', 'state', 'city', 'bio', 'phone', 'profile_image', 'cover_image'  
        ]
