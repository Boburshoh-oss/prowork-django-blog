from django.contrib import admin

# Register your models here.
from blog.models import Post,Tag
admin.site.register(Post)
admin.site.register(Tag)
