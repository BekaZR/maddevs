from django.contrib import admin
from mainapp.models import User, Diagnoses, Pacient

# Registered all models in admin panel
admin.site.register(User)
admin.site.register(Pacient)
admin.site.register(Diagnoses)
