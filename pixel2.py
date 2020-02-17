import numpy as np
from PIL import Image

path='C:/Users/Konstantinos/Desktop/pic.jpg'
#Open image
img = Image.open(path).convert("L")
imgarr = np.array(img)

area=22
height=len(imgarr)-len(imgarr)%area
columns=height//area
width=len(imgarr[0])-len(imgarr[0])%area
rows=width//area
print("width ",width, " height ",height, " columns ", columns," rows ",rows)

#Add to 2d array. Each number is a pixel
data = np.zeros((height, width, 3), dtype=np.uint8)
temp =np.zeros((area,area,3),dtype=np.uint8)
#print(data[0][0][2])
#print(imgarr[0:(area+0)][0:(area+0)])
for i in range(0,columns):
    for j  in range(0,rows):
        #print("i ",i," j ",j)
        unique, counts = np.unique(imgarr[i:i+area][j:j+area], return_counts=True)
        if len(unique)==0 :
            continue
        result = np.where(np.asarray((unique, counts)).T == np.amax(np.asarray((unique, counts)).T))
        print("result[0] = ",result[0][0])
        temp[0:area][0:area]= result[0][0]
        print(temp[0:area][0:area])
print(data[0][0])
img = Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()