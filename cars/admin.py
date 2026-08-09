from django.contrib import admin
from .models import Cars

class MemberAdmin(admin.ModelAdmin):
    admin.site.register(Cars)