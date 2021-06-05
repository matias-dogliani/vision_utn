import cv2 
import numpy as np 

#Variables globales de control 
drawing = False 
ix, iy = -1, -1 
fx, fy = -1, -1 

def EuclideanTrans(img,angle,tx,ty): 
    (h,w) = img.shape[0], img.shape[1]
    #H  = np.float32([[np.cos(angle), np.sin(angle), tx], 
                  #-1*[np.sin(angle), np.cos(angle), ty]] )
    
    R = cv2.getRotationMatrix2D((w/2,h/2),angle,scale=1.0)
    H = np.float32([[R[0][0],R[0][1], tx], 
                    [R[1][0],R[1][1], ty]] )
    
    T = cv2.warpAffine(img,H,(w,h))
    return T

def draw (event,x,y,flags,param): 
    global ix, iy,fx,fy, drawing, mode 
    if event == cv2.EVENT_LBUTTONDOWN: 
        drawing = True 
        ix, iy = x,y 
    elif event == cv2.EVENT_MOUSEMOVE: 
        if drawing is True: 
            imgSwap[:] = img[:]  
            cv2.rectangle(imgSwap,(ix,iy), (x,y), (0,255,0),1) 
    elif event == cv2.EVENT_LBUTTONUP: 
        drawing = False
        fx,fy = x,y
        cv2.rectangle(imgSwap,(ix,iy), (x,y), (0,255,0),1) 

img =cv2.imread("./img/lena.jpeg")  
imgSwap =cv2.imread("./img/lena.jpeg")  
cv2.namedWindow("Ventana Imagen")
cv2.setMouseCallback("Ventana Imagen",draw) 

print(" Opciones :" , 
            "g : Guardar porción de imagen",
            "r : Limpiar la imagen", 
            "e : Transformar la seleccion ", 
            "q : salir " , sep = "\n" ) 
while(1):
    cv2.imshow("Ventana Imagen", imgSwap) 
    k = cv2.waitKey(1) 
    if k == ord('q'):  
        break 
    elif k == ord('g'): 
        cv2.imwrite("./img/imagen_seleccionada.png",img[iy:fy, ix:fx]) 
    elif k == ord('r'): 
        imgSwap[:] = img[:] 
    elif k == ord('e'):
        SelT = EuclideanTrans(img[ix:fx, iy:fy],10,20,20)
        cv2.imwrite("./img/sel_transformada.png",SelT) 
        
cv2.destroyAllWindows() 
