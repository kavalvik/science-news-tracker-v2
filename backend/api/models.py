from django.db import models
from pgvector.django import VectorField

class Article(models.Model):
    title = models.CharField(max_length=500, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    source = models.CharField(max_length=200, blank=True, verbose_name="Источник")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    #embedding = VectorField(dimensions=384, null=True, blank=True)  # <-- добавить эту строку
    
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title[:50]