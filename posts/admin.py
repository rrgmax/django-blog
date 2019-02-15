from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)