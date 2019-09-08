import cv2
import numpy as np
image=cv2.imread('input.jpg')
print(image.shape) #for colored images, it would have 3 values; height, width and colorspace. In color images we have 3 colorspaces (RGB)
cv2.imshow('original', image)
cv2.waitKey()
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale', gray_image)
print(gray_image.shape) #for grayscale images we would have 2 values only; height and width. colorspace has no value for grayscale images
cv2.waitKey()
cv2.destroyALLWindows()

#output values
#(183, 275, 3) – for colored image
#(183, 275) – for grayscale image
