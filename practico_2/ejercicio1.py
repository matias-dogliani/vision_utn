#from cv2 import imread, imwrite
import cv2 

imagen = cv2.imread("./hoja.png") 
UMBRAL = 240 
""" otro método es convertir la imagen a un solo canal en 
    escala de grises. 

    img_gris = imagen[:,:,0]+ imagen[:,:,1] + imagen[:,:,2] 
""" 

for i in range(imagen.shape[2]):      #3 Canales 
    for j in range(imagen.shape[1]): 
        for k in range(imagen.shape[0]): 
            if (imagen[k,j,i] < UMBRAL): 
                print( imagen[k,j,i])  
                imagen[k,j,i] =0;


cv2.imwrite("resultado.png", imagen) 
