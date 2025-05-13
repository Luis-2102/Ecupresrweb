from django.contrib import admin
from .models import Icono
# Register your models here.

@admin.register(Icono)
class Icono(admin.ModelAdmin):
    list_display = ['img']
    search_fields =['img']
    list_filter = ('created', 'updated')
