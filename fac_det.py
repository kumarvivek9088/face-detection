import cv2
haar_file=cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade=cv2.CascadeClassifier(haar_file)
webcam=cv2.VideoCapture(0)
count=1
while count==1:
    i,im=webcam.read()
    faces=face_cascade.detectMultiScale(im,1.3,5)
    for (p,q,r,s) in faces:
        cv2.rectangle(im,(p,q),(p+r,q+s),(0,255,0),3)
    
    cv2.imshow("Face Detection",im)
    cv2.waitKey(10)
