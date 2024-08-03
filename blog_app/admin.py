from django.contrib import admin
from .models import Post,Comment
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','message','image']
    search_fields = ['title']

@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name','text']
    search_fields = ['name']
