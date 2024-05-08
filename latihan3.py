import cv2
import numpy as np 

img = cv2.imread('kucing.jpg')

#mencoba 4 nilai gamma
for gamma in [0.1, 0.5, 1.2, 2.2]:
    #apply gamma correction
    gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8')
    #save gambar
    cv2.imwrite('gamma_transformed'+str(gamma)+'.jpg', gamma_corrected)
    