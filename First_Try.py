import os
from PIL import Image
import cv2
import numpy
from collections import Counter


# Program to find most frequent
# element in a list

def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num


path='C:/Users/Konstantinos/Desktop/pic.jpg'
#Open image
img = Image.open(path).convert("L")
imgarr = numpy.array(img)
print(imgarr[0][0])
#Picture is 940x1260. Each number in imgarr is a pixel
print("Columnns: ", len(imgarr[0]))
cols = len(imgarr[0])
print("Rows: ", len(imgarr))
rows = len(imgarr)

#Plan is to ask a number for how many pixels to combine ex. 20x20 pixelation
#Then find the prominent colour for each area and replace all the pixels of that area with that
#

area = 20
temparr=[[0]*area]*area
pixarr=[[0]*cols]*rows
#Each block
for line in range(0,rows-1,area): #for line=0;line<rows;line=line+area
    for column in range(0,cols-1,area):
        # print("line ",line," Column",column)
        #Set block in pixarr
        for i in range(line,area+line-1):                                         #i=area*line;i<area*(line+1);i++
            for j in range(column,area+column-1):
                #print("i ",i," j ",j)
                #print("x ",i-area*line," y ",j-area*column)
                temparr[i-line][j-column] = imgarr[i][j]
        dom = most_frequent(temparr)
        #print("Dom ",dom[0])
        for i in range(line,area+line-1):
            for j in range(column,area+column-1):
                pixarr[i][j] = dom[0]
                #print("pixar[",i,"][",j,"]=", pixarr[i][j])


img = Image.fromarray(pixarr, 'RGB')
img.save('my.png')
img.show()