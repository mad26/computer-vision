import cv2
image=cv2.imread('input.jpg')
hsv_image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV) #converting color image to HSV format
cv2.imshow('HSV image',hsv_image)
cv2.imshow('Hue channel',hsv_image[:,:,0]) #outputing the hue channel of the image
cv2.imshow('saturation channel',hsv_image[:,:,1]) #outputing the saturation channel of the image
cv2.imshow('value channel',hsv_image[:,:,2]) #outputing the value channel of the image
cv2.waitKey()
cv2.destroyAllWindows()
