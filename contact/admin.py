from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'topic', 'date', 'answered')
    list_filter = ('date', 'answered')
    search_fields = ['name', 'email', 'message']

    ordering = ('-date',)