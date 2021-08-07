from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.AboutAuthorView.as_view(), name='about'),
    path('contact/', views.AboutContactView.as_view(), name='contact'),
]