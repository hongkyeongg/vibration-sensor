from time import time  

import json  

import pandas as pd  

import tablib  

import time  

import asyncio  

import joblib  

from tensorflow.keras.models import load_model  

import numpy as np  

import os  

import boto3   

import pandas as pd   

import sys   

import datetime 

from flask import Flask, render_template, make_response,request  

  

  

app = Flask(__name__)  

  

class model:  

  

    def __init__(self):  

  

        self.cover_DL = 'dl_cover_model.h5'  

        self.cover_GB = 'cover_GB.pkl'  

        self.cover_LinearSVC = 'cover_LinearSVC.pkl'  

        self.cover_LR = 'cover_LR.pkl'  

        self.motor_DL = 'dl_motor_model.h5'  

        self.motor_GB = 'motor_GB.pkl'  

        self.motor_LinearSVC = 'motor_LinearSVC.pkl'  

        self.motor_LR = 'motor_LR.pkl'  

  

    def load_cover_DL(self):  

        return load_model(self.cover_DL)  

  

    def load_cover_GB(self): 

        return joblib.load(self.cover_GB)  

  

    def load_cover_LinearSVC(self):  

        return joblib.load(self.cover_LinearSVC)  

  

    def load_cover_LR(self):  

        return joblib.load(self.cover_LR)  

  

    def load_motor_DL(self):  

        return load_model(self.motor_DL)  

    def load_motor_GB(self):  

        return joblib.load(self.motor_GB)  

  

    def load_motor_LinearSVC(self):  

        return joblib.load(self.motor_LinearSVC)  

  

    def load_motor_LR(self):  

        return joblib.load(self.motor_LR)  

  

    def predict(self, model, data):  

        return model.predict(data)  

  

  

model=model()  

dlmodel=model.load_cover_DL()  

dlmodel2=model.load_motor_DL()  

dlmodel3=model.load_cover_GB()  

dlmodel4=model.load_motor_GB()  

dlmodel5=model.load_cover_LinearSVC()  

dlmodel6=model.load_motor_LinearSVC()  

dlmodel7=model.load_cover_LR()  

dlmodel8=model.load_motor_LR()  

  

if sys.version_info[0] < 3:    

    from StringIO import StringIO # Python 2.x   

else:   

    from io import StringIO # Python 3.x   

  

# get your credentials from environment variables   

  

client = boto3.client('s3', aws_access_key_id='aws_access_key_id',   

        aws_secret_access_key='aws_secret_access_key')   

  

bucket_name = 'witsensor-bucket'   

  

  

  

  

#print(df4) 

#print(list(df4.iloc[3]))   

  

# s3 접속하기  

  

s3 = boto3.resource('s3')  

   

  

if not os.path.exists('dl_cover_model1.csv'): 

    file = open('dl_cover_model1.csv', 'w', encoding='utf-8', newline='') 

     

if not os.path.exists('dl_motor_model.csv'): 

    file = open('dl_motor_model.csv', 'w', encoding='utf-8', newline='') 

     

if not os.path.exists('load_cover_GB.csv'): 

    file = open('load_cover_GB.csv', 'w', encoding='utf-8', newline='') 

         

if not os.path.exists('load_motor_GB.csv'): 

    file = open('load_motor_GB.csv', 'w', encoding='utf-8', newline='') 

         

if not os.path.exists('load_cover_LinearSVC.csv'): 

    file = open('load_cover_LinearSVC.csv', 'w', encoding='utf-8', newline='') 

         

if not os.path.exists('load_motor_LinearSVC.csv'): 

    file = open('load_motor_LinearSVC.csv', 'w', encoding='utf-8', newline='') 

         

if not os.path.exists('load_cover_LR.csv'): 

    file = open('load_cover_LR.csv', 'w', encoding='utf-8', newline='') 

     

if not os.path.exists('load_motor_LR.csv'): 

    file = open('load_motor_LR.csv', 'w', encoding='utf-8', newline='') 

     

object_key4 = 'csv_result.csv' 

csv_obj4 = client.get_object(Bucket=bucket_name, Key=object_key4)   

body4 = csv_obj4['Body']   

csv_string4 = body4.read().decode('utf-8')   

df4 = pd.read_csv(StringIO(csv_string4), header=None)          

cnt=len(df4) 

   # 버킷 이름 확인하기   

     

for bucket in s3.buckets.all():  

  

    print(bucket.name)  

  

# S3 버킷에 있는 파일 업로드하기  

  

# 버킷 지정하기  

  

bucket_name = 'witsensor-bucket'  

  

bucket = s3.Bucket(bucket_name)  

  

   

  

# 파일 업로드하기  

#dl 

local_file1 ='/home/hongkyeong/문서/sensor/dl_cover_model1.csv' 
obj_file1 = 'dl_cover_model1.csv'   # S3 에 올라갈 파일명 
local_file2 ='/home/hongkyeong/문서/sensor/dl_motor_model.csv' 
obj_file2 = 'dl_motor_model.csv'   # S3 에 올라갈 파일명 

#ml
local_file3 ='/home/hongkyeong/문서/sensor/load_cover_GB.csv' 
obj_file3 = 'load_cover_GB.csv'   # S3 에 올라갈 파일명 
local_file4 ='/home/hongkyeong/문서/sensor/load_motor_GB.csv' 
obj_file4 = 'load_motor_GB.csv'   # S3 에 올라갈 파일명 
local_file5 ='/home/hongkyeong/문서/sensor/load_cover_LinearSVC.csv' 
obj_file5 = 'load_cover_LinearSVC.csv'   # S3 에 올라갈 파일명 
local_file6 ='/home/hongkyeong/문서/sensor/load_motor_LinearSVC.csv' 
obj_file6 = 'load_motor_LinearSVC.csv'   # S3 에 올라갈 파일명 
local_file7 ='/home/hongkyeong/문서/sensor/load_cover_LR.csv' 
obj_file7 = 'load_cover_LR.csv'   # S3 에 올라갈 파일명 
local_file8 ='/home/hongkyeong/문서/sensor/load_motor_LR.csv' 
obj_file8 = 'load_motor_LR.csv'   # S3 에 올라갈 파일명  

  


  

  

a=[] 

for i in range(0,cnt): 

    test=[] 

    for j in range(0,9): 

        val=df4.iloc[i][j] 

        test.append(val) 

    a.append(test) 

     

    #dl 

for i in range(cnt-50,cnt-10):  

    data1=a[i:i+10]  

    #print(data1)  

  

     

    data1 = np.array(data1)[:, :].astype(np.float32)  

    data1 = np.reshape(data1, (1,) + data1.shape + (1,))  

    #dl_cover_model 

    result=model.predict(dlmodel,data1)  

    result=result.tolist()  

     

    dlcovertest=([(result[0][0]), (result[0][1]),(result[0][2])])   

    to_csv = [dlcovertest.index(max(dlcovertest))]  

    df = pd.DataFrame(to_csv) 

    #print("Df1",df2) 

    df.to_csv('dl_cover_model1.csv', index=False,header=False,mode='a', encoding='cp949') 

  

             

    #dl_motor_model  

    result2=model.predict(dlmodel2,data1)  

    result2=result2.tolist()  

     

    dlmotortest=([(result2[0][0]), (result2[0][1]),(result2[0][2])])   

    to_csv2 = [dlmotortest.index(max(dlmotortest))]  

    df2 = pd.DataFrame(to_csv2) 

    #print("Df1",df2) 

    df2.to_csv('dl_motor_model.csv', index=False,header=False,mode='a', encoding='cp949') 

     

    bucket.upload_file(local_file1 , obj_file1)  

    bucket.upload_file(local_file2 , obj_file2)  

     

for i in range(cnt-50,cnt-10):  

        data3=a[i:i+10]  

        data3 = np.array(data3).astype(np.float32)  

        data3=data3.flatten()  

        data3 = np.reshape(data3,(1,90))  

  

        #load_cover_GB  

        result3=model.predict(dlmodel3,data3)  

        result3=result3.tolist()  

        to_csv3 = [(result3[0])]   

        print("load_cover_GB ",to_csv3) 

        df3 = pd.DataFrame(to_csv3) 

        df3.to_csv('load_cover_GB.csv', index=False,header=False,mode='a', encoding='cp949') 

  

        #load_motor_GB  

        result4=model.predict(dlmodel4,data3)  

        result4=result4.tolist()  

        to_csv4 = [(result4[0])]   

        print("load_motor_GB ",to_csv4) 

        df4 = pd.DataFrame(to_csv4) 

        df4.to_csv('load_motor_GB.csv', index=False,header=False,mode='a', encoding='cp949') 

             

             

        #load_cover_LinearSVC  

        result5=model.predict(dlmodel5,data3)  

        result5=result5.tolist()  

        to_csv5 = [(result5[0])]  

        print("load_cover_LinearSVC ",to_csv5) 

        df5 = pd.DataFrame(to_csv5) 

        df5.to_csv('load_cover_LinearSVC.csv', index=False,header=False,mode='a', encoding='cp949') 

             

             

        #load_motor_LinearSVC  

        result6=model.predict(dlmodel6,data3)  

        result6=result6.tolist()  

        to_csv6 = [(result6[0])]  

        print("load_motor_LinearSVC",to_csv6) 

        df6 = pd.DataFrame(to_csv6) 

        df6.to_csv('load_motor_LinearSVC.csv', index=False,header=False,mode='a', encoding='cp949') 

             

             

        #load_cover_LR  

        result7=model.predict(dlmodel7,data3)  

        result7=result7.tolist()  

        to_csv7 = [(result7[0])]  

        print("load_cover_LR ",to_csv7) 

        df7 = pd.DataFrame(to_csv7) 

        df7.to_csv('load_cover_LR.csv', index=False,header=False,mode='a', encoding='cp949') 

             

             

        #load_motor_LR  

        result8=model.predict(dlmodel8,data3)  

        result8=result8.tolist()  

        to_csv8 = [(result8[0])]  

        print("load_motor_LR ",to_csv8) 

        df8 = pd.DataFrame(to_csv8) 

        df8.to_csv('load_motor_LR.csv', index=False,header=False,mode='a', encoding='cp949') 

         

         

        bucket.upload_file(local_file3 , obj_file3)  

        bucket.upload_file(local_file4 , obj_file4)  

        bucket.upload_file(local_file5 , obj_file5)  

        bucket.upload_file(local_file6 , obj_file6)    

        bucket.upload_file(local_file7 , obj_file7)  

        bucket.upload_file(local_file8 , obj_file8)     

         

@app.route("/testgraph.html")  

def graph():  

    object_key1 = 'dl_cover_model1.csv' 

    object_key2 = 'dl_motor_model.csv' 

    object_key3 = 'csv_result.csv' 

    object_key4 = 'load_cover_GB.csv' 

    object_key5 = 'load_cover_LinearSVC.csv' 

    object_key6 = 'load_cover_LR.csv' 

    object_key7 = 'load_motor_GB.csv' 

    object_key8 = 'load_motor_LinearSVC.csv' 

    object_key9 = 'load_motor_LR.csv' 

     

     

    csv_obj1 = client.get_object(Bucket=bucket_name, Key=object_key1)   

    body1 = csv_obj1['Body']   

    csv_string1 = body1.read().decode('utf-8')  

    df1 = pd.read_csv(StringIO(csv_string1), header=None) 

    data1=list(df1[0]) 

  

  

    if(len(data1)>100): 

        data1 = data1[:70] 

     

     

     

    csv_obj2 = client.get_object(Bucket=bucket_name, Key=object_key2)   

    body2 = csv_obj2['Body']   

    csv_string2 = body2.read().decode('utf-8')  

    df2 = pd.read_csv(StringIO(csv_string2), header=None) 

    data2=list(df2[0]) 

  

  

    if(len(data2)>100): 

        data2 = data2[:70] 

  

    csv_obj3 = client.get_object(Bucket=bucket_name, Key=object_key3)   

    body3 = csv_obj3['Body']   

    csv_string3 = body3.read().decode('utf-8')  

    df3 = pd.read_csv(StringIO(csv_string3), header=None) 

    cnt=len(df3) 

    a3=[] 

  

    for i in range(0,cnt): 

        test3=[] 

        for j in range(0,9): 

            val3=df3.iloc[i][j] 

            test3.append(val3) 

        a3.append(test3) 

    data3=a3 

     

    if(len(data3)>100): 

        data3 = data3[:70] 

         

         

    csv_obj4 = client.get_object(Bucket=bucket_name, Key=object_key4)   

    body4 = csv_obj4['Body']   

    csv_string4 = body4.read().decode('utf-8')  

    df4 = pd.read_csv(StringIO(csv_string4), header=None) 

    data4=list(df4[0]) 

     

    if(len(data4)>100): 

        data4 = data4[:70] 

         

         

         

    csv_obj5 = client.get_object(Bucket=bucket_name, Key=object_key5)   

    body5 = csv_obj5['Body']   

    csv_string5 = body5.read().decode('utf-8')  

    df5 = pd.read_csv(StringIO(csv_string5), header=None) 

    data5=list(df5[0]) 

  

  

    if(len(data5)>100): 

        data5 = data5[:70] 

         

         

    csv_obj6 = client.get_object(Bucket=bucket_name, Key=object_key6)   

    body6 = csv_obj6['Body']   

    csv_string6 = body6.read().decode('utf-8')  

    df6 = pd.read_csv(StringIO(csv_string6), header=None) 

    data6=list(df6[0]) 

  

    if(len(data6)>100): 

        data6 = data6[:70] 

         

         

         

    csv_obj7 = client.get_object(Bucket=bucket_name, Key=object_key7)   

    body7 = csv_obj7['Body']   

    csv_string7 = body7.read().decode('utf-8')  

    df7 = pd.read_csv(StringIO(csv_string7), header=None) 

    data7=list(df7[0]) 

     

     

    if(len(data7)>100): 

        data7 = data7[:70] 

         

         

    csv_obj8 = client.get_object(Bucket=bucket_name, Key=object_key8)   

    body8 = csv_obj8['Body']   

    csv_string8 = body8.read().decode('utf-8')  

    df8 = pd.read_csv(StringIO(csv_string8), header=None) 

    data8=list(df8[0]) 

     

    if(len(data8)>100): 

        data8 = data8[:70] 

         

         

  

    csv_obj9 = client.get_object(Bucket=bucket_name, Key=object_key9)   

    body9 = csv_obj9['Body']   

    csv_string9 = body9.read().decode('utf-8')  

    df9 = pd.read_csv(StringIO(csv_string9), header=None)     

    data9=list(df9[0])     

     

    if(len(data9)>100): 

        data9 = data9[:70] 

     

     

  

         

    return render_template('testgraph.html',data1=data1,data2=data2,data3=data3,data4=data4,data5=data5,data6=data6,data7=data7,data8=data8,data9=data9)  

  

     

@app.route("/ax.html")  

def ax():  

    object_key1 = 'csv_x.csv' 

    csv_obj1 = client.get_object(Bucket=bucket_name, Key=object_key1)   

    body1 = csv_obj1['Body']   

    csv_string1 = body1.read().decode('utf-8')  

    df1 = pd.read_csv(StringIO(csv_string1), header=None)  

    data=list(df1[0]) 

    now = datetime.datetime.now() 

    return render_template('ax.html',data=data,now=now)  

  

@app.route("/ay.html")  

def ay():  

    object_key1 = 'csv_x.csv' 

    csv_obj1 = client.get_object(Bucket=bucket_name, Key=object_key1)   

    body1 = csv_obj1['Body']   

    csv_string1 = body1.read().decode('utf-8')  

    df1 = pd.read_csv(StringIO(csv_string1), header=None)  

    data=list(df1[1]) 

    return render_template('ay.html',data=data)  

  

@app.route("/az.html")  

def az():  

    object_key1 = 'csv_x.csv' 

    csv_obj1 = client.get_object(Bucket=bucket_name, Key=object_key1)   

    body1 = csv_obj1['Body']   

    csv_string1 = body1.read().decode('utf-8')  

    df1 = pd.read_csv(StringIO(csv_string1), header=None)  

    data=list(df1[2]) 

    return render_template('az.html',data=data)  

  

@app.route("/wx.html")  

def wx():  

    object_key1 = 'csv_y.csv' 

    csv_obj1 = client.get_object(Bucket=bucket_name, Key=object_key1)   

    body1 = csv_obj1['Body']   

    csv_string1 = body1.read().decode('utf-8')  

    df1 = pd.read_csv(StringIO(csv_string1), header=None)  

    data=list(df1[0]) 

    return render_template('wx.html',data=data)  

  

@app.route("/wy.html")  

def wy():  

    object_key1 = 'csv_y.csv' 

    csv_obj1 = client.get_object(Bucket=bucket_name, Key=object_key1)   

    body1 = csv_obj1['Body']   

    csv_string1 = body1.read().decode('utf-8')  

    df1 = pd.read_csv(StringIO(csv_string1), header=None)  

    data=list(df1[1]) 

    return render_template('wy.html',data=data)  

  

@app.route("/wz.html")  

def wz():  

    object_key1 = 'csv_y.csv' 

    csv_obj1 = client.get_object(Bucket=bucket_name, Key=object_key1)   

    body1 = csv_obj1['Body']   

    csv_string1 = body1.read().decode('utf-8')  

    df1 = pd.read_csv(StringIO(csv_string1), header=None)  

    data=list(df1[2]) 

    return render_template('wz.html',data=data)  

  

@app.route("/anglex.html")  

def anglex():  

    object_key1 = 'csv_z.csv' 

    csv_obj1 = client.get_object(Bucket=bucket_name, Key=object_key1)   

    body1 = csv_obj1['Body']   

    csv_string1 = body1.read().decode('utf-8')  

    df1 = pd.read_csv(StringIO(csv_string1), header=None)  

    data=list(df1[0]) 

    return render_template('anglex.html',data=data)   

  

  

@app.route("/angley.html")  

def angley():  

    object_key1 = 'csv_z.csv' 

    csv_obj1 = client.get_object(Bucket=bucket_name, Key=object_key1)   

    body1 = csv_obj1['Body']   

    csv_string1 = body1.read().decode('utf-8')  

    df1 = pd.read_csv(StringIO(csv_string1), header=None)  

    data=list(df1[1]) 

    return render_template('angley.html',data=data)   

  

@app.route("/anglez.html")  

def anglez():  

    object_key1 = 'csv_z.csv' 

    csv_obj1 = client.get_object(Bucket=bucket_name, Key=object_key1)   

    body1 = csv_obj1['Body']   

    csv_string1 = body1.read().decode('utf-8')  

    df1 = pd.read_csv(StringIO(csv_string1), header=None)  

    data=list(df1[2]) 

    return render_template('anglez.html',data=data) 

  

@app.route('/live-data')  

def live_data():  

     

    object_key1 = 'csv_x.csv' 

    csv_obj1 = client.get_object(Bucket=bucket_name, Key=object_key1)   

    body1 = csv_obj1['Body']   

    csv_string1 = body1.read().decode('utf-8')  

    df1 = pd.read_csv(StringIO(csv_string1), header=None)  

    results=list(df1[0]) 

    cnt=0 

    make=[] 

    #print(type(results)) 

    for i in results: 

        print(i) 

        make.append(i) 

        a=list(df1[3][cnt]) 

        a=''.join(a) 

        make.append(a) 

        cnt+=1   

    response = make_response(json.dumps(make))  

    response.content_type = 'application/json'  

    return response  

     

@app.route('/live-data1')  

def live_data1():  

     

    object_key1 = 'csv_x.csv' 

    csv_obj1 = client.get_object(Bucket=bucket_name, Key=object_key1)   

    body1 = csv_obj1['Body']   

    csv_string1 = body1.read().decode('utf-8')  

    df1 = pd.read_csv(StringIO(csv_string1), header=None)  

    results=list(df1[1]) 

    cnt=0 

    make=[] 

    #print(type(results)) 

    for i in results: 

        print(i) 

        make.append(i) 

        a=list(df1[3][cnt]) 

        a=''.join(a) 

        make.append(a) 

        cnt+=1   

    response = make_response(json.dumps(make))  

    response.content_type = 'application/json'  

    return response  

  

@app.route('/live-data2')  

def live_data2():  

     

    object_key1 = 'csv_x.csv' 

    csv_obj1 = client.get_object(Bucket=bucket_name, Key=object_key1)   

    body1 = csv_obj1['Body']   

    csv_string1 = body1.read().decode('utf-8')  

    df1 = pd.read_csv(StringIO(csv_string1), header=None)  

    results=list(df1[2]) 

    cnt=0 

    make=[] 

    #print(type(results)) 

    for i in results: 

        print(i) 

        make.append(i) 

        a=list(df1[3][cnt]) 

        a=''.join(a) 

        make.append(a) 

        cnt+=1   

    response = make_response(json.dumps(make))  

    response.content_type = 'application/json'  

    return response  

  

@app.route('/live-data3')  

def live_data3():  

     

    object_key1 = 'csv_y.csv' 

    csv_obj1 = client.get_object(Bucket=bucket_name, Key=object_key1)   

    body1 = csv_obj1['Body']   

    csv_string1 = body1.read().decode('utf-8')  

    df1 = pd.read_csv(StringIO(csv_string1), header=None)  

    results=list(df1[0]) 

    cnt=0 

    make=[] 

    #print(type(results)) 

    for i in results: 

        print(i) 

        make.append(i) 

        a=list(df1[3][cnt]) 

        a=''.join(a) 

        make.append(a) 

        cnt+=1   

    response = make_response(json.dumps(make))  

    response.content_type = 'application/json'  

    return response  

  

@app.route('/live-data4')  

def live_data4():  

     

    object_key1 = 'csv_y.csv' 

    csv_obj1 = client.get_object(Bucket=bucket_name, Key=object_key1)   

    body1 = csv_obj1['Body']   

    csv_string1 = body1.read().decode('utf-8')  

    df1 = pd.read_csv(StringIO(csv_string1), header=None)  

    results=list(df1[1]) 

    cnt=0 

    make=[] 

    #print(type(results)) 

    for i in results: 

        print(i) 

        make.append(i) 

        a=list(df1[3][cnt]) 

        a=''.join(a) 

        make.append(a) 

        cnt+=1   

    response = make_response(json.dumps(make))  

    response.content_type = 'application/json'  

    return response  

  

@app.route('/live-data5')  

def live_data5():  

     

    object_key1 = 'csv_y.csv' 

    csv_obj1 = client.get_object(Bucket=bucket_name, Key=object_key1)   

    body1 = csv_obj1['Body']   

    csv_string1 = body1.read().decode('utf-8')  

    df1 = pd.read_csv(StringIO(csv_string1), header=None)  

    results=list(df1[2]) 

    cnt=0 

    make=[] 

    #print(type(results)) 

    for i in results: 

        print(i) 

        make.append(i) 

        a=list(df1[3][cnt]) 

        a=''.join(a) 

        make.append(a) 

        cnt+=1   

    response = make_response(json.dumps(make))  

    response.content_type = 'application/json'  

    return response  

  

@app.route('/live-data6')  

def live_data6():  

     

    object_key1 = 'csv_z.csv' 

    csv_obj1 = client.get_object(Bucket=bucket_name, Key=object_key1)   

    body1 = csv_obj1['Body']   

    csv_string1 = body1.read().decode('utf-8')  

    df1 = pd.read_csv(StringIO(csv_string1), header=None)  

    results=list(df1[0]) 

    cnt=0 

    make=[] 

    #print(type(results)) 

    for i in results: 

        print(i) 

        make.append(i) 

        a=list(df1[3][cnt]) 

        a=''.join(a) 

        make.append(a) 

        cnt+=1   

    response = make_response(json.dumps(make))  

    response.content_type = 'application/json'  

    return response  

  

@app.route('/live-data7')  

def live_data7():  

     

    object_key1 = 'csv_z.csv' 

    csv_obj1 = client.get_object(Bucket=bucket_name, Key=object_key1)   

    body1 = csv_obj1['Body']   

    csv_string1 = body1.read().decode('utf-8')  

    df1 = pd.read_csv(StringIO(csv_string1), header=None)  

    results=list(df1[1]) 

    cnt=0 

    make=[] 

    #print(type(results)) 

    for i in results: 

        print(i) 

        make.append(i) 

        a=list(df1[3][cnt]) 

        a=''.join(a) 

        make.append(a) 

        cnt+=1   

    response = make_response(json.dumps(make))  

    response.content_type = 'application/json'  

    return response  

  

@app.route('/live-data8')  

def live_data8():  

     

    object_key1 = 'csv_z.csv' 

    csv_obj1 = client.get_object(Bucket=bucket_name, Key=object_key1)   

    body1 = csv_obj1['Body']   

    csv_string1 = body1.read().decode('utf-8')  

    df1 = pd.read_csv(StringIO(csv_string1), header=None)  

    results=list(df1[2]) 

    cnt=0 

    make=[] 

    #print(type(results)) 

    for i in results: 

        print(i) 

        make.append(i) 

        a=list(df1[3][cnt]) 

        a=''.join(a) 

        make.append(a) 

        cnt+=1   

    response = make_response(json.dumps(make))  

    response.content_type = 'application/json'  

    return response  

if __name__ == '__main__':  

  

    print("app.run")  

  

    app.run(debug=True, host='127.0.0.1', port=5000)  

  
