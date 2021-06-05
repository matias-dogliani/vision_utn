import cv2 


cam = cv2.VideoCapture()
fps = cam.get(cv2.CAP_PROP_FPS)

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

#Opcion 2
def get_fps(cam): 
    NUM_FPS = 100
    if cam.isOpened(): 
        to = time.time() 
        for i in range(0,NUM_FPS): 
            ret,frame = video.read() 
        tf = time.time() 
        s = tf-to 
    return NUM_FPS / s 

