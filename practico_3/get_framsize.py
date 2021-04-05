
import cv2 


cam = cv2.VideoCapture()
h_cam = int(cam.get(3)) 
w_cam = int(cam.get(4)) 

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

