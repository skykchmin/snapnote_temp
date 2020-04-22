from django.contrib import admin
from .models import Snuser

# Register your models here.
class SnuserAdmin(admin.ModelAdmin):
    list_display = ('id','email','password')

admin.site.register(Snuser, SnuserAdmin)
