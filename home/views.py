from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os
import csv
import pandas as pd
import numpy as np
from sklearn import preprocessing, svm
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
# Create your views here.

def index(request):
    return render(request, 'pages/home.html')
def upload(request):
    context = {}
    if request.method == 'POST':
        model = request.POST['drop1']
        upload_file = request.FILES['data']
        if upload_file.name.endswith('.csv'):
            folder = 'document'
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))
            savefile = FileSystemStorage()
            name = savefile.save("data.csv", upload_file)
            d = os.getcwd()
            file_directory = d + '\document\\' + name
        df = pd.read_csv("document/data.csv")
        columns = (['duration'
        ,'protocol_type'
        ,'service'
        ,'flag'
        ,'src_bytes'
        ,'dst_bytes'
        ,'land'
        ,'wrong_fragment'
        ,'urgent'
        ,'hot'
        ,'num_failed_logins'
        ,'logged_in'
        ,'num_compromised'
        ,'root_shell'
        ,'su_attempted'
        ,'num_root'
        ,'num_file_creations'
        ,'num_shells'
        ,'num_access_files'
        ,'num_outbound_cmds'
        ,'is_host_login'
        ,'is_guest_login'
        ,'count'
        ,'srv_count'
        ,'serror_rate'
        ,'srv_serror_rate'
        ,'rerror_rate'
        ,'srv_rerror_rate'
        ,'same_srv_rate'
        ,'diff_srv_rate'
        ,'srv_diff_host_rate'
        ,'dst_host_count'
        ,'dst_host_srv_count'
        ,'dst_host_same_srv_rate'
        ,'dst_host_diff_srv_rate'
        ,'dst_host_same_src_port_rate'
        ,'dst_host_srv_diff_host_rate'
        ,'dst_host_serror_rate'
        ,'dst_host_srv_serror_rate'
        ,'dst_host_rerror_rate'
        ,'dst_host_srv_rerror_rate'
        ,'attack'
        ,'level'])
        df.columns = columns
        dos_attacks = ['apache2','back','land','neptune','mailbomb','pod','processtable','smurf','teardrop','udpstorm','worm']
        probe_attacks = ['ipsweep','mscan','nmap','portsweep','saint','satan']
        privilege_attacks = ['buffer_overflow','loadmdoule','perl','ps','rootkit','sqlattack','xterm']
        access_attacks = ['ftp_write','guess_passwd','http_tunnel','imap','multihop','named','phf','sendmail','snmpgetattack','snmpguess','spy','warezclient','warezmaster','xclock','xsnoop']
        attack_labels = ['Normal','DoS','Probe','Privilege','Access']
        def map_attack(attack):
            if attack in dos_attacks:
                attack_type = 1
            elif attack in probe_attacks:
                attack_type = 2
            elif attack in privilege_attacks:
                attack_type = 3
            elif attack in access_attacks:
                attack_type = 4
            else:
                attack_type = 0
                
            return attack_type
        attack_map = df.attack.apply(map_attack)
        df['attack_map'] = attack_map
        features_to_encode = ['protocol_type', 'service', 'flag']
        encoded = pd.get_dummies(df[features_to_encode])

        numeric_features = ['duration', 'src_bytes', 'dst_bytes']
        to_fit = encoded.join(df[numeric_features])

        binary_y = df['attack_map']
        binary_train_X, binary_val_X, binary_train_y, binary_val_y = train_test_split(to_fit, binary_y, test_size=0.6)    
        if model == 'svm':
            binary_model = svm.SVC(C=50, kernel='linear')
            binary_model.fit(binary_train_X, binary_train_y)
            binary_predictions = binary_model.predict(binary_val_X)

            # calculate and display our base accuracty
            base_rf_score = accuracy_score(binary_predictions,binary_val_y)
            pd.to_pickle(binary_model, r'./model.pickle')
            print(base_rf_score)
        elif model == 'random_forest':            
            binary_model = RandomForestClassifier()
            binary_model.fit(binary_train_X, binary_train_y)
            binary_predictions = binary_model.predict(binary_val_X)

            # calculate and display our base accuracty
            base_rf_score = accuracy_score(binary_predictions,binary_val_y)
            pd.to_pickle(binary_model, r'./model.pickle')
            print(base_rf_score)
        else:
            binary_model = LogisticRegression()
            binary_model.fit(binary_train_X, binary_train_y)
            binary_predictions = binary_model.predict(binary_val_X)

            # calculate and display our base accuracty
            base_rf_score = accuracy_score(binary_predictions,binary_val_y)
            pd.to_pickle(binary_model, r'./model.pickle')
            print(base_rf_score)
        
    return render(request, 'pages/upload.html', context)
def predict(request):
    print(request.POST.get('action'))
        # duration = float(request.POST.get('duration'))
        # print(duration)
    # model = pd.read_pickle(r'./model.pickle')

    # output = model.predict()
    return render(request, 'pages/predict.html')