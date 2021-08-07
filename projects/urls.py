from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects, name='projects'),
    # path('post/<str:slug>/', views.post_detail, name='post'),
]