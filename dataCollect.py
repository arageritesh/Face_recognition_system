# import cv2
# import os
# video = cv2.VideoCapture(0)

# # facedetect = cv2.CascadeClassifier('')

# # count=0

# # nameID = str(input("Enter your name: ")).lower()

# # path = 'images/' + nameID

# # isExist = os.path.exists(path)

# # if isExist:
# #     print("Name already Exists")
# #     nameID=str(input("Enter your name again: "))
# # else:
# #     os.makedirs(path)

# while True:
#     ret,frame = video.read()
#     # faces = facedetect.detectMultiScale(frame,1.3,5)
#     # for x,y,w,h in faces:
#     #     count=count+1
#     #     name='./images/'+nameID+str(count)+'.jpg'
#     #     print("creating Images........."+name)
#     #     cv2.imwrite(name,frame[y:y+h,x:x+w])
#     #     cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
#     cv2.imshow("WindowFrame",frame)
#     k=cv2.waitKey(0)
#     if k==ord('q'):
#         break
#     video.release()
#     cv2.destroyAllWindows()

#############################################################################################################

# import cv2
# import os

# video = cv2.VideoCapture(0)

# # facedetect = cv2.CascadeClassifier('')

# # count=0

# # nameID = str(input("Enter your name: ")).lower()

# # path = 'images/' + nameID

# # isExist = os.path.exists(path)

# # if isExist:
# #     print("Name already Exists")
# #     nameID=str(input("Enter your name again: "))
# # else:
# #     os.makedirs(path)

# while True:
#     ret, frame = video.read()
#     if not ret:
#         print("Error: Failed to capture frame.")
#         break

#     # faces = facedetect.detectMultiScale(frame,1.3,5)
#     # for x,y,w,h in faces:
#     #     count=count+1
#     #     name='./images/'+nameID+str(count)+'.jpg'
#     #     print("creating Images........."+name)
#     #     cv2.imwrite(name,frame[y:y+h,x:x+w])
#     #     cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    
#     cv2.imshow("WindowFrame", frame)
    
#     k = cv2.waitKey(1)  # Change waitKey argument to 1 to update frames continuously
#     if k == ord('q'):
#         break

# video.release()
# cv2.destroyAllWindows()

###########################################################################################################

# import cv2
# import os

# video = cv2.VideoCapture(0)

# facedetect = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')

# count=0

# nameID = str(input("Enter your name: ")).lower()

# path = 'images/' + nameID

# isExist = os.path.exists(path)

# if isExist:
#     print("Name already Exists")
#     nameID=str(input("Enter your name again: "))
# else:
#     os.makedirs(path)

# while True:
#     ret, frame = video.read()
#     if not ret:
#         print("Error: Failed to capture frame.")
#         break

#     faces = facedetect.detectMultiScale(frame,1.3,5)
#     for x,y,w,h in faces:
#         count=count+1
#         name='./images/'+nameID+str(count)+'.jpg'
#         print("creating Images........."+name)
#         cv2.imwrite(name,frame[y:y+h,x:x+w])
#         cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    
#     cv2.imshow("WindowFrame", frame)
    
#     cv2.waitKey(1)  # Change waitKey argument to 1 to update frames continuously
#     if count>500:   # Check if 'q' key is pressed
#         break

# # Release video capture and close windows after exiting the loop
# video.release()
# cv2.destroyAllWindows()

import cv2
import os

video = cv2.VideoCapture(0)

# Specify the correct path to the Haar Cascade XML file
cascade_path = 'haarcascade_frontalface_default.xml'
facedetect = cv2.CascadeClassifier(cascade_path)

count = 0

nameID = str(input("Enter your name: ")).lower()

path = 'images/' + nameID

isExist = os.path.exists(path)

if isExist:
    print("Name already exists")
    nameID = str(input("Enter your name again: "))
    path = 'images/' + nameID
else:
    os.makedirs(path)
    print(f"Directory created at: {path}")

while True:
    ret, frame = video.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    faces = facedetect.detectMultiScale(frame, 1.3, 5)
    for x, y, w, h in faces:
        count += 1
        name = os.path.join(path, nameID + str(count) + '.jpg')
        print("Creating Image: " + name)
        cv2.imwrite(name, frame[y:y+h, x:x+w])
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
    
    cv2.imshow("WindowFrame", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q') or count > 500:  # Check if 'q' key is pressed or count > 500
        break

# Release video capture and close windows after exiting the loop
video.release()
cv2.destroyAllWindows()

