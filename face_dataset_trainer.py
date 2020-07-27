import cv2
import os
import numpy as np
from PIL import Image

def train_faces():
    print("start training")
    #face recognizer local binary
    recognizer=cv2.face.LBPHFaceRecognizer_create()
    path='dataset'
    def getImagesWithID(path):
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
        faces=[]
        IDs=[]

        for imagepath in imagePaths:
            faceImg=Image.open(imagepath).convert('L')
            faceNp=np.array(faceImg,'uint8')
            print(imagepath)
            ID=int(os.path.split(imagepath)[-1].split(".")[1])
            #dataset/User.1.3
            faces.append(faceNp)
            IDs.append(ID)
            cv2.imshow("Training",faceNp)
            cv2.waitKey(10)
        return np.array(IDs),faces

    #get images with their corresponding ids
    Ids,faces=getImagesWithID(path)
    #train recognizer
    recognizer.train(faces,Ids)
    #parameters learned by recognizer is stored in yml file
    recognizer.save('trainingData.yml')
    #destroy all windows
    cv2.destroyAllWindows()
    return
        
if __name__ == '__main__':
    train_faces()
