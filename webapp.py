import streamlit as st
import cv2
from PIL import Image
import numpy as np
import pandas as pd
import io
from datetime import datetime
import warnings
from dataset_maker import collect_dataset
from face_dataset_trainer import train_faces
import face_dataset_trainer
warnings.filterwarnings("ignore")
#face detector
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#face recognizer
rec=cv2.face.LBPHFaceRecognizer_create()
#read trained parameters for LBPH model
rec.read("trainingData.yml")
def markAttendance(name):
    with open('Attendance.csv','r+') as f:

    	#read file line by line
        myDataList = f.readlines()
        nameList = []

        #iterate over each line
        for line in myDataList:

        	#split with comma
            entry = line.split(',')

            #after splitting extarct name for each line and append it to list of names
            nameList.append(entry[0])

        #if name not in nameList:
        	#grab current date and time
        now = datetime.now()

            #stringify date-time
        dtString = now.strftime('%H:%M:%S')

            #write a line in Attendance.csv file
        f.writelines(f'\n{name},{dtString}')






def detect_faces(our_image):
    img = np.array(our_image.convert('RGB'))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces in gray scale
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    print("Detetcting")
    name='Unknown'
    for (x, y, w, h) in faces:
        # To draw a rectangle in a face
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        #pass the gray image after cropping it so that only detected face can be passed
        id, uncertainty = rec.predict(gray[y:y + h, x:x + w])
        print(id, uncertainty)
	#experiment with theshold i.e. 50 here
        if (uncertainty< 60):
            if (id == 1):

                name = "First"
                cv2.putText(img, name, (x, y + h), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2.0, (0, 0, 255))
                markAttendance(name)
            elif(id == 2):
                name = "Second"
                cv2.putText(img, name, (x, y + h), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2.0, (0, 0, 255))
                markAttendance(name)
            elif(id == 3):
                name = "Third"
                cv2.putText(img, name, (x, y + h), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2.0, (0, 0, 255))
                markAttendance(name)

        else:
            cv2.putText(img, 'Unknown', (x, y + h), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2.0, (0, 0, 255))


    return img[y:y + h, x:x + w]
def main():
    """Face Recognition App"""

    st.title("Streamlit Tutorial")

    html_temp = """
    <body style="background-color:white;">
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Attendance With Face Recognition</h2>
    </div>
    <br>
    </body>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.set_option('deprecation.showfileUploaderEncoding', False)

    if st.button("Collect Data"):
        collect_dataset()
    if st.button("Train Faces"):
        train_faces()
    image_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
    if image_file is not None:
        our_image = Image.open(image_file)
        st.text("Original Image")
        st.sidebar.image(our_image,use_column_width=True)

    if st.button("Recognise"):
        result_img= detect_faces(our_image)
        st.sidebar.image(result_img,use_column_width=True, )

    if st.button("Show Attendance"):
        attendance = pd.read_csv("Attendance.csv")
        st.write(attendance)

    if st.button('Real Time'):
        cam = cv2.VideoCapture(0)
        count = 1
        #started infinite loop
        while(count < 3):
            #read from video and return success status and image
            success, img = cam.read()
            count = count + 1
            #cv2.imshow("FRAME",img)
        st.sidebar.image(img,use_column_width=True,caption= "Captured Image")
        image = detect_faces(Image.fromarray(img))
        st.sidebar.image(image, use_column_width=True, caption = "Cropped and Detected Image")
        #release camera object
        cam.release()
        cv2.destroyAllWindows()
        

if __name__ == '__main__':
    main()
