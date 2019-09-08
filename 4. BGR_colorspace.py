import cv2
import numpy as np
image = cv2.imread('input.jpg')
B,G,R=image[0,0] #reading B,G,R value for the firstset [0,0] pixel
print(B,G,R) #printing the values stored for BGR at [0,0]
print(image.shape) #printing the size of image
gray_img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #converting color image to grayscale image
print(gray_img.shape) #printing the size of gray scale image
#gray_image pixel value for 10,50 pixel
print(gray_img[10,50]) #printing the value of pixels of grayscale image stored at [10,50]
