from django.contrib import admin
from blog.models import Blog
# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('article_title', 'article_body', 'count_views')
    list_filter = ('is_published',)
    list_search = ('article_title',)
