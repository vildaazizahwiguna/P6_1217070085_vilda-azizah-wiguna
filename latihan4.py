import cv2
import numpy as np 
import matplotlib.pyplot as plt

img = cv2.imread('kucing.jpg')
img = cv2.resize(img, (600,400))
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_img = cv2.convertScaleAbs(gray_img, alpha=1.10, beta=40)
cv2.imshow('original image', gray_img)

#fungsi ini akan mengembalikan nilai piksel mulai dari 0-255
def hist(image):
    h = np.zeros(shape=(256,1))
    s = image.shape
    for i in range(s[0]):
        for j in range(s[1]):
            k = image[i,j]
            h[k,0] = h[k,0] + 1
    return h
histg = hist(gray_img)
plt.plot(histg)
plt.show()

x = histg.reshape(1,256)
y = np.zeros((1,256))
s = gray_img.shape
for i in range(256):
    if x[0,i] == 0:
        y[0,i] = 0
    else:
        y[0,i] = i

#mengekstrasksi nilai piksel min dan maks dari y 
min_ = np.min(y[np.nonzero(y)])
max_ = np.max(y[np.nonzero(y)])

#mengekstraksi rumus normalisasi gambar/contrast strecthing
stretch = np.round(((255-0)/(max_-min_))*(y-min_))
stretch[stretch<0] = 0
stretch[stretch>255] = 255

#memodifikasi nilai piksel gambar abu-abu asli
for i in range(s[0]):
    for j in range(s[1]):
        k = gray_img[i,j]
        gray_img[i,j] = stretch[0,k]

#histogram gambar yang diregangkan
histg2 = hist(gray_img)
plt.plot(histg2)
plt.show()
cv2.imshow('stretched image: ', gray_img)
cv2.waitKey(0)