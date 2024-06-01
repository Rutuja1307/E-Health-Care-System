from django import forms
from django.contrib.auth.models import User
from . import models



#for admin signup
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }


#for doctor related form
class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class DoctorForm(forms.ModelForm):
    class Meta:
        model=models.Doctor
        fields=['address','mobile','department','status','profile_pic']



#for patient related form
class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class PatientForm(forms.ModelForm):
    #this is the extrafield for linking patient and their assigend doctor
    #this will show dropdown __str__ method doctor model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in Doctor model and return it
    assignedDoctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Name and Department", to_field_name="user_id")
    class Meta:
        model=models.Patient
        fields=['address','mobile','status','symptoms','profile_pic','age','weight','height']

class DateInput(forms.DateInput):
    input_type='date'
class AppointmentForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    patientId=forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True),empty_label="Patient Name and Symptoms", to_field_name="user_id")
    class Meta:
        model=models.Appointment
        fields=['description','status','appointmentDate']
        widgets={
            'appointmentDate':DateInput(),
        }

class DateInput(forms.DateInput):
    input_type='date'
class PatientAppointmentForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    class Meta:
        model=models.Appointment
        fields=['description','status','appointmentDate']
        widgets={
            'appointmentDate':DateInput(),
        }


#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))




class DrugsUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class DrugsForm(forms.ModelForm):
    class Meta:
        model=models.Drugs
        fields=['mobile','profile_pic','status']
        
        
        
class DateInput(forms.DateInput):
    input_type='date'
class StockForm(forms.ModelForm):
    class Meta:
        model=models.Stock
        fields=['drugname','category','quantity','datestock','expirydate','profile_pic','status','price']
        # fields='__all__'
        widgets={
            'datestock':DateInput(),
            'expirydate':DateInput(),
            # 'datestock':forms.DateInput(attrs={'placeholder':'stockdate'})
        }
        
class DateInput(forms.DateInput):
    input_type='date'
class NurseDetailForm(forms.ModelForm):
    class Meta:
        model=models.NurseDetail
        fields=['roomno','roomtype','allotmentDate']
        # fields='__all__'
        widgets={
            'allotmentDate':DateInput(),
            
        }
     
    
        
class DateInput(forms.DateInput):
    input_type='date'
class RoomForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    patientId=forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True),empty_label="Patient Name and Symptoms", to_field_name="user_id")
    class Meta:
        model=models.Room
        fields=['roomno','roomtype','allotmentDate']
        widgets={
            'allotmentDate':DateInput(),
        }
        

class NurseUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class NurseForm(forms.ModelForm):
    class Meta:
        model=models.Nurse
        fields=['address','mobile','status','profile_pic']
        # widgets={
        #     'login':DateInput(),
        # }