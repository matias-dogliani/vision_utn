import cv2 
import numpy as np 

#Variables globales de control 
drawing = False 
mode = True
ix, iy = -1, -1 

def euclidianT (angle,tx,ty):
    pass


def draw (event,x,y,flgas,param): 
    global ix, iy, drawing, mode 
    if event == cv2.EVENT_LBUTTONDOWN: 
        drawing = True 
        ix, iy = x,y 
    elif event == cv2.EVENT_MOUSEMOVE: 
        if drawing is True: 
            imgSwap[:] = img[:]  
            cv2.rectangle(imgSwap,(ix,iy), (x,y), (0,255,0),1) 
    elif event == cv2.EVENT_LBUTTONUP: 
        drawing = False 
        cv2.rectangle(imgSwap,(ix,iy), (x,y), (0,255,0),1) 

img =cv2.imread("./img/lena.jpeg")  
imgSwap =cv2.imread("./img/lena.jpeg")  
#imgSwap = img #Esto no seriviria porque apunta a lo mismo 
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
        cv2.imwrite("./img/imagen_dibujada.png",imgSwap) 
    elif k == ord('r'): 
        #imgSwap = img #Con esto pasa lo mismo, hago que apunte a lo mismo
        imgSwap[:] = img[:] 
    elif k == ord('e'): 
        euclidianT(1,2,2) 
cv2.destroyAllWindows() 
