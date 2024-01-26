#!/usr/bin/env python
# coding: utf-8

# In[5]:


from PIL import Image, ImageDraw,ImageFont
import random
import os

lbfilename = '/Users/mariacheb/Downloads/RND_PHOTO/labels.txt'
imgdir = '/Users/mariacheb/Downloads/RND_PHOTO/IMG'
backgrW = 2000
backgrH = 900
minImgSize = 100
imgtopaint =  15 # сколько картинок вывести на экран, в каталоге их может быть больше
fontH     = 10 # cколько пикселей оставить под подпись
kolonX    = 0
maxpicH  = 500
maxpicW  = 800

Mainfont = ImageFont.truetype('/Users/mariacheb/Downloads/RND_PHOTO/font.ttf', size=24)
def listLabels():
  filelb = False
  try: 
    listnames = list()               
    filelb = open(lbfilename,'r')    # открыть файл
    for item in filelb: 
      #print(item)  
      listnames.append(item.rstrip())  # прочитать строки файла, удалить перенос строки
    return listnames
  except  Exception as error:
        
    print("ошибка чтения из файла "+lbfilename)
    return list()
  finally:    
    if filelb:filelb.close()

def listPhotos():
   try:        
     #print(imgdir)   
     reslist = list()   
     listOfFile = os.listdir(imgdir)
     for name in listOfFile:
        if name.lower().endswith(('.png', '.jpg', '.jpeg')):
            reslist.append(name)
     #print(listOfFile)
     return reslist
   except  Exception as error:
      print("ошибка получения списка файлов в папке"+imgdir)
      return list()

# изменить случайным образом размер картинки, но в пределах  фона
def resimg(inpimg):
   picW,picH = inpimg.size
   if (picW/backgrW) > (picH/backgrH): # пляшем от ширины  иначе от высоты   
     newS = random.randint(minImgSize, maxpicW)
     perc = newS/picW
   else:
     newS = random.randint(minImgSize, maxpicH)   
     perc = newS/picH
   newW = int(picW*perc)
   newH = int(picH*perc)
   return inpimg.resize((newW-fontH,newH-fontH)) 

# найтина фоне координаты картинки но в пределах     
def findposimg(imgW,imgH):

  rndX = random.randint(kolonX, backgrW-imgW-kolonX)
  rndY = random.randint(fontH, backgrH-imgH-fontH)
  
  return rndX,rndY
  
def mainpproc():

  listlb = listLabels()
  listph = listPhotos()
  
  if (len(listph)==0 or len(listlb)==0):
     print('Список фото или подписей пустой!')
     exit
  minlen = min(len(listlb),len(listph),imgtopaint)
  random.shuffle(listlb)
  random.shuffle(listph)
  imbc = Image.new('RGB', (backgrW, backgrH), color = 'black' )#(219, 193, 27))
  draw = ImageDraw.Draw(imbc)  
  for i in range(0,minlen): # цикл по картинкам и подписям
     #print(listph[i] )
     currim = Image.open(imgdir+'/'+listph[i])
     newimg= resimg(currim)
     posX,posY = findposimg(newimg.size[0],newimg.size[1])
     imbc.paste(newimg, (posX,posY))
     draw.text((posX,posY+newimg.size[1]), listlb[i], font=Mainfont, fill='white') # вывести подпись картинки
     
  imbc.show()
   
mainpproc()
#print(os.getcwd())


# In[ ]:





# In[ ]:




