import cv2 
import numpy as np 

#Variables globales de control 
drawing = False 
ix, iy = -1, -1 
fx, fy = -1, -1 

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


def fixedSlice():                                                                     
    global ix,iy,fx,fy                                                          
                                                                                
    if fx < ix:                                                                 
        fx,ix = ix,fx                                                           
    if fy < iy:                                                                 
        fy,iy = iy,fy                                                           
                                                                                
    return img[iy:fy, ix:fx]



img =cv2.imread("./img/lena.jpeg")  
imgSwap =cv2.imread("./img/lena.jpeg")  
cv2.namedWindow("Ventana Imagen")
cv2.setMouseCallback("Ventana Imagen",draw) 

print(" Opciones :" , 
            "g : Guardar porción de imagen",
            "r : Limpiar la imagen", 
            "q : salir " , sep = "\n" ) 
while(1):
    cv2.imshow("Ventana Imagen", imgSwap) 
    k = cv2.waitKey(1) 
    if k == ord('q'):  
        break 
    elif k == ord('g'): 
        cv2.imwrite("./img/imagen_seleccionada.png",fixedSlice())        
    elif k == ord('r'): 
        imgSwap[:] = img[:] 
        
cv2.destroyAllWindows() 
