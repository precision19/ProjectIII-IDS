from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('upload/', views.upload),
    path('predict/', views.predict)
]