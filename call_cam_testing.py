'''
This File is for open the camera and safe the picture of someone break in the room
'''

import cv2     #cv2 is for readin the camera
import numpy as np     #for the matrix calculation to tell the different between two frame
from PIL import Image, ImageChops    #image processing
import os    # read and write file
global rval, breaker_frame     #try to avoid saving files, not finish yet
import itchat     # wechat things, not using here



if __name__ == '__main__':
    cv2.namedWindow("preview") #create the frame to debug
    vc = cv2.VideoCapture(0) #calling the camera, number means the camera name, 0 is defult || first web camera, 1 is the webcamera, and so on


    # open the first frame
    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False

    
    breaker_frame = None

    # create flags for checking break in or not 
    count_same = 0
    has_same = False
    count_diff = 0
    has_diff = False


    # start the camera
    while rval:
        # read the frame for now
        rval, now_frame = vc.read()

        # display the image
        cv2.imshow("preview", now_frame)
        # read two frame at this moment and next moment
        img1 = Image.fromarray(frame, 'RGB')
        img2 = Image.fromarray(now_frame, 'RGB')

        # campare the color difference between two different frame
        # output is still a picture
        diff = ImageChops.difference(img1, img2)
        # reform the diff value to become an array
        array = np.array(diff)
        # return a boolean value that if any value in this matrix are less then 40
        # the number 40 can be changes due to the camera frame difference
        out = np.where(array > 40)[0].size

        # checking this frame is differnt or not, adding valuable to different values
        if(out == 0):
            #print("Same") //debug use
            count_same += 1  
            if (count_diff < 25):
                count_diff = 0
        else:
            #print("Different") //debug use
            count_diff += 1
            count_same = 0



        # decideing should we save the picture to computer or not
        # save the picture when 25 consecutive frames are different and decide if the person left when 80 consecutive frames are the same
        if(count_diff >= 25 and (not has_diff)):
            #send_move_danger()
            has_diff = True
            breaker_frame = now_frame
            #cv2.imwrite("breaker.jpg", now_frame)
        if(count_same > 80 and count_diff >= 25):
            #send_move_save()
            #os.remove("breaker.jpg")
            breaker_frame = None
            count_diff = 0
            count_same = 0
            has_diff = False
        # update frame
        frame = now_frame
        # this is closing the program by Esc key on your keyboard(upper left)
        key = cv2.waitKey(20)
        if key == 27:
            rval = False

    # delete the picture and the window when the program is closing 
    if(os.path.isfile("./breaker.jpg")):
        os.remove("breaker.jpg")
    cv2.destroyWindow("preview")

