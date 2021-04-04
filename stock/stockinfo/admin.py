from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
   list_display = ('name','password','email','sex')

admin.site.register(User, UserAdmin)