from django.contrib import admin

from .models import Post


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}


admin.site.register(Post, PostAdmin)
