from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # path('about/', views.AboutAuthorView.as_view(), name='about'),
    # path('contact/', views.AboutContactView.as_view(), name='contact'),
    path('about/', TemplateView.as_view(template_name="about.html"), name='about'),
    path('contact/', views.contact, name='contact'),
    path('taplink/', views.links, name='taplink'),
]