from django.contrib import admin
from mainapp.models import User, Diagnoses, Pacient

admin.site.register(User)
admin.site.register(Pacient)
admin.site.register(Diagnoses)
