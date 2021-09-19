from django.urls import path
from . import views

app_name='about'
url_patterns = [
        path('', views.AboutView.as_view(), name='about'),
    ]

