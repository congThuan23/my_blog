from django.contrib import admin
from .models import Post, Comment
class CommentInline(admin.TabularInline):
    model = Comment 

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','body','date']
    list_filter = ['date']
    search_fields = ['title']
    inlines = [CommentInline]

admin.site.register(Post,PostAdmin)