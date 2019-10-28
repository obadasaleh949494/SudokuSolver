from PIL import Image, ImageDraw,ImageFont
def BuildImage (string):
    if len(string) <81 :
        print('the numbers less than 81 numbers')
        return 
    img = Image.new('RGB', (550, 550), color = (255, 255, 255))
         
    d = ImageDraw.Draw(img)
    counter1=61
    counter2=1
    c1=1
    c2=61
    xx=0
    f = ImageFont.truetype("arial.ttf", 20)
    for xx in range(9):
        c1=1
        for yy in range (549):      
            if xx== 5 or xx==2:
                d.text((c1,c2-1), "_", fill=(0,0,0))
                d.text((c1,c2-2), "_", fill=(0,0,0))
            d.text((c1,c2), "_", fill=(0,0,0))
            c1=c1+1
            yy=yy+1
        c2=c2+61
        xx=xx+1
    for x in range(9):
        counter2=1
        for y in range (549):
            if x== 5 or x==2:
                d.text((counter1-1,counter2), "|", fill=(0,0,0))
                d.text((counter1-2,counter2), "|", fill=(0,0,0))

            d.text((counter1,counter2), "|", fill=(0,0,0))
            counter2=counter2+1
            y=y+1
        counter1=counter1+61
        x=x+1
    w=30
    h=30
    i=0
 

    img.save('tt.png')
str='123456789123456789123456789123456789123456789123456789123456789123456789123456789'
BuildImage(str)
