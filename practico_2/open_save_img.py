import cv2 

img = cv2.imread('./hoja.png') 
cv2.imshow('Imagen', img) 
k = cv2.waitKey(0) 

# Anda sin ord()
if k == 's': 
    print('Save img as gray') 
    cv2.imwrite('Leaf_gray.png',img) 
else: 
    print('Not save img') 

cv2.destroyAllWindows()

