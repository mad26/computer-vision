import cv2
import numpy as np
import matplotlib.pyplot as plt #we need to import matplotlib to create histogram plots
image=cv2.imread('input.jpg')
histogram=cv2.calcHist([image],[0],None,[256],[0,256])
plt.hist(image.ravel(),256,[0,256]) #we plot a histogram, ravel() flatens our image array
plt.show()
color=('b','g','r') #viewing seperate color channels
for i, col in enumerate (color):  #we know seperate the color and plot each in histogram
    histogram2=cv2.calcHist([image],[i],None,[256],[0,256])
    plt.plot(histogram2,color=col)
    plt.xlim([0,256])
    plt.show()   
