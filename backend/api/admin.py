from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'source', 'created_at']
    search_fields = ['title', 'content']
    list_filter = ['source', 'created_at']