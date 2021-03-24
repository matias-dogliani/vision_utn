import cv2 


""" Puedo importar con 1 solo canal o con 3 canales y 
pasarlo a pata a escalas de grises 

img_gris = imagen[:,:,0]+ imagen[:,:,1] + imagen[:,:,2]
""" 

imagen = cv2.imread("./hoja.png",0) 
img_orig = imagen


UMBRAL = 240 

cv2.namedWindow("Original")
cv2.imshow("Original",img_orig)


for i in range(imagen.shape[0]): 
    for j in range(imagen.shape[1]):
        if (imagen[i,j] < UMBRAL): 
            imagen[i,j]= 0 
        else: 
            imagen[i,j]= 255

cv2.namedWindow("Resultado")
cv2.imshow("Resultado",imagen)
cv2.waitKey() 
cv2.imwrite("resultado.png",imagen) 
