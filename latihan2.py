import cv2
import numpy as np 
import matplotlib.pyplot as plt

image = cv2.imread('kucing.jpg')

#log transformation
c = 255 / np.log(1 + np.max(image))
log_image = c * (np.log(image + 1))

log_image = np.array(log_image, dtype = np.uint8)

#display
plt.imshow(image)
plt.show()
plt.imshow(log_image)
plt.show()