from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SignUpForm,LoginForm
from django.contrib.auth import authenticate , login
from django.contrib import messages

# Create your views here.
# def index(request):
#     return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "User Created Successfully")
            return redirect('login_view')
        else:
            messages.error(request, "Invalid Form Submission")
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid credentials")
        else:
            messages.error(request, "Error validating form")
    return render(request, 'login.html', {'form': form})

def home(request) : 
    return render(request,'homepage.html')