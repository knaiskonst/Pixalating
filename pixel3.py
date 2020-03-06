from PIL import Image
path='C:/Users/Konstantinos/Desktop/pic.png'
input = Image.open(path)

#Image size
width,height =input.size
#Pixelation Size
w,h=(128,128)
#resize input to pixelated size
temp = input.resize((w,h), resample=Image.BILINEAR)
#Generate Output
output=temp.resize((width,height) , resample = Image.NEAREST)

output.save('C:/Users/Konstantinos/Desktop/pix.png')
