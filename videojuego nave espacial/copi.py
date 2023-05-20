def subir_nave():
    global y, nave1
    y-=5
    c.delete(nave1)
    if y<0:
        y=ALTURA
        nave1=c.create_image(x,ALTURA,image=nave)
    else:
        nave1=c.create_image(x,y,image=nave)
def bajar_nave():
    global y, nave1
    y+=5
    c.delete(nave1)
    if y > ALTURA:
        y=0
        nave1=c.create_image(x,y,image=nave)
    else:
        nave1=c.create_image(x,y,image=nave)
def derecha_nave():
    global x, nave1
    x+=5
    c.delete(nave1)
    if x > BASE:
        x=0
        nave1=c.create_image(x,y,image=nave)
    else:
        nave1=c.create_image(x,y,image=nave)
def izquierda_nave():