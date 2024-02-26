from django.contrib import admin
from  .models import  *
# Register your models here.
class contactAdmin(admin.ModelAdmin):
    list_display = ('fname','lname','email','message')
admin.site.register(contact,contactAdmin)

class vehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicleimage','rent','vehicle1','vehicle2','vehicle3')
admin.site.register(vehicle,vehicleAdmin)

class ourserviceAdmin(admin.ModelAdmin):
    list_display = ('heading','des')
admin.site.register(ourservice,ourserviceAdmin)

class testimonialsAdmin(admin.ModelAdmin):
    list_display = ('desc','picture','name')
admin.site.register(testimonials,testimonialsAdmin)

