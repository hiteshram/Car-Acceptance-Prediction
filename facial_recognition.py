import cv2
import numpy as np
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


image_folder_path="dataset\\subjects\\"
subject_faces=[]
subject_labels=[]
num_of_subjects=40
num_of_image=8
dim=(200,200)
for i in range(1,num_of_subjects+1):
    for j in range(1,num_of_image+1):
        image_path=image_folder_path+"\\s"+str(i)+"\\"+str(j)+".pgm"
        image = cv2.imread(image_path)
        resized_image=cv2.resize(image,dim)
        grey_image = cv2.cvtColor(resized_image,cv2.COLOR_BGR2GRAY)
        subject_faces.append(grey_image)
        subject_labels.append(i)
        
face_recognizer_lbp = cv2.face.LBPHFaceRecognizer_create()
face_recognizer_lbp.train(subject_faces, np.array(subject_labels))
#face_recognizer_lbp.save("face_recognizer_lbp.xml")


face_recognizer_eigen = cv2.face.EigenFaceRecognizer_create()
face_recognizer_eigen.train(subject_faces,np.array(subject_labels))

face_recognizer_fisher = cv2.face.FisherFaceRecognizer_create()
face_recognizer_fisher.train(subject_faces,np.array(subject_labels))


#Testing part

y_pred_lbp=[]
y_pred_eigen=[]
y_pred_fisher=[]

y_test=[]

for i in range(1,num_of_subjects+1):
    for j in [9,10]:
        img=cv2.imread(image_folder_path+"s"+str(i)+"\\"+str(j)+".pgm")
        resize_img=cv2.resize(img,dim)
        grey_img = cv2.cvtColor(resize_img,cv2.COLOR_BGR2GRAY)
        
        label,confidence = face_recognizer_lbp.predict(grey_img)
        y_pred_lbp.append(label)
        
        label,confidence = face_recognizer_eigen.predict(grey_img)
        y_pred_eigen.append(label)
        
        label,confidence = face_recognizer_fisher.predict(grey_img)
        y_pred_fisher.append(label)
        
        y_test.append(i)
        #print("Subject :"+str(i)+" Label : "+str(label)+" Confidence : "+str(confidence))

acc_eigen=accuracy_score(y_pred_eigen,y_test)
acc_fisher=accuracy_score(y_pred_fisher,y_test)
acc_lbp=accuracy_score(y_pred_lbp,y_test)


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
methods = ['EigenFaces', 'FisherFaces','LBP']
accuracy = [acc_eigen,acc_fisher,acc_lbp]
ax.bar(methods,accuracy)
plt.show()