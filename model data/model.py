import joblib
from tensorflow.keras.models import load_model
import numpy as np
import sqlite3


infile=open('test.txt','r')

cnt=0
data=list()
for row in infile:
    cnt=cnt+1
    #print(row)
    tmp=row.split('\n')
    data.append(tmp[0].split(' ')[:-1])

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
infile=open('test.txt','r')
linecnt=infile.read().count("\n")+1
dlmodel=model.load_cover_DL()
dlmodel2=model.load_motor_DL()

conn = sqlite3.connect('dlresultdb4.sqlite')#저장할 db이름
curs = conn.cursor()
curs.execute("CREATE TABLE dl_cover_model (low real, medium real, high real)")
curs.execute("CREATE TABLE dl_motor_model (low real, medium real, high real)")
sql_insert="INSERT INTO dl_cover_model (low,medium,high) VALUES (?,?,?);"
sql_insert2="INSERT INTO dl_motor_model (low,medium,high) VALUES (?,?,?);"   

for i in range(linecnt-10):
    data1=data[i:i+10]
    data1 = np.array(data1)[:, :].astype(np.float32)
    data1 = np.reshape(data1, (1,) + data1.shape + (1,))    
#TABLE : test3 , 컬럼이름 : (x ,y,z)

#load_cover_DL split

    #load_cover_DL
    result=model.predict(dlmodel,data1)
    result=result.tolist()
    to_db = [(result[0][0]), (result[0][1]),(result[0][2])]
    curs.execute(sql_insert,to_db)
    
    #load_motor_DL
    result2=model.predict(dlmodel2,data1)
    result2=result2.tolist()
    to_db2 = [(result2[0][0]), (result2[0][1]),(result2[0][2])]
    curs.execute(sql_insert2,to_db2)
    
    
    print(i,result)
    print(i,result2)

conn.commit()  #커밋 (쌓아둔 명령 실행)
conn.close()
    