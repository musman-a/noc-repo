from django.contrib import admin
from .models import Icccomplaints,Ncdcomplaints,Seacomplaints,Cccomplaints,Acscomplaints,Sqcomplaints

# Register your models here.
admin.site.register(Icccomplaints)
admin.site.register(Ncdcomplaints)
admin.site.register(Seacomplaints)
admin.site.register(Cccomplaints)
admin.site.register(Acscomplaints)
admin.site.register(Sqcomplaints)