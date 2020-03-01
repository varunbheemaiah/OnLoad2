
import numpy as np
import cv2
from time import time,localtime,strftime
from requests import get
from json import loads,dumps
import numpy as np

org=(260,25)
org2=(10,30)
fontScale=1
font = cv2.FONT_HERSHEY_SIMPLEX
color=(0,0,255)
thickness = 2
cap = cv2.VideoCapture(0)
text='DIM'

while(True):
	ret, frame = cap.read()
	start = 'Start : Mysuru ,Karnataka ,India'
	end = 'End : Banglore, Karnataka, India'
	distance = "Distance : 146 km"
	time_taken = "Time : 3 hours 10 mins"
	speed = "Average speed : 69 km/h"
	frame = cv2.putText(frame,start,(10,370),font,0.4,(255,255,255),1,cv2.LINE_AA,False)
	frame = cv2.putText(frame,end,(10,385),font,0.4,(255,255,255),1,cv2.LINE_AA,False)
	frame = cv2.putText(frame,distance,(10,400),font,0.4,(255,255,255),1,cv2.LINE_AA,False)
	frame = cv2.putText(frame,time_taken,(10,415),font,0.4,(255,255,255),1,cv2.LINE_AA,False)
	frame = cv2.putText(frame,speed,(10,430),font,0.4,(255,255,255),1,cv2.LINE_AA,False)
	
	time_ = strftime("%H:%M",localtime(time()))
	date = strftime("%D",localtime(time()))
	frame = cv2.putText(frame,text,org,font,fontScale,color,thickness,cv2.LINE_AA,False)
	frame = cv2.putText(frame,time_,org2,font,0.6,color,1,cv2.LINE_AA,False)
	frame = cv2.putText(frame,date,(520,30),font,0.6,color,1,cv2.LINE_AA,False)
	cv2.namedWindow('frame',cv2.WINDOW_FREERATIO)
	cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	#(thresh,gray)=cv2.threshold(gray,150,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	gray = cv2.bitwise_not(gray)
	cv2.imshow('frame',gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
