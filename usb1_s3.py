
import serial  

import time 

import pandas as pd 

import os 

import boto3 

s = serial.Serial("/dev/ttyACM0", 115200)  

  

  

while True:  

  

    data = s.readline()  

    print(data)  

    now = time.localtime() 

    a="%04d/%02d/%02d/%02d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec) 

    print(a) 

    data=str(data) 

    cnt=len(data.split(' ')) 

    result1=data.split(' ') 

    num=result1[0] 

             

             

             

# s3 접속하기 

    s3 = boto3.resource('s3') 

  

# 버킷 이름 확인하기 

    for bucket in s3.buckets.all(): 

        print(bucket.name) 

# S3 버킷에 있는 파일 업로드하기 

# 버킷 지정하기 

    bucket_name = 'witsensor-bucket' 

    bucket = s3.Bucket(bucket_name) 

  

# 파일 업로드하기 

    local_file1 ='/home/hongkyeong/문서/sensor/csv_x.csv' 

    obj_file1 = 'csv_x.csv'   # S3 에 올라갈 파일명 

    local_file2 ='/home/hongkyeong/문서/sensor/csv_y.csv' 

    obj_file2 = 'csv_y.csv'   # S3 에 올라갈 파일명 

    local_file3 ='/home/hongkyeong/문서/sensor/csv_z.csv' 

    obj_file3 = 'csv_z.csv'   # S3 에 올라갈 파일명 

    local_file4 ='/home/hongkyeong/문서/sensor/csv_result.csv' 

    obj_file4 = 'csv_result.csv'   # S3 에 올라갈 파일명 

  

  

  

     

     

    if cnt==10 and len(num)>5: 

        if not os.path.exists('csv_x.csv'): 

             

            test=result1[0].split('\'') 

            list1 = [] 

            list1.append([(float(test[1])), (float(result1[1])),(float(result1[2])),a]) 

            df1 = pd.DataFrame(list1) 

            df1.to_csv('csv_x.csv', index=False,header=False,mode='w', encoding='cp949') 

         

            list2 = [] 

            list2.append([(float(result1[3])), (float(result1[4])), (float(result1[5])),a]) 

            df2 = pd.DataFrame(list2) 

            df2.to_csv('csv_y.csv', index=False,header=False,mode='w', encoding='cp949') 

         

            list3 = [] 

            list3.append([(float(result1[6])), (float(result1[7])), (float(result1[8])),a]) 

            df3 = pd.DataFrame(list3) 

            df3.to_csv('csv_z.csv', index=False,header=False,mode='w', encoding='cp949') 

         

            list4 = [] 

            list4.append([(float(test[1])), (float(result1[1])), (float(result1[2])),(float(result1[3])), (float(result1[4])), (float(result1[5])),(float(result1[6])), (float(result1[7])), (float(result1[8])),a]) 

            df4 = pd.DataFrame(list4) 

            df4.to_csv('csv_result.csv', index=False,header=False,mode='w', encoding='cp949') 

            bucket.upload_file(local_file1 , obj_file1) 

            bucket.upload_file(local_file2 , obj_file2) 

            bucket.upload_file(local_file3 , obj_file3) 

            bucket.upload_file(local_file4 , obj_file4) 

  

        else: 

            test=result1[0].split('\'') 

            list1 = [] 

            list1.append([(float(test[1])), (float(result1[1])),(float(result1[2])),a]) 

            df1 = pd.DataFrame(list1) 

            df1.to_csv('csv_x.csv', index=False,header=False,mode='a', encoding='cp949') 

         

            list2 = [] 

            list2.append([(float(result1[3])), (float(result1[4])), (float(result1[5])),a]) 

            df2 = pd.DataFrame(list2) 

            df2.to_csv('csv_y.csv', index=False,header=False,mode='a', encoding='cp949') 

         

            list3 = [] 

            list3.append([(float(result1[6])), (float(result1[7])), (float(result1[8])),a]) 

            df3 = pd.DataFrame(list3) 

            df3.to_csv('csv_z.csv', index=False,header=False,mode='a', encoding='cp949') 

         

         

            list4 = [] 

            list4.append([(float(test[1])), (float(result1[1])), (float(result1[2])),(float(result1[3])), (float(result1[4])), (float(result1[5])),(float(result1[6])), (float(result1[7])), (float(result1[8])),a]) 

            df4 = pd.DataFrame(list4) 

            df4.to_csv('csv_result.csv', index=False,header=False,mode='a', encoding='cp949') 

            bucket.upload_file(local_file1 , obj_file1) 

            bucket.upload_file(local_file2 , obj_file2) 

            bucket.upload_file(local_file3 , obj_file3) 

            bucket.upload_file(local_file4 , obj_file4) 

       

        print(df1) 

        print(df2) 

        print(df3) 

        print(df4) 
