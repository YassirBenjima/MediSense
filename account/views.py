from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,LoginForm,ProfileForm,UserForm
from django.contrib.auth import authenticate , login
from django.contrib import messages
from .models import Profile,delete_old_file,User
from datetime import date
from django.db.models import Q

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
    profile = request.user.profile 
    return render(request,'dashboard.html', {'profile': profile})

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
        profile = Profile(user=request.user)

    old_profile_image = profile.profile_image.path if profile.profile_image else None
    old_cover_image = profile.cover_image.path if profile.cover_image else None

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            new_profile_image = request.FILES.get('profile_image')
            new_cover_image = request.FILES.get('cover_image')

            if new_profile_image and old_profile_image:
                delete_old_file(profile.profile_image)

            if new_cover_image and old_cover_image:
                delete_old_file(profile.cover_image)
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('settings')
    else:
        form = ProfileForm(instance=profile)
    profile = request.user.profile 

    return render(request, 'settings.html', {'form': form, 'user_email': user_email, 'profile': profile})

def calculate_age(birth_date):
    today = date.today()
    if birth_date:
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return None

@login_required
def liste_patients(request):
    user_email = request.user.email
    search_query = request.GET.get('search', '')
    blood_group = request.GET.get('blood_group', '')

    patients = User.objects.filter(is_patient=True).select_related('profile')

    # Filtres
    if search_query:
        patients = patients.filter(
            Q(username__icontains=search_query) |
            Q(profile__first_name__icontains=search_query) |
            Q(profile__last_name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(profile__city__icontains=search_query) |
            Q(profile__country__icontains=search_query)
        )

    if blood_group:
        patients = patients.filter(profile__blood_group=blood_group)

    # Statistiques dynamiques
    stable_count = 0
    good_count = 0
    critical_count = 0

    age_25_plus = 0
    age_16_30 = 0
    age_0_15 = 0

    for patient in patients:
        profile = patient.profile
        age = calculate_age(profile.birth_date)
        weight = getattr(profile, 'weight', 0)

        # Catégorisation santé selon âge et poids (à ajuster si besoin)
        if 18 <= age <= 60 and 50 <= weight <= 90:
            stable_count += 1
        elif (age < 18 or age > 60) and (weight >= 45 and weight <= 95):
            good_count += 1
        else:
            critical_count += 1

        # Catégorisation par tranches d’âge
        if age > 25:
            age_25_plus += 1
        elif 16 <= age <= 25:
            age_16_30 += 1
        else:
            age_0_15 += 1

    context = {
        'patients': patients,
        'user_email': user_email,
        'stable_count': stable_count,
        'good_count': good_count,
        'critical_count': critical_count,
        'age_25_plus': age_25_plus,
        'age_16_30': age_16_30,
        'age_0_15': age_0_15,
    }

    return render(request, 'patients/liste_patients.html', context)

@login_required
def add_patient(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.is_patient = True
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            messages.success(request, "Patient added successfully.")
            return redirect('liste_patients')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'patients/add_patient.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
    
@login_required
def edit_patient(request, patient_id):
    patient = get_object_or_404(User, id=patient_id)
    profile = patient.profile

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=patient)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            password = request.POST.get('password')
            if password:
                user_form.instance.set_password(password)

            user_form.save() 
            profile_form.save() 

            messages.success(request, "Patient updated successfully.")
            return redirect('liste_patients')
    else:
        user_form = UserForm(instance=patient)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'patients/edit_patient.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'patient': patient
    })
    
@login_required
def delete_patient(request, pk):
    patient = get_object_or_404(User, pk=pk)
    patient.delete()
    messages.success(request, "Patient deleted successfully.")
    return redirect('liste_patients')

@login_required
def liste_assistants(request):
    user_email = request.user.email
    search_query = request.GET.get('search', '')
    blood_group = request.GET.get('blood_group', '')
    assistants = User.objects.filter(is_assistant=True).select_related('profile')
    if search_query:
        assistants = assistants.filter(
            Q(username__icontains=search_query) |
            Q(profile__first_name__icontains=search_query) |
            Q(profile__last_name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(profile__city__icontains=search_query) |
            Q(profile__country__icontains=search_query)
        )
    if blood_group:
        assistants = assistants.filter(profile__blood_group=blood_group)
    context = {
        'assistants': assistants,
        'user_email': user_email,
    }

    return render(request, 'assistants/liste_assistants.html', context)

@login_required
def add_assistant(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.is_assistant = True
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            messages.success(request, "Assistant added successfully.")
            return redirect('liste_assistants')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'assistants/add_assistant.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def edit_assistant(request,assistant_id) : 
    assistant = get_object_or_404(User, id=assistant_id)
    profile = assistant.profile

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=assistant)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            password = request.POST.get('password')
            if password:
                user_form.instance.set_password(password)

            user_form.save() 
            profile_form.save() 

            messages.success(request, "Assistant updated successfully.")
            return redirect('liste_assistants')
    else:
        user_form = UserForm(instance=assistant)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'assistants/edit_assistant.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'assistant': assistant
    })

@login_required
def delete_assistant(request,pk) : 
    assistant = get_object_or_404(User, pk=pk)
    assistant.delete()
    messages.success(request, "Assistant deleted successfully.")
    return redirect('liste_assistants')