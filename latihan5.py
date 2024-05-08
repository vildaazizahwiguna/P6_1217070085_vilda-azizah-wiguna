import cv2
import numpy as np

# read gambar
img=cv2.imread('kucing.jpg',0)

# buat histogram Eqqualization menggunakan cv2
equ = cv2.equalizeHist(img)

# stacking image
res = np.hstack((img, equ))

# menampilkan gambar
cv2.imshow('kucing.jpg',res)

cv2.waitKey(0)
cv2.destroyAllWindows()