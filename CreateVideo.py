import os
import cv2

path='images/'
images=[]

for file in os.listdir(path):
    name,ext= os.path.splitext(file)
    if ext in ['.jif','.png','.jpg','.jpeg']:
        file_name=  path+'/'+file
        images.append(file_name)

count=len(images)

frame= cv2.imread(images[0])
height,width,layers=frame.shape
size=(width,height)

out=cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)
for i in range(0,count):
    frame=cv2.imread(images[i])
    out.write(frame)
out.release()    
