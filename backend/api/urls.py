from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('chat/', views.chat, name='chat'),  # новый эндпоинт
]