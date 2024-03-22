import os
import cv2

path = "Images/"

Images=[]


for file in os.listdir(path):
    name, ext = os.path.splitext(file)


    if est in ['.gif','.png',,'.jpg','.jpeg','.jfif']:
        file_name = path+"/"+files

        print(file_name)

        Images.append(file_name)
print(len(Images))
count = len(Images)

frame = cv2.imread(images[0])
height,width,channels = frame.shape
size = (width,height)
print(size)

out=cv2.videowriter('project.avi',cv2.videowriter_fourcc(*'DIVX'),0.8,size)


for i in range(count -1,0,-1):
    frame=cv2.imread(Images[i])
    out.write(frame)

out.release()
print("Done")