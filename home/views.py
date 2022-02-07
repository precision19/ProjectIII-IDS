from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os
import csv
import pandas as pd
# Create your views here.

def index(request):
    return render(request, 'pages/home.html')
def upload(request):
    context = {}
    if request.method == 'POST':
        upload_file = request.FILES['data']
        if upload_file.name.endswith('.csv'):
            savefile = FileSystemStorage()
            name = savefile.save("data.csv", upload_file)
            d = os.getcwd()
            file_directory = d + '\document\\' + name
    df = pd.read_csv("document/data.csv")    
    return render(request, 'pages/upload.html', context)
def predict(request):
    return render(request, 'pages/predict.html')