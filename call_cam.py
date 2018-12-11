import cv2
import numpy as np
from PIL import Image, ImageChops
import os
global rval, frame
import itchat

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False

count_same = 0
has_same = False
count_diff = 0
has_diff = False

while rval:
    
    rval, now_frame = vc.read()

    cv2.imshow("preview", now_frame)    
    img1 = Image.fromarray(frame, 'RGB')
    img2 = Image.fromarray(now_frame, 'RGB')

    
    diff = ImageChops.difference(img1, img2)
    array = np.array(diff)
    out = np.where(array > 40)[0].size
    if(out == 0):
        #print("Same")
        count_same += 1
        if (count_diff < 25):
            count_diff = 0
    else:
        #print("Different")
        count_diff += 1
        count_same = 0

    if(count_diff >= 25 and (not has_diff)):
        #send_move_danger()
        has_diff = True
        cv2.imwrite("breaker.jpg", now_frame)
    if(count_same > 80 and count_diff >= 25):
        #send_move_save()
        os.remove("breaker.jpg")
        count_diff = 0
        count_same = 0
        has_diff = False
    
    frame = now_frame

    key = cv2.waitKey(20)
    if key == 27:
        rval = False
if(os.path.isfile("./breaker.jpg")):
    os.remove("breaker.jpg")
cv2.destroyWindow("preview")

