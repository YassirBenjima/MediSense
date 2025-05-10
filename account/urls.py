from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path('', views.index , name='index'),
    path('login/', views.login_view , name='login_view'),
    path('register/', views.register , name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/' , views.dashboard , name='dashboard'),
    path('myprofile/', views.myprofile , name='myprofile'),
    path('settings/', views.profile_settings , name='settings'),
    path('patients/', views.liste_patients, name='liste_patients'),
    path('patients/add/', views.add_patient, name='add_patient'),
    path('edit_patient/<int:patient_id>/', views.edit_patient, name='edit_patient'),
    path('patients/delete/<int:pk>/', views.delete_patient, name='delete_patient'),
    path('assistants/', views.liste_assistants, name='liste_assistants'),
    path('assistants/add/', views.add_assistant, name='add_assistant'),
    path('assistants/<int:assistant_id>/', views.edit_assistant, name='edit_assistant'),
    path('assistants/delete/<int:pk>/', views.delete_assistant, name='delete_assistant'),
    path('doctors/', views.liste_doctors, name='liste_doctors'),
    path('doctors/add/', views.add_doctor, name='add_doctor'),
    path('doctors/<int:doctor_id>/', views.edit_doctor, name='edit_doctor'),
    path('doctors/delete/<int:pk>/', views.delete_doctor, name='delete_doctor'),
    path('appointments/', views.schedule_list, name='schedule_list'),
    path('appointments/create/', views.schedule_create, name='schedule_create'),
    path('appointments/<int:pk>/update/', views.schedule_update, name='schedule_update'),
    path('appointments/<int:pk>/delete/', views.delete_schedule, name='schedule_delete'),
    # Patient
    path('doctors_profile',views.doctors_profile,name='doctors_profile'),
    
]
