import requests
import urllib
import cv2
import numpy as np
import os

link = "http://192.168.43.198:8080/shot.jpg"
path = "D:\\dataset"
try:
    os.mkdir(path)
    print("Directory " , name ,  " Created ") 
except FileExistsError:
    print("Directory " , name ,  " already exists")
    
print("Enter name: ")
name = input().strip()
path=path+"\\"+name

try:
    os.mkdir(path)
    print("Directory " , name ,  " Created ") 
except FileExistsError:
    print("Directory " , name ,  " already exists")

i=0
while True:
    if(i>=25):
        break
    i +=1
    imgResp = urllib.request.urlopen(link)
    imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img = cv2.imdecode(imgNp,-1)
    cv2.imshow("camera",img)
    cv2.imwrite(path+'\\'+str(i)+'.jpg',img)
    cv2.waitKey(1)
