import cv2

resized=1
# img_path="1.jpg"
# img_path,resized="pic.png",0
# img_path="picture.jpg"
img_path="pic1.png"


face_cascade= cv2.CascadeClassifier("W:\python\openCV\haar_cascadeclassifire_fontface.xml")

img = cv2.imread(img_path)
gray_img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


face= face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=10)
for x,y,w,h in face:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
# print(face)

resized_img= cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

if resized == 0:
    cv2.imshow("Pic Window",img)
else:
    cv2.imshow("Pic Window",resized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
print("-"*15+"Execution Done"+"-"*15)