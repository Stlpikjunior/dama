from PIL import Image,ImageDraw




sachovnica= []
for i in range(8):
   riadok = []
   for j in range(8):
       riadok.append(0)
   sachovnica.append(riadok)

   
def check(x:int,y:int) ->bool:#najpr sachovnica[y][x]
   for j in range(8):
       for i in range(8):
           if i ==x or j==y or j+i ==x+y or i-j ==x-y:
               if sachovnica[j][i] ==1:
                   return False
   return True
count = 0
def drticka(dama:int,imag): #cislo damy urcuje riaadok
   global sachovnica
   global count
   global img
   imag = img
   img2 = ImageDraw.Draw(imag)
   sq = imag.size[0]//8
   if dama==8:
     
       print(sachovnica)
       print('•••••••••••••')
       count+=1
      
       for moc in range(8):
         for po in range(8):
           if sachovnica[po][moc]==1:
             st_p = (po*sq,moc*sq)
             en_p = ((po+1)*sq,(moc+1)*sq)
             img2.ellipse([st_p,en_p], fill = 'turquoise') 
           
   else:
       for i in range(8):
           if check(i,dama):    
               sachovnica[dama][i] = 1
               drticka(dama+1,img)
               sachovnica[dama][i]=0

        

for i in range(1,4):
  img = Image.new( 'RGB', (320,320), "black") # create a new black image
  pixels = img.load()
  sq_x = img.size[0]//8
  sq_y = img.size[1]//8

  img1 = ImageDraw.Draw(img) 
  
  for m in range(0,img.size[0],sq_x):    # for every col:
    for n in range(0,img.size[1], sq_y):
       m,n = m//8*(img.size[0]//sq_x),n//8*(img.size[1]//sq_y)
       if ((m+n)/sq_x)%2 ==0:
         st_p = (m,n)
         en_p = (m+sq_x,n+sq_y)
         img1.rectangle([st_p,en_p], fill = 'white') 
  drticka(0,img)

  
      

  img.show()
  img.save('kus'+str(i)+'.jpg')