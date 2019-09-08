import cv2
import numpy as np
image = cv2.imread('input.jpg')
B,G,R = cv2.split(image)
zeros=np.zeros(image.shape[:2],dtype="uint8") #shape[:2] would grab everything upto designated points i.e upto 2 position, height and width
cv2.imshow("RED",cv2.merge([zeros,zeros,R]))
cv2.imshow("Green",cv2.merge([zeros,G,zeros]))
cv2.imshow("Blue",cv2.merge([B,zeros,zeros]))
cv2.waitKey(0)
cv2.destroyAllWindows()
