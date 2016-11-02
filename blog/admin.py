from django.contrib import admin
from .models import Post, Comments, Keywords
from .models import Category
from mptt.admin import MPTTModelAdmin


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'parent']

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Keywords)


