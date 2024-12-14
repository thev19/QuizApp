from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

from quiz.views import welcome_page

urlpatterns = [
    path('', welcome_page, name='welcome'),
    path('admin/', admin.site.urls),
    path('quiz/', include('quiz.urls')),
]