from django.contrib import admin
from .models import Product, Category

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'sold',
        'highlight',
        'width',
        'height',
        'image',
    )

    ordering = ('title',)



admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
