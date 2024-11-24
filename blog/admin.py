from django.contrib import admin
from .models import Blog, Category

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'intro',
        'date',
        'status',
    )

    ordering = ('title',)



admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)