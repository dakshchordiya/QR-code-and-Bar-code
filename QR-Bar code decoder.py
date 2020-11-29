import cv2
import numpy as np
from pyzbar.pyzbar import decode


img = cv2.imread("1.jfif")
img = cv2.resize(img , (1000,800))

code =  decode(img)
print(code)

cv2.imshow("image" , img)
cv2.waitKey(0)