import cv2
import streamlit as st
#video capture object with id =0
def collect_dataset():
    cam = cv2.VideoCapture(0)

    #downlaod xml file that has been trained to detect face in image
    face_detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


    #id of image
    image_id = int(input("Enter Image id (start id count with 1)"))
    image_id = str(st.number_input("Enter image id",value=5))   #this can some time create problem

    sampleNum=0
    if int(image_id) > 0:
        #started infinite loop
        while(True):

            #read from video and return success status and image
            success, img = cam.read()

            #convert image from rgb to gray
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            #detect face in gray scale image
            faces = face_detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

                #captured face  and then crop image and save in the dataset folder
                cv2.imwrite("dataset/User."+image_id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                sampleNum=sampleNum+1
                cv2.imshow('frame',img)
            # break if the sample number is morethan 20
            if sampleNum>20:
                break

        #release camera object
        cam.release()
        cv2.destroyAllWindows()
        return

if __name__ == '__main__':
    collect_dataset()
