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
def drticka(dama:int): #cislo damy urcuje riadok
   global sachovnica
   global count


   if dama==8:
     
        print(sachovnica)
        print('•••••••••••••')
        count+=1
        img = Image.new( 'RGB', (320,320), "black") # create a new black image
        pixels = img.load()
        sq= img.size[0]//8

        img1 = ImageDraw.Draw(img) 
        
  
        for m in range(0,img.size[0],sq):    # for every col:
          for n in range(0,img.size[1], sq):
            m,n = m//8*(img.size[0]//sq),n//8*(img.size[1]//sq)
            if ((m+n)/sq)%2 ==0:
              st_p = (m,n)
              en_p = (m+sq,n+sq)
              img1.rectangle([st_p,en_p], fill = 'white') 
        for moc in range(8):
          for po in range(8):
            if sachovnica[po][moc]==1:
              st_p = (po*sq,moc*sq)
              en_p = ((po+1)*sq,(moc+1)*sq)
              img1.ellipse([st_p,en_p], fill = 'turquoise') 
        if count == 92:
          img.save('dama'+str(count)+'.jpg')
           
   else:
       for i in range(8):
           if check(i,dama):    
               sachovnica[dama][i] = 1
               drticka(dama+1)
               sachovnica[dama][i]=0

drticka(0)



  
      


