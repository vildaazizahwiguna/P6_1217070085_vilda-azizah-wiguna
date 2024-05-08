import cv2

img = cv2.imread('kucing.jpg', 1)
cv2.imshow("original imgae", img)

#clahe (contrast limited adaptive histogram equalization)
clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8,8))

lab = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)
l, a, b = cv2.split(lab)
l2 = clahe.apply(l)

lab = cv2.merge((l2, a, b))
img2 = cv2.cvtColor(lab, cv2.COLOR_Lab2BGR)
cv2.imshow('hasil peningkatan kontras dengan clahe', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()