from django.contrib import admin

# Register your models here.
from .models import Create, Contact

admin.site.register(Create)
admin.site.register(Contact)