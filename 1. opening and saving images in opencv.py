import cv2 #Import opencv in python by command
import numpy as np #importing numpy library
image=cv2.imread('input.jpg') #Load an image using ‘imread’ specifying the path to the image
cv2.imshow('hello_world', image) #To show the image we use imshow function, the first parameter is the title showed on top of image window
 #written as a string, while the second parameter is the readed image using imrread function
print(image.shape) #prints the size of image using three dimensional array provided by numpy
print('Height of image:',(image.shape[0],'pixels')) #the first block of array stores the height of the image in 'pixels'
print('Width of image:',(image.shape[1],'pixels'))  #the second block stores the height of image in 'pixels'
cv2.imwrite('output.jpg',image) #you can save the image using imwrite function by specifying 'filename.type' and the image you want to save
cv2.imwrite('output.png',image)
cv2.waitKey() #waitkey allows to input information when image is open, by leaving it blank it just waits for any key to be pressed to close it
cv2.destroyAllWindows() #'destroyAllWindows’ closes all the open windows, failure to place this will cause your programme to hang.
