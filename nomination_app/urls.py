# nomination_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.nomination_form_view, name='nomination_form'),
]
