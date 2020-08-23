from django.urls import path
from . import views

urlpatterns = [
    path('', views.projectIndex, name='projectIndex'),
    path('<int:pk>/', views.projectDetails, name='projectDetails'),
]