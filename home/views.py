from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'pages/home.html')
def upload(request):
    return render(request, 'pages/upload.html')
def preview(request):
    return render(request, 'pages/preview.html')
def predict(request):
    return render(request, 'pages/predict.html')