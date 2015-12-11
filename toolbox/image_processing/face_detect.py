""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np

kernel = np.ones((21,21),'uint8')
cap = cv2.VideoCapture(0)

while(True):
	face_cascade = cv2.CascadeClassifier('/home/jong/Desktop/softdes/SoftwareDesignFall15/toolbox/image_processing/haarcascade_frontalface_alt.xml')
	ret, frame = cap.read()
	faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
	for (x,y,w,h) in faces:
		frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255))
		cv2.circle(frame,(x+int(w/2),y+int(h/2)),int(h/2.5),(255,255,255),-1)
		cv2.circle(frame,(x+int(w/3)*2,y+int(h/3)),10,(0,0,0),-1)
		cv2.circle(frame,(x+int(w/3),y+int(h/3)),10,(0,0,0),-1)
		cv2.rectangle(frame,(x+int(w/3),y+int(h/3)*2),(x+int(w/3)*2,y+int(h/3)*2),(0,0,0),10)
	# Display the resulting frame
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
	    break

cap.release()
cv2.destroyAllWindows()