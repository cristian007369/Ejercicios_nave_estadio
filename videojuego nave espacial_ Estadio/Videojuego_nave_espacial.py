from tkinter import *
import random
global y,x,nave1
y=150
x=250
nave1=0
BASE=500
ALTURA=300
nave_moviendose = False 
def crear_meteoritos():
    c.delete("circulo") 
    for i in range(30):
        x=random.randint(0,BASE-20)
        y=random.randint(0,ALTURA-20)
        z=random.randint(1,20)
        color="#"
        for caracter in range(6):
            color+=random.choice("0123456789ABCDEF")
        circulo=c.create_oval(x,y,x+z,y+z, fill=color,tags="circulo")
def detener_movimiento(event):
    global nave_moviendose
    nave_moviendose = False
def mover_nave():
    global y, nave1, nave_moviendose
    if nave_moviendose:  
        y -= 7  
        if nave1:  
            c.delete(nave1)
        if y<0:
            y=ALTURA
            nave1=c.create_image(x,ALTURA,image=nave)
        else:
            nave1=c.create_image(x,y,image=nave)
        crear_meteoritos()  
        ventana_principal.after(100, mover_nave)
def iniciar_movimiento(event):
    global nave_moviendose
    if not nave_moviendose:  
        nave_moviendose = True
        mover_nave() 
def mover_nave2():
    global y, nave1, nave_moviendose
    if nave_moviendose:  
        y += 7  
        if nave1:  
            c.delete(nave1)
        if y > ALTURA:
            y=0
            nave1=c.create_image(x,y,image=nave)
        else:
            nave1=c.create_image(x,y,image=nave)
        crear_meteoritos()   
        ventana_principal.after(100, mover_nave2)
def iniciar_movimiento2(event):
    global nave_moviendose
    if not nave_moviendose:  
        nave_moviendose = True
        mover_nave2() 
def mover_nave3():
    global x, nave1, nave_moviendose
    if nave_moviendose:  
        x -= 7  
        if nave1:  
            c.delete(nave1)
        if x<0:
            x=BASE
            nave1=c.create_image(x,y,image=nave)
        else:
            nave1=c.create_image(x,y,image=nave)  
        crear_meteoritos() 
        ventana_principal.after(100, mover_nave3)
def iniciar_movimiento3(event):
    global nave_moviendose
    if not nave_moviendose:  
        nave_moviendose = True
        mover_nave3()  
def mover_nave4():
    global x, nave1, nave_moviendose
    if nave_moviendose:  
        x += 7  
        if nave1:  
            c.delete(nave1)
        if x > BASE:
            x=0
            nave1=c.create_image(x,y,image=nave)
        else:
            nave1=c.create_image(x,y,image=nave)  
        crear_meteoritos() 
        ventana_principal.after(100, mover_nave4)
def iniciar_movimiento4(event):
    global nave_moviendose
    if not nave_moviendose:  
        nave_moviendose = True
        mover_nave4() 
def star():
    global nave1, x ,y,fon1
    if nave1!=0:
        c.delete(nave1)
        c.delete(fon1)
    x=250
    y=150
    fon1=c.create_image(x,y, image=fondo)
    nave1=c.create_image(x,y,image=nave)
    crear_meteoritos()


ventana_principal = Tk()
ventana_principal.title("Videojuego nave espacial")
ventana_principal.geometry("875x400")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="black")

arriba=PhotoImage(file="img/arriba.png")
abajo=PhotoImage(file="img/abajo.png")
derecha=PhotoImage(file="img/derecha.png")
izquierda=PhotoImage(file="img/izquierda.png")
fondo=PhotoImage(file="img/fon11.png")
star1=PhotoImage(file="img/star.png")
nave=PhotoImage(file="img/nave .png")
fondo33=PhotoImage(file="img/fondo_planeta1.png")

label_imagen = Label(ventana_principal,bg="black", image=fondo33)
label_imagen.pack()

c= Canvas(ventana_principal, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=125,y=30)

#Botones arriba abajo izquierda derecha
bt_subir = Button(ventana_principal,bg="black", image=arriba,activebackground="black")
bt_subir.place(x=725, y=105, width=50, height=50)
bt_subir.bind("<ButtonPress>", iniciar_movimiento)
bt_subir.bind("<ButtonRelease>", detener_movimiento)

bt_izquierda = Button(ventana_principal,bg="black", image=izquierda,activebackground="black")
bt_izquierda.place(x=675, y=155, width=50, height=50)
bt_izquierda.bind("<ButtonPress>", iniciar_movimiento3)
bt_izquierda.bind("<ButtonRelease>", detener_movimiento)

bt_derecha = Button(ventana_principal,bg="black", image=derecha,activebackground="black")
bt_derecha.place(x=775, y=155, width=50, height=50)
bt_derecha.bind("<ButtonPress>", iniciar_movimiento4)
bt_derecha.bind("<ButtonRelease>", detener_movimiento)

bt_bajar = Button(ventana_principal,bg="black", image=abajo,activebackground="black")
bt_bajar.place(x=725, y=205, width=50, height=50)
bt_bajar.bind("<ButtonPress>", iniciar_movimiento2)
bt_bajar.bind("<ButtonRelease>", detener_movimiento)

bt_star = Button(ventana_principal,bg="black", image=star1,  command=star)
bt_star.place(x=350, y=343, width=50, height=50)

ventana_principal.mainloop()