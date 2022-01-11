import cv2,time,numpy
camera_port= 0
video=cv2.VideoCapture(camera_port,cv2.CAP_DSHOW)
# face_cascade= cv2.CascadeClassifier("W:\python\openCV\haar_cascadeclassifire_fontface.xml")
face_cascade= cv2.CascadeClassifier("W:\python\openCV\haarcascade_smile.xml")
a=1

while True:
    a+=1
    check,frame= video.read()
    
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face= face_cascade.detectMultiScale(gray_frame,scaleFactor=1.05,minNeighbors=5)
    # print(face)
    
    for x,y,w,h in face:
        fframe = cv2.rectangle(frame,(x,y),(x+w,y+h),(100,100,0),2)
    if len(face)==0:
        frame=numpy.flip(frame,1)
        cv2.imshow("Capture- Q to Quit",frame)
    else:
        fframe=numpy.flip(fframe,1)
        cv2.imshow("Capture- Q to Quit",fframe)
    # print(frame)
    key= cv2.waitKey(1)
    # # if a== 50:
    # #     break
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

print("Total Frame Prossesing ", a)
print("-"*15+"Execution Done"+"-"*15)