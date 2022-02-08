from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os
import csv
import pandas as pd
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
# Create your views here.

def index(request):
    return render(request, 'pages/home.html')
def upload(request):
    context = {}
    if request.method == 'POST':
        model = request.POST['drop1']
        upload_file = request.FILES['data']
        if upload_file.name.endswith('.csv'):
            savefile = FileSystemStorage()
            name = savefile.save("data.csv", upload_file)
            d = os.getcwd()
            file_directory = d + '\document\\' + name
        if model == 'svm':
            pass
        elif model == 'logistic':
            pass
        else:
            pass
    df = pd.read_csv("document/data.csv")    
    return render(request, 'pages/upload.html', context)
def predict(request):
    return render(request, 'pages/predict.html')