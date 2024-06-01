from django.db import models
from django.contrib.auth.models import User

category=(
    ("Antibiotics","Antibiotics"),
    ("Cardiology","Cardiology"),
    ("Dermatology/skin","Dermatology/skin"),
    ("Diabetology","Diabetology"),
    ("Gastroenterology","Gastroenterology"),
    ("Gynaecology","Gynaecology"),
    ("Hormones","Hormones"),
    ("Dental","Dental"),
    ("LiverDisorders","LiverDisorders"),
    ("Neurology","Neurology"),
    ("Nutritional Preparation","Nutritional Preparation"),
    ("Ophthalmology","Ophthalmology"),
    ("Pain Management","Pain Management"),
    ("Respiratory","Respiratory"),
    ("Urology","Urology"),
    ("Vaccines","Vaccines"),
    
)

departments=[('Cardiologist','Cardiologist'),
('General Physicians','General Physicians'),
('Dentist','Dentist'),
('Small Baby Care Specialist','Small Baby Care Specialist'),
('Orthopedic','Orthopedic'),
('Neurologist','Neurologist'),
('Respirology','Respirology'),
('Urology','Urology'),
('Gynecologist','Gynecologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons'),
]

RoomNo=(
        ("101","101"),
        ("102","102"),
        ("103","103"),
        ("104","104"),
        ("105","105"),
        ("106","106"),
        ("107","107"),
        ("108","108"),
        ("109","109"),        
)

RoomType=(
        ("General","General"),
        ("Private","Private"),
        ("ICU(Intensive Care Unit)","ICU(Intensive Care Unit)"),
        ("CCU(Cardiac/Coronary Care Unit)","CCU(Cardiac/Coronary Care Unit)"),
        ("Operation","Operation"),
        ("Surgical","Surgical"),
        ("MaternityCare","MaternityCare"),
               
)

class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)



class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    age=models.CharField(max_length=3,null=True)
    weight=models.CharField(max_length=3,null=True)
    height=models.CharField(max_length=3,null=True)
    symptoms = models.CharField(max_length=100,null=False)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    admitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name+" ("+self.symptoms+")"


class Appointment(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    appointmentDate=models.DateField(auto_now=True)
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)
    appointmentDate=models.DateField(null=True)



class PatientDischargeDetails(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40)
    assignedDoctorName=models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    symptoms = models.CharField(max_length=100,null=True)

    admitDate=models.DateField(null=False)
    releaseDate=models.DateField(null=False)
    daySpent=models.PositiveIntegerField(null=False)

    roomCharge=models.PositiveIntegerField(null=False)
    medicineCost=models.PositiveIntegerField(null=False)
    doctorFee=models.PositiveIntegerField(null=False)
    OtherCharge=models.PositiveIntegerField(null=False)
    total=models.PositiveIntegerField(null=False)

class Drugs(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/DrugsProfilePic/',null=True,blank=True)
    mobile = models.CharField(max_length=20,null=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name)
    
class Stock(models.Model):
    # user=models.OneToOneField(User,on_delete=models.CASCADE)
    drugname = models.CharField(max_length=50, null=True)
    quantity = models.IntegerField( null=True)
    price=models.IntegerField(null=True)
    category = models.CharField(max_length=50,choices=category,default='Antibiotics')
    # datestock = models.DateField(auto_now_add=False, auto_now=True)
    profile_pic= models.ImageField(upload_to='profile_pic/StockProfilePic/',null=True)
    datestock=models.DateField(null=True)
    expirydate = models.DateField(null=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.drugname+" "+self.user.category
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.drugname)
    
    
class NurseDetail(models.Model):
     # patientId=models.PositiveIntegerField(null=True)
    # doctorId=models.PositiveIntegerField(null=True)
    # patientName=models.CharField(max_length=40,null=True)
    # doctorName=models.CharField(max_length=40,null=True)
    roomno= models.IntegerField(max_length=50,choices=RoomNo,default='101')
    roomtype= models.CharField(max_length=50,choices=RoomType,default='General Ward')
    allotmentDate=models.DateField(null=True)
    status=models.BooleanField(default=False)
    
class Room(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    roomno= models.IntegerField(max_length=50,choices=RoomNo,default='101')
    roomtype= models.CharField(max_length=50,choices=RoomType,default='General Ward')
    allotmentDate=models.DateField(null=True)
    status=models.BooleanField(default=False)
    
    
class Nurse(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/NurseProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    # roomno= models.CharField(max_length=50,choices=RoomNo,default='101')
    # login=models.DateField(auto_now=True)
    # patientId=models.PositiveIntegerField(null=True)
    # doctorId=models.PositiveIntegerField(null=True)
    # patientName=models.CharField(max_length=40,null=True)
    # doctorName=models.CharField(max_length=40,null=True)
    # roomno= models.IntegerField(max_length=50,choices=RoomNo,default='101')
    # roomtype= models.CharField(max_length=50,choices=RoomType,default='General Ward')
    # allotmentDate=models.DateField(null=True)
    status=models.BooleanField(default=False)
    # status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.address)