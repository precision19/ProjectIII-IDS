from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('upload/', views.upload),
    path('preview/', views.preview),
    path('predict/', views.predict)
]