from tkinter import *
import random

# Variables globales
ANCHO_CANVAS = 420
ALTO_CANVAS = 350
RADIO_PELOTA = 50
VELOCIDAD_PELOTA = 3

# Función para mover la pelota
def mover_pelota():
    global direccion_x, direccion_y  # Declarar las variables como globales
    
    # Obtener las coordenadas actuales de la pelota
    x, y = c.coords(texto_id)

    # Calcular las nuevas coordenadas de la pelota
    nuevo_x = x + direccion_x * VELOCIDAD_PELOTA
    nuevo_y = y + direccion_y * VELOCIDAD_PELOTA

    # Verificar los límites del Canvas
    if nuevo_x + RADIO_PELOTA/2 > ANCHO_CANVAS:
        direccion_x = random.choice([-1])  # Cambiar la dirección en el eje x en una dirección aleatoria
    elif nuevo_x - RADIO_PELOTA/2 < 0:
        direccion_x = random.choice([1])

    if nuevo_y + RADIO_PELOTA/2 > ALTO_CANVAS:
        direccion_y = random.choice([-1])  # Cambiar la dirección en el eje y en una dirección aleatoria
    elif nuevo_y - RADIO_PELOTA/2 < 0:
        direccion_y = random.choice([1])
         

    # Mover la pelota a la nueva posición
    c.move(texto_id, direccion_x * VELOCIDAD_PELOTA, direccion_y * VELOCIDAD_PELOTA)

    ventana.after(10, mover_pelota)

# Crear la ventana principal
ventana = Tk()
ventana.config(bg="tan1")
ventana.title("Movimiento de Pelota")
ventana.geometry("440x430")

pelota=PhotoImage(file="img/pelota.png")
cancha=PhotoImage(file="img/cancha.png")

# Crear el Canvas
c = Canvas(ventana, width=ANCHO_CANVAS, height=ALTO_CANVAS, bg="gray15")
c.place(x=10,y=10)

x_inicial = ANCHO_CANVAS / 2
y_inicial = ALTO_CANVAS / 2

can=c.create_image(x_inicial,y_inicial,image=cancha)
texto_id = c.create_image(x_inicial, y_inicial, image=pelota)

# Definir la dirección inicial de la pelota
direccion_x = 1  
direccion_y = 1  

bt_subir = Button(ventana,bg="green", text="Jugar",activebackground="oliveDrab1",command=mover_pelota)
bt_subir.place(x=170, y=370, width=100, height=50)

ventana.mainloop()
