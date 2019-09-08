#greyscaling is the process by which an image is converted from a full color to shades of grey(black and white)
import cv2
import numpy as np
# load our input image
image=cv2.imread('input.jpg')
print(image.shape)
cv2.imshow('original', image)
cv2.waitKey()

#we use cvtcolor, to convert to greyscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale', gray_image)
print(gray_image.shape)
cv2.waitKey()
cv2.destroyALLWindows()

#simpler way to onvert image into grayscale is just add the argument 0 in imread function aside to the image name
#grey_image=cv2.imread('input.jpg',0)
#cv2.imshow('grayscale',grey_image)
#cv2.waitKey()
#cv2.destroyAllWindows()
