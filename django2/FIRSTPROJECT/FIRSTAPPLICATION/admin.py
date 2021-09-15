from django.contrib import admin
from .models import teacher, student, service_provider

# Register your models here.
admin.site.register(teacher)
admin.site.register(student)
admin.site.register(service_provider)
