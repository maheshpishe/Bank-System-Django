from django.contrib import admin
from .models import Employee,Transaction,History

# admin.site.register(Position)
admin.site.register(Employee)
admin.site.register(Transaction)
admin.site.register(History)
# Register your models here.
