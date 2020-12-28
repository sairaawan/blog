from django.contrib import admin

# Register your models here.
from .models import Author, Category, Posting, Comment, PostView



admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Posting)
admin.site.register(Comment)
admin.site.register(PostView)

