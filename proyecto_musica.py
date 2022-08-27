

from tkinter import*
from tkinter.ttk import Combobox
from tkinter import ttk


#funciones para flujo de ventanas

def popingles():
    ventana_pi.deiconify()
    ventana.iconify()

def popespañol():
    ventana_pe.deiconify()
    ventana.iconify()
    
def musicales():
    ventana_m.deiconify()
    ventana.iconify()

def rock():
    ventana_r.deiconify()
    ventana.iconify()

#regresar al inicio
    
def back_pi():
    ventana_pi.iconify()
    ventana.deiconify()

def back_pe():
    ventana_pe.iconify()
    ventana.deiconify()
    
def back_m():
    ventana_m.iconify()
    ventana.deiconify()

def back_r():
    ventana_r.iconify()
    ventana.deiconify()

#siguiente quiz

def sig_pi():
    ventana_pi.iconify()
    ventana_pe.deiconify()

def sig_pe():
    ventana_pe.iconify()
    ventana_m.deiconify()
    
def sig_m():
    ventana_m.iconify()
    ventana_r.deiconify()



###ventana principal
ventana=Tk()
ventana.title("Music Pop Quiz")
ventana.config(cursor="heart")
ventana.config(bd=15)
ventana.config(relief="raised")

cuadro=Frame(ventana, width=780, height=980)
cuadro.pack(fill='both', expand=1)

canvas= Canvas(cuadro, width=780, height=980)
canvas.pack(side='left', fill='both', expand=1)
canvas.config(bg="white")

cuadro.config(bg="deepskyblue")
cuadro.config(bd=20)



###ventana secundaria pop ingles


def mensaje_pi():
#contador puntaje
 respuesta1_pi=str(opciones1_pi.get())
 respuesta2_pi=str(opciones2_pi.get())
 respuesta3_pi=str(opciones3_pi.get())
 respuesta4_pi=str(opciones4_pi.get())
 respuesta5_pi=str(opciones5_pi.get())
 
 puntaje_pi=int(0)
 if respuesta1_pi=="Coldplay":
    puntaje_pi=puntaje_pi + 1
 else:
    puntaje_pi = puntaje_pi

 if respuesta2_pi=="Mercy":
    puntaje_pi=puntaje_pi + 1
 else:
    puntaje_pi=puntaje_pi

 if respuesta3_pi=="the way that it was":
   puntaje_pi=puntaje_pi + 1
 else:
   puntaje_pi=puntaje_pi
 
 if respuesta4_pi=="Olivia Rodrigo":
      puntaje_pi=puntaje_pi + 1
 else:
    puntaje_pi=puntaje_pi

 if respuesta5_pi=="Billie Eilish":
    puntaje_pi=puntaje_pi + 1
 else:
    puntaje_pi=puntaje_pi

 calificacion_pi=float(puntaje_pi/.5)
 nombre=str(respuesta_nombrepi.get())
 fin_pi.config(text=("Gracias " + nombre +" por conterstar, tu calificación es", calificacion_pi))

 
ventana_pi=Toplevel(ventana)
ventana_pi.title("Pop Ingles")
ventana_pi.config(bd=15)
ventana_pi.config(cursor="pencil")
ventana_pi.config(relief="raised")

cuadro_pi=Frame(ventana_pi, width=600, height=950)
cuadro_pi.pack(fill='both', expand=1)

canvas_pi=Canvas(cuadro_pi, width=600, height=950)
canvas_pi.pack(side='left', fill='both', expand=1)
canvas_pi.config(bg="white")

cuadro_pi.config(bg="aquamarine2")
cuadro_pi.config(bd=20)


intro_pi=Label(cuadro_pi, text = "Contesta las preguntas sobre pop")
intro_pi.config(bg="white", fg="aquamarine")
intro2_pi=Label(cuadro_pi, text = "Al finalizar dar click en el botón final para conocer tu resultado")
intro2_pi.config(bg="white", fg="aquamarine")
nombre_pi=Label(cuadro_pi, text="Ingresa tu nombre:")
nombre_pi.config(bg="aquamarine", fg="white")
respuesta_nombrepi=Entry(cuadro_pi)


#Uso de combobox para desplegar opciones de respuesta

pregunta1_pi=Label(cuadro_pi, text="¿Qué banda canta la canción “The Scientist”?")
pregunta1_pi.config(bg="aquamarine", fg="white")
pregunta2_pi=Label(cuadro_pi, text="¿Qué canción pertenece a Shawn Mendes”?")
pregunta2_pi.config(bg="aquamarine", fg="white")
pregunta3_pi= Label(cuadro_pi, text = "Completa la letra Go home, get ahead light speed")
pregunta3_pi.config(bg="aquamarine", fg="white")
pregunta3_pi2= Label(cuadro_pi, text = "internet I don’t want to talk about “_____“")
pregunta3_pi2.config(bg="aquamarine", fg="white")
pregunta4_pi=Label(cuadro_pi, text="¿Quién ganó el premio Grammy al mejor álbum de pop vocal en 2022?")
pregunta4_pi.config(bg="aquamarine", fg="white")
pregunta5_pi=Label(cuadro_pi, text="¿Qué artista canta la canción “Happier than ever”?")
pregunta5_pi.config(bg="aquamarine", fg="white")

fin_pi=Label(cuadro_pi, text = "")
fin_pi.config(bg="white", fg="aquamarine")
#Uso de combobox para desplegar opciones de respuesta
opciones1_pi=Combobox(cuadro_pi,values=["The Beatles", "Coldplay", "Queen", "Imagine Dragons"])
opciones2_pi=Combobox(cuadro_pi,values=["Rolling in the deep", "Stay", "Mercy", "Golden"])
opciones3_pi=Combobox(cuadro_pi,values=["the past", "last summer", "that", "the way that it was"])
opciones4_pi=Combobox(cuadro_pi,values=["Olivia Rodrigo", "Dua Lipa", "Doja Cat", "Billie Eilish"])
opciones5_pi=Combobox(cuadro_pi,values=["Demi Lovato", "Selena Gomez", "Katy Perry", "Billie Eilish"])

final_pi=Button(cuadro_pi,text="Finalizar", command=mensaje_pi)
final_pi.config(relief="raised")

##calificación


#Colocación dentro de la ventana pop ingles 
intro_pi.place(x=185, y=30)
intro2_pi.place(x=85, y=50)

nombre_pi.place(x=80, y=100, width=450, height=25)
respuesta_nombrepi.place(x=130, y=140, width=320, height=25)

pregunta1_pi.place(x=80, y=190, width=450, height=25)
opciones1_pi.place(x=130, y=230, width=320, height=25)

pregunta2_pi.place(x=80, y=280, width=450, height=25)
opciones2_pi.place(x=130, y=320, width=320, height=25)

pregunta3_pi.place(x=80, y=370, width=450, height=25)
pregunta3_pi2.place(x=80, y=395, width=450, height=25)
opciones3_pi.place(x=130, y=440, width=320, height=25)

pregunta4_pi.place(x=80, y=490, width=450, height=25)
opciones4_pi.place(x=130, y=530, width=320, height=25)

pregunta5_pi.place(x=80, y=580, width=450, height=25)
opciones5_pi.place(x=130, y=620, width=320, height=25)

fin_pi.place(x=170, y=660)
final_pi.place(x=185, y=700, width=210, height=25)

###ventana secundaria pop español

#contador puntaje
puntaje_pe=0

def mensaje_pe():

#contador puntaje
 respuesta1_pe=str(opciones1_pe.get())
 respuesta2_pe=str(opciones2_pe.get())
 respuesta3_pe=str(opciones3_pe.get())
 respuesta4_pe=str(opciones4_pe.get())
 respuesta5_pe=str(opciones5_pe.get())

 puntaje_pe=int(0)
 
 if respuesta1_pe=="Camila":
    puntaje_pe=puntaje_pe + 1
 else:
    puntaje_pe = puntaje_pe

 if respuesta2_pe=="Ex de verdad":
    puntaje_pe=puntaje_pe + 1
 else:
    puntaje_pe=puntaje_pe
    
 if respuesta3_pe=="¿con quién se queda el perro?":
   puntaje_pe=puntaje_pe + 1
 else:
   puntaje_pe=puntaje_pe
 
 if respuesta4_pe=="Shakira":
      puntaje_pe=puntaje_pe + 1
 else:
    puntaje_pe=puntaje_pe

 if respuesta5_pe=="Belanova":
    puntaje_pe=puntaje_pe + 1
 else:
    puntaje_pe=puntaje_pe

 calificacion_pe=float(puntaje_pe/.5)
 nombre=str(respuesta_nombrepe.get())
 fin_pe.config(text=("Gracias " + nombre +" por conterstar, tu calificación es", calificacion_pe))

ventana_pe=Toplevel(ventana)
ventana_pe.title("Pop Español")
ventana_pe.config(bd=15)
ventana_pe.config(cursor="mouse")
ventana_pe.config(relief="raised")

cuadro_pe=Frame(ventana_pe, width=600, height=950)
cuadro_pe.pack(fill='both', expand=1)

canvas_pe=Canvas(cuadro_pe, width=600, height=950)
canvas_pe.pack(side='left', fill='both', expand=1)
canvas_pe.config(bg="white")

cuadro_pe.config(bg="orange")
cuadro_pe.config(bd=20)

intro_pe=Label(cuadro_pe, text = "Contesta las preguntas sobre pop")
intro_pe.config(bg="white", fg="orange")
intro2_pe=Label(cuadro_pe, text = "Al finalizar dar click en el botón final para conocer tu resultado")
intro2_pe.config(bg="white", fg="orange")
nombre_pe=Label(cuadro_pe, text="Ingresa tu nombre:")
nombre_pe.config(bg="orange", fg="white")
respuesta_nombrepe=Entry(cuadro_pe)


#Uso de combobox para desplegar opciones de respuesta

pregunta1_pe=Label(cuadro_pe, text="¿Qué banda canta la canción “Alejate de Mi”?")
pregunta1_pe.config(bg="orange", fg="white")
pregunta2_pe=Label(cuadro_pe, text="¿Qué canción pertenece a Ha-ash”? ")
pregunta2_pe.config(bg="orange", fg="white")
pregunta3_pe= Label(cuadro_pe, text = "Completa la letra: Si tu te vas ")
pregunta3_pe.config(bg="orange", fg="white")
pregunta3_pe2= Label(cuadro_pe, text = "y yo me voy __________")
pregunta3_pe2.config(bg="orange", fg="white")
pregunta4_pe=Label(cuadro_pe, text="¿Quién ganó el premio Grammy al mejor álbum de pop latino en 2017 ?")
pregunta4_pe.config(bg="orange", fg="white")
pregunta5_pe=Label(cuadro_pe, text="¿Qué artista canta la canción “Por ti”?")
pregunta5_pe.config(bg="orange", fg="white")

fin_pe=Label(cuadro_pe, text = "")
fin_pe.config(bg="white", fg="orange")

#Uso de combobox para desplegar opciones de respuesta
opciones1_pe=Combobox(cuadro_pe,values=["Mana", "El Tri", "Camila", "Moderato"])
opciones2_pe=Combobox(cuadro_pe,values=["Ex de verdad", "Tu de que vas", "Perdón", "Espacio Sideral"])
opciones3_pe=Combobox(cuadro_pe,values=["que  vamos  a hacer", "es el fin", "a mi casa", "¿con quién se queda el perro?"])
opciones4_pe=Combobox(cuadro_pe,values=["Luis Miguel", "Shakira", "Bad Bunny", "Jesse & Joy"])
opciones5_pe=Combobox(cuadro_pe,values=["Yuridia", "Rio roma", "Belanova", "Timbiriche"])

final_pe=Button(cuadro_pe,text="Finalizar", command=mensaje_pe)
final_pe.config(relief="raised")

#Colocación dentro de la ventana pop ingles 
intro_pe.place(x=185, y=30)
intro2_pe.place(x=85, y=50)

nombre_pe.place(x=80, y=100, width=450, height=25)
respuesta_nombrepe.place(x=130, y=140, width=320, height=25)

pregunta1_pe.place(x=80, y=190, width=450, height=25)
opciones1_pe.place(x=130, y=230, width=320, height=25)

pregunta2_pe.place(x=80, y=280, width=450, height=25)
opciones2_pe.place(x=130, y=320, width=320, height=25)

pregunta3_pe.place(x=80, y=370, width=450, height=25)
pregunta3_pe2.place(x=80, y=395, width=450, height=25)
opciones3_pe.place(x=130, y=440, width=320, height=25)

pregunta4_pe.place(x=80, y=490, width=450, height=25)
opciones4_pe.place(x=130, y=530, width=320, height=25)

pregunta5_pe.place(x=80, y=580, width=450, height=25)
opciones5_pe.place(x=130, y=620, width=320, height=25)

fin_pe.place(x=170, y=660)
final_pe.place(x=185, y=700, width=210, height=25)


#ventana secundaria musicales
ventana_m=Toplevel(ventana)
ventana_m.title("Musicales")
ventana_m.config(bd=15)
ventana_m.config(cursor="star")
ventana_m.config(relief="raised")

cuadro_m=Frame(ventana_m, width=600, height=950)
cuadro_m.pack(fill='both', expand=1)

canvas_m=Canvas(cuadro_m, width=600, height=950)
canvas_m.pack(side='left', fill='both', expand=1)
canvas_m.config(bg="white")

cuadro_m.config(bg="hot pink")
cuadro_m.config(bd=20)

#ventana secundaria rock
ventana_r=Toplevel(ventana)
ventana_r.title("Rock")
ventana_r.config(bd=15)
ventana_r.config(cursor="pirate")
ventana_r.config(relief="raised")

cuadro_r=Frame(ventana_r, width=600, height=950)
cuadro_r.pack(fill='both', expand=1)

canvas_r=Canvas(cuadro_r, width=600, height=950)
canvas_r.pack(side='left', fill='both', expand=1)
canvas_r.config(bg="white")

cuadro_r.config(bg="darkviolet")
cuadro_r.config(bd=20)




ventana.mainloop()
