from tkinter import *
from os import listdir
from os.path import isfile, join
from tkinter.ttk import *
from PIL import ImageTk
import ctypes
import os
import tkinter as tk
import cv2
import shutil
import csv
import time
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import tkinter.ttk as ttk
import tkinter.font as font
import openpyxl
import subprocess
import pyodbc
from pyodbc import Error



user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

window = Tk()
window.title("FAST NU Face Recogniser Attendance System")

canvas = Canvas(width = 100, height = 160, bg = '#5D6D7E')
canvas.pack(expand = YES, fill = BOTH)
image = ImageTk.PhotoImage(file = "C:/Users/Zaka/Desktop/Python/image.jpg")
canvas.create_image(0, 0, image = image, anchor = NW)

load = Image.open("C:/Users/Zaka/Desktop/Python/nuces.png")
render = ImageTk.PhotoImage(load)
img = Label(window, image=render)
img.image = render
img.place(x=480, y=65)


window.attributes('-fullscreen', True)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

message = tk.Label(window, text=" Face Recognition Attendance System For Fast Lahore" ,fg='#A2D9CE' ,bg="#34495E" ,width=50  ,height=1,font=('times', 18, ' bold ')) 
message.place(x=345, y=13)

lbl = tk.Label(window, text="Student Number",width=16  ,height=1  ,fg="#A2D9CE"  ,bg="#34495E" ,font=('times', 15, ' bold ') ) 
lbl.place(x=480, y=200)

txt = tk.Entry(window,width=23 ,bg="#A2D9CE" ,fg="Black",font=('times', 15, ' bold '))
txt.place(x=690, y=200)

lbl2 = tk.Label(window, text="Student Name",width=16  ,fg="#A2D9CE"  ,bg="#34495E"    ,height=1 ,font=('times', 15, ' bold ')) 
lbl2.place(x=480, y=250)

txt2 = tk.Entry(window,width=23  ,bg="#A2D9CE"  ,fg="Black",font=('times', 15, ' bold ')  )
txt2.place(x=690, y=250)

lbl5 = tk.Label(window, text="Degree",width=16  ,fg="#A2D9CE"  ,bg="#34495E"    ,height=1 ,font=('times', 15, ' bold ')) 
lbl5.place(x=480, y=300)

txt5 = tk.Entry(window,width=23  ,bg="#A2D9CE"  ,fg="Black",font=('times', 15, ' bold ')  )
txt5.place(x=690, y=300)

lbl3 = tk.Label(window, text="Notification Bar ",width=20  ,fg="#A2D9CE"  ,bg="#34495E"  ,height=1 ,font=('times', 15, ' bold  ')) 
lbl3.place(x=580, y=450)

lbl4 = tk.Label(window, text="Status ",width=20  ,fg="#A2D9CE"  ,bg="#34495E"  ,height=1 ,font=('times', 15, ' bold  ')) 
lbl4.place(x=580, y=610)

message = tk.Label(window, text="" ,bg="#A2D9CE"  ,fg="Green"  ,width=30  ,height=1, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
message.place(x=517, y=490)

message1 = tk.Label(window, text="" ,bg="#A2D9CE"  ,fg="Black"  ,width=40  ,height=3, activebackground = "yellow" ,font=('times', 20, ' bold ')) 
message1.place(x=378, y=650)

try:
    con = pyodbc.connect('Driver={SQL Server};'
                      'Server=.\SQL2014;'
                      'Database=Attendance_System;'
                      'Trusted_Connection=yes;')

    if con:
        res="Database Connected"
        message.configure(text=res)

except Error as e:
    print("Error while connecting to MySQL", e)

cursor = con.cursor()



def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def open_excel_file():
    path="C:/Users/Zaka/Desktop/Python/Attendance"
    path=os.path.realpath(path)
    os.startfile(path)


def face_extractor(img):
    face_classifier = cv2.CascadeClassifier('C:/Python/Python 3.7.4/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)

    if faces is():
        return None

    for(x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]

    return cropped_face

error="Database Constraint Error"

def is_alpha(str):
    count = 0
    for ch in str:
        if ch.isalpha() or ch.isspace():
            count = count + 1
    if count == len(str):
        return True
    return False

def checkL(str):
    if str[2] == 'L':
        return True
    return False
        

def checkIdFirstTwo(str):
    if((str[0]>='0' and str[0]<='9') and (str[1]>='1' and str[1]<='9')):
        return True
    return False

def checkIdLastFour(str):
    temp = ""
    if(len(str) == 7):
        temp += str[3]+str[4]+str[5]+str[6]
    num = int(temp,10)
    if(num >= 1 and num <= 9999):
        return True
    return False


def checkIdLen(str):
    if len(str) == 7:
        return True
    return False

def Take_image():
    
    Id=txt.get()

    name=txt2.get() 
 
    degree=txt5.get()
    if((checkL(Id) and checkIdFirstTwo(Id) and checkIdLastFour(Id) and len(Id) != 0 and checkIdLen(Id) and is_alpha(name) and len(name)!=0 and  len(degree)!=0)):#
        try:
            cursor.execute('''Exec  [dbo].[insertStudent]
                            @sid = ?,
                            @snam = ?,
                            @Deg = ?''', Id, name , degree )
            con.commit()
            Id = Id.replace("L", "")
            cam = cv2.VideoCapture(0)
            count = 0
            harcascadePath = "C:/Python/Python 3.7.4/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml"
            detector=cv2.CascadeClassifier(harcascadePath)
            while True:
                ret, frame = cam.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x,y,w,h) in faces:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                    count+=1
                    cv2.imshow('Face Sampling',frame)
                    print("Face Sample " + str(count) )
                    cv2.imwrite("C:/Users/Zaka/Desktop/Python/Faces/ "+name +"."+ Id +'.'+ str(count) + ".jpg", gray[y:y+h,x:x+w])

                else:
                    res="Face recognizing in process"
                    pass

                if cv2.waitKey(1) & 0xFF == ord('q') or count==100:
                    break

            cam.release()
            cv2.destroyAllWindows()
            res = "Images Saved for Student Id : " + Id + ' ' + name
            row = [Id,name,degree]
            with open(r'C:/Users/Zaka/Desktop/Python/Student_details.csv','a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
                csvFile.close()
                message.configure(text=res) 
        
        except:
            res="Database Constraint Error"
            message.configure(text=res)
    
    else:
            
        if (not checkL(Id)):
            res="Student Number format should be **L****"
            message.configure(text=res)
        if(not checkIdLastFour(Id)):
            res="Last 4 letters should be > 0001"
            message.configure(text=res)
        if (not checkIdFirstTwo(Id)):
            res="First 2 letters should be > 00"
            message.configure(text=res)
        if (not checkIdLen(Id)):
            res = "Student Number length should be 7"
            message.configure(text=res)
        if (not is_alpha(name)):
            res =  "Enter only Alphabets in Name"
            message.configure(text=res)
        if (not is_alpha(degree)):
            res="Enter only Alphabets in Degree"
            message.configure(text=res)
        if len(Id) == 0:
            res="Id cannot be empty"
            message.configure(text=res)
        if len(degree) == 0:
            res="Degree cannot be empty"
            message.configure(text=res) 
        if len(name) == 0:
            res="Name cannot be empty"
            message.configure(text=res)   


def Train_Samples():
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    harcascadePath = "C:/Python/Python 3.7.4/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml"
    detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndIds("C:/Users/Zaka/Desktop/Python/Faces")
    recognizer.train(faces, np.array(Id))
    recognizer.save("C:/Users/Zaka/Desktop/Python/TrainingImageLabel/Trainer.yml")
    res = "Image Trained"
    message.configure(text= res)

def getImagesAndIds(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    #print(imagePaths)
    
    #create stdth face list
    faces=[]
    #create stdty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)        
    return faces,Ids


def Mark_Attendance():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("C:/Users/Zaka/Desktop/Python/TrainingImageLabel/Trainer.yml")
    harcascadePath = "C:/Python/Python 3.7.4/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);    
    df=pd.read_csv("C:/Users/Zaka/Desktop/Python/Student_details.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names =  ['Id','Name','Degree','Date','Time']
    attendance = pd.DataFrame(columns = col_names)
    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id,conf = recognizer.predict(gray[y:y+h,x:x+w])
            if(conf < 80 ):
                ts = time.time()      
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                std_nam=df.loc[df['Id'] == Id] ['Name'].values
                Degree =df.loc[df['Id']==Id] ['Degree'].values
                attendance.loc[len(attendance)] = [Id,std_nam,Degree,date,timeStamp]
                try:
                    nId = int(Id,10)
                    nstdName = str(std_nam)
                    nDegree = str(Degree)
                    ntime = str(timeStamp)
                    ndate = str(date)
                    cursor.execute('''Exec  [dbo].[InsertAttendance]
                        @Id = ?,
                        @std_nam = ?,
                        @Degree = ?,
                        @time = ?,
                        @date=?
                        ''', nId, nstdName , nDegree,ntime,ndate)
                    con.commit()
                except:
                    res="Attendance Already Marked"
                    message.configure(text=res)
        attendance=attendance.drop_duplicates(subset=['Id'],keep='first')
        cv2.imshow('Image Scanner',im) 
        if (cv2.waitKey(1)==ord('q')):
            break
    #ts = time.time()      
    #date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour,Minute,Second=timeStamp.split(":")
    fileName="C:/Users/Zaka/Desktop/Python/Attendance/Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    attendance.to_csv(fileName,index=False)
    cam.release()
    cv2.destroyAllWindows()
    res=attendance
    message1.configure(text= res)
    r = "Attendance Updated"
    message.configure(text= r)

def minimize():
    window.iconify()
def quit():
    window.destroy()

takeImg = tk.Button(window, text="Take Samples", command=Take_image  ,fg='green'  ,bg='#17202A'  ,width=13  ,height=1, activebackground = "red" ,font=('times', 15, ' bold '))
takeImg.place(x=480, y=350)

trainImg = tk.Button(window, text="Train Samples",command = Train_Samples, fg='green'  ,bg='#17202A'  ,width=13  ,height=1, activebackground = "red" ,font=('times', 15, ' bold '))
trainImg.place(x=760, y=350)

AttendanceImg = tk.Button(window, text="Mark Attendance",command = Mark_Attendance, fg='green'  ,bg='#17202A'  ,width=13  ,height=1, activebackground = "red" ,font=('times', 15, ' bold '))
AttendanceImg.place(x=480, y=400)



Open_excel = tk.Button(window, text="Open Attendance Folder",command = open_excel_file, fg='white'  ,bg='#17202A'  ,width=18  ,height=1, activebackground = "red" ,font=('times', 12, ' bold '))
Open_excel.place(x=615, y=540)

lbl6 = tk.Label(window, text="Powered By Saad (AI Project)",width=25  ,fg="#A2D9CE"  ,bg="#34495E"    ,height=1 ,font=('times', 15, ' bold ')) 
lbl6.place(x=3, y=735)

PhotoImage1=tk.PhotoImage(file="C:/Users/Zaka/Desktop/Python/close.png")
quitWindow = tk.Button(window,  command=quit , image=PhotoImage1 ,activebackground = "Red")
quitWindow.place(x=1325, y=1)

PhotoImage2=tk.PhotoImage(file="C:/Users/Zaka/Desktop/Python/min.png")
minimize = tk.Button(window, command=minimize, image = PhotoImage2 , activebackground = "red")
minimize.place(x=1290, y=1)

window.mainloop()







