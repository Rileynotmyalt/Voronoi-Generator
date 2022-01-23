from PIL import Image
import numpy as np
import math

#? JFL
# https://en.wikipedia.org/wiki/Jump_flooding_algorithm
#? Fortune's
# https://en.wikipedia.org/wiki/Fortune%27s_algorithm
# https://github.com/jansonh/Voronoi/blob/master/Voronoi.py
# https://www.cs.hmc.edu/~mbrubeck/voronoi.html
#?

distances=[]
colors=[]

def rcol():
  r = np.random.randint(0,255)
  g = np.random.randint(0,255)
  b = np.random.randint(0,255)
  a = 255
  return r,g,b,a

try:
  n=int(input('pieces: '))
except ValueError:
  n=3

im=Image.new("RGBA",(500,500))
pix=im.load()

xList=np.random.randint(0,im.width,n)
yList=np.random.randint(0,im.height,n)

for i in range(len(xList)):
  print(i,xList[i],yList[i])
  pix[xList[i],yList[i]]=(255,255,255,255)
  try:
    pix[xList[i]-1,yList[i]]=(255,255,255,255)
  except:
    pass
  try:
    pix[xList[i]+1,yList[i]]=(255,255,255,255)
  except:
    pass
  try:
    pix[xList[i],yList[i]-1]=(255,255,255,255)
  except:
    pass
  try:
    pix[xList[i],yList[i]+1]=(255,255,255,255)
  except:
    pass
  colors.append(rcol())

dots=im
dots.save('Dots.png')
print()
print('Calculating Voronoid')
for height in range(im.height):
  for width in range(im.width):
    dist=(xList-width)**2+(yList-height)**2
    pix[width,height]=colors[np.argmin(dist)]

print('saving')

im.save('Image.png')
print('Done')

nums=np.random.randint(0,100,22)