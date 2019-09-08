import cv2
image=cv2.imread('input.jpg')
B,G,R=cv2.split(image) #opencv's split function splits the image into each color index
cv2.imshow("Red",R) #outputing red space of image
cv2.imshow("Green",G) #outputing green space of image
cv2.imshow("Blue",B) #outputing blue space of image
#making the original image by merging the individual color components
merged=cv2.merge([B,G,R]) #merging the three color spaces
cv2.imshow("merged",merged)
#amplifying the blue color
merged=cv2.merge([B+100,G,R]) #amplifying the blue component of image
cv2.imshow("merged with blue amplify",merged)
#representing the shape of individual color components.
# the output wuld be only two dimension whih wouldbe height and width, since third element of RGB component is individually represented
print(B.shape)
print(R.shape)
print(G.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()
