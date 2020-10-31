import numpy as np 
import cv2 
  
cap = cv2.VideoCapture('overpass.mp4') #To run a video file with moving objects
#cap = cv2.VideoCapture(0) #To run a video by accessing the web camera of laptop

#METHOD-1
backSub = cv2.createBackgroundSubtractorMOG2() # a Gaussian Mixture-based Background/Foreground Segmentation Algorithm
#One important feature of this algorithm is that it selects the appropriate number of gaussian distribution for each pixel.

#METHOD-2
#backSub = cv2.createBackgroundSubtractorKNN()

#Check whether the video is captured or not
if not cap.isOpened:
    print('Unable to open')
    exit(0)

  
while(1): 
    ret, frame = cap.read()
    if frame is None:
        break

    #update the background model
    fgmask = backSub.apply(frame,learningRate=0.01)
    mask=cv2.cvtColor(fgmask,cv2.COLOR_GRAY2BGR)
    #show the current frame and the fg masks
    cv2.imshow('frame', frame) 
    cv2.imshow('mask', mask&frame) 
  
    #press esc key to stop the loop
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break
