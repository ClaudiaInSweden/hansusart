from django.contrib import admin
from .models import Inquiry


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'product', 'email','date')
    search_fields = ['first_name', 'last_name', 'product']
    list_filter = ['product', 'date']

    ordering = ('-date',)