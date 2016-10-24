from django.contrib import admin
from .models import Post
from .models import Catgory


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'parent']

admin.site.register(Post)
admin.site.register(Catgory.CatgoryAdmin)



