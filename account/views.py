from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,LoginForm,ProfileForm
from django.contrib.auth import authenticate , login
from django.contrib import messages
from .models import Profile
from datetime import date

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
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid credentials")
        else:
            messages.error(request, "Error validating form")
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request) : 
    return render(request,'dashboard.html')

@login_required
def myprofile(request):
    try:
        profile = request.user.profile 
    except Profile.DoesNotExist:
        profile = None
    age = calculate_age(profile.birth_date) if profile else None

    return render(request, 'myprofile.html', {'profile': profile,'age' : age})


@login_required
def profile_settings(request):
    user_email = request.user.email
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        # Si le profil n'existe pas, on en crée un nouveau
        profile = Profile(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            # Assurez-vous que le profil est lié à l'utilisateur
            profile = form.save(commit=False)
            profile.user = request.user  # Lier le profil à l'utilisateur actuel
            profile.save()
            return redirect('settings')  # Rediriger après avoir enregistré les informations
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'settings.html', {'form': form, 'user_email': user_email})



def calculate_age(birth_date):
    today = date.today()
    if birth_date:
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return None