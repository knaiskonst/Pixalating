from PIL import Image
import numpy as np
from scipy import stats

def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num

path='C:/Users/Konstantinos/Desktop/pic.png'
img = Image.open(path)
#Creates flat array [height*width][R,G,B]
pixels = list(img.getdata())
imgarr = np.array(img)

area=2
height=len(imgarr)
print(height)
columns=height//area
width=len(imgarr[0])
print(width)
rows=width//area

data = np.zeros((height, width, 3), dtype=np.uint8)

data = np.reshape(pixels,(height,width,3))
print(pixels[0])
print(data[0:2][0:1][0])

m = stats.mode(data[0:area][0:area][0])
print(m)
