from django.urls import path

from .views import HomeAPIVew

urlpatterns = [
    path('homeapi/', HomeAPIVew.as_view(), name='homeapi')
]
