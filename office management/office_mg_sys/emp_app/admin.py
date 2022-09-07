from django.contrib import admin

from .models import Department, Role, employee

# Register your models here.
admin.site.register(employee)
admin.site.register(Role)
admin.site.register(Department)