from django.contrib import admin
from .models import Movies,Booking,Contact
# Register your models here.

class contactAdmin(admin.ModelAdmin):
    pass
admin.site.register(Contact,contactAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display=('cs_name','cs_phno')
admin.site.register(Booking,OrderAdmin)

class MoviesAdmin(admin.ModelAdmin):
    list_display=('name','desc')
admin.site.register(Movies,MoviesAdmin)



