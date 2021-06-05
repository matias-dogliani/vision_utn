
import cv2 

#v2.CAP_PROP_FRAME_WIDTH   #3
#cv2.CAP_PROP_FRAME_HEIGH  #4 

cam = cv2.VideoCapture()
w_cam = int(cam.get(3)) 
h_cam = int(cam.get(4)) 

while(cam.isOpened()): 
    ret_, frame = cam.read() 

    if ret is True: 
        cv2.imshow("Video", frame) 
        if cv2.waitkey(1/fps) & OxFF == 'q'):
            break; 

    else: 
        break; 

cam.release() 
cv2.destroyAllWindows() 

