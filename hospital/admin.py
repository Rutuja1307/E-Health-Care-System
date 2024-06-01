from django.contrib import admin
from .models import Doctor,Patient,Appointment,PatientDischargeDetails,Drugs,Stock,Room,Nurse,NurseDetail
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentAdmin)

class PatientDischargeDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatientDischargeDetails, PatientDischargeDetailsAdmin)

class DrugsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Drugs, DrugsAdmin)

class StockAdmin(admin.ModelAdmin):
    pass
admin.site.register(Stock, StockAdmin)

class NurseDetailAdmin(admin.ModelAdmin):
    pass
admin.site.register(NurseDetail, NurseDetailAdmin)

class RoomAdmin(admin.ModelAdmin):
    pass
admin.site.register(Room, RoomAdmin)

class NurseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Nurse, NurseAdmin)