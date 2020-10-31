import cv2
from sklearn.cluster import KMeans
import numpy as np
import math
img=cv2.imread("car_color3.jpg")
cv2.imshow("img",img)
cv2.waitKey(0)
x=[]
h,w,c=img.shape
for i in range(len(img)):
    for j in range(len(img[i])):
        x.append(img[i][j])
model=KMeans(n_clusters=5)
model=model.fit(x)
centers=model.cluster_centers_
predictions=model.labels_
s=set(predictions)
print(s)
ct={}
for i in predictions:
    if i not in ct:
        ct[i]=1
    else:
        ct[i]+=1
print(ct)
maxi=0
for i in ct:
    if ct[i]>maxi:
        maxi=ct[i]
        maxi_ind=i
print(maxi_ind,maxi)
req_center=centers[maxi_ind]
print(req_center)
b,g,r = int(req_center[0]),int(req_center[1]),int(req_center[2])
print(r,g,b)

color_dic={(250,250,250):"white",
           (225,225,225):"silver",
           (220,220,220):"gray",
           (150,150,150):"darkgray",
           (75,75,75):"black",
           (230,170,0):"yellow",
           (180, 0, 0):"maroon",
           (255,0,0):"red",
           (0,255,0):"green",
           (0,0,255):"blue"}
mini=float("inf")
for i in color_dic:
    diff=((r-i[0])**2+(g-i[1])**2+(b-i[2])**2)**0.5
    if diff<mini:
        mini=diff
        color=color_dic[i]
print(color)

