from django.contrib import admin

from .models import Blog

# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','is_special','status')
    search_fields = ('title','author','category__title')
    list_filter = ('status','is_special','publish')
    list_per_page = 30