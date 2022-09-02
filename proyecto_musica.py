from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
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

def sig_r():
    ventana_r.iconify()
    ventana_pi.deiconify()
    
#Colocación dentro de la ventanas
def colocacion():


    intro.place(x=185, y=30)
    intro2.place(x=85, y=50)

    nombre.place(x=80, y=100, width=450, height=25)
    respuesta_nombre.place(x=130, y=140, width=320, height=25)

    pregunta1.place(x=80, y=190, width=450, height=25)


    pregunta2.place(x=80, y=280, width=450, height=25)


    pregunta3.place(x=80, y=370, width=450, height=25)
    pregunta3_2.place(x=80, y=395, width=450, height=25)


    pregunta4.place(x=80, y=490, width=450, height=25)
    pregunta5.place(x=80, y=580, width=450, height=25)

    final.place(x=195, y=700, width=210, height=25)
    
    regresar_inicio.place(x=20, y=700, width=140, height=25)

    siguiente_nivel.place(x=445, y=700, width=140, height=25)

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

 if respuesta2_pi=="Mercy":
    puntaje_pi=puntaje_pi + 1

 if respuesta3_pi=="the way that it was":
    puntaje_pi=puntaje_pi + 1
 
 if respuesta4_pi=="Olivia Rodrigo":
    puntaje_pi=puntaje_pi + 1
 
 if respuesta5_pi=="Billie Eilish":
    puntaje_pi=puntaje_pi + 1

 cal_pi=puntaje_pi/.5
 nombre=str(respuesta_nombre.get())
 print(messagebox.askretrycancel(message=("Gracias " + nombre +" por conterstar, tu calificación es", cal_pi), title="Calificación"))


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

 if respuesta2_pe=="Ex de verdad":
    puntaje_pe=puntaje_pe + 1

 if respuesta3_pe=="¿con quién se queda el perro?":
   puntaje_pe=puntaje_pe + 1
 
 if respuesta4_pe=="Shakira":
      puntaje_pe=puntaje_pe + 1

 if respuesta5_pe=="Belanova":
    puntaje_pe=puntaje_pe + 1

 cal_pe=puntaje_pe/.5
 nombre=str(respuesta_nombre.get())
 print(messagebox.askretrycancel(message=("Gracias " + nombre +" por conterstar, tu calificación es", cal_pe), title="Calificación"))

 
def mensaje_m():
#contador puntaje
 respuesta1_m=str(opciones1_m.get())
 respuesta2_m=str(opciones2_m.get())
 respuesta3_m=str(opciones3_m.get())
 respuesta4_m=str(opciones4_m.get())
 respuesta5_m=str(opciones5_m.get())


 puntaje_m=int(0)
 if respuesta1_m=="Dear Evan Hansen":
    puntaje_m=puntaje_m + 1

 if respuesta2_m=="Michael in the bathroom":
    puntaje_m=puntaje_m + 1

 if respuesta3_m=="Heather":
   puntaje_m=puntaje_m + 1
 
 if respuesta4_m=="George Washington":
      puntaje_m=puntaje_m + 1
 
 if respuesta5_m=="In the Heights":
    puntaje_m=puntaje_m + 1

 cal_m=puntaje_m/.5
 nombre=str(respuesta_nombre.get())
 print(messagebox.askretrycancel(message=("Gracias " + nombre +" por conterstar, tu calificación es", cal_m), title="Calificación"))

def mensaje_r():
#contador puntaje
 respuesta1_r=str(opciones1_r.get())
 respuesta2_r=str(opciones2_r.get())
 respuesta3_r=str(opciones3_r.get())
 respuesta4_r=str(opciones4_r.get())
 respuesta5_r=str(opciones5_r.get())


 puntaje_r=int(0)
 if respuesta1_r=="Queen":
    puntaje_r=puntaje_r + 1

 if respuesta2_r=="Dream On":
    puntaje_r=puntaje_r + 1

 if respuesta3_r=="fantasy":
   puntaje_r=puntaje_r + 1
 
 if respuesta4_r=="Radiohead":
      puntaje_r=puntaje_r + 1
 
 if respuesta5_r=="Led Zeppelin":
    puntaje_r=puntaje_r + 1

 cal_r=puntaje_r/.5
 nombre=str(respuesta_nombre.get())
 print(messagebox.askretrycancel(message=("Gracias " + nombre +" por conterstar, tu calificación es", cal_r), title="Calificación"))
    
        

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

cuadro.config(bg="lightgrey")
cuadro.config(bd=20)

pop_ingles=Button(cuadro, text="Pop Ingles", fg="aquamarine", font=("Roboto Cn",34),command=popingles)

pop_español=Button(cuadro, text="Pop Español", fg="orange", font=("Roboto Cn",34),command=popespañol)

musical=Button(cuadro, text="Musicales",fg="hot pink", font=("Roboto Cn",34),command=musicales)

rock=Button(cuadro, text="Pop Español",fg="darkviolet", font=("Roboto Cn",34),command=rock)

pop_ingles.place(x=180, y=190, width=450, height=60)

pop_español.place(x=180, y=310, width=450, height=60)

musical.place(x=180, y=430, width=450, height=60)

rock.place(x=180, y=560, width=450, height=60)
                




###ventana secundaria pop ingles
 
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


intro=Label(cuadro_pi, text = "Contesta las preguntas sobre pop")
intro.config(bg="white", fg="aquamarine")
intro2=Label(cuadro_pi, text = "Al finalizar dar click en el botón final para conocer tu resultado")
intro2.config(bg="white", fg="aquamarine")
nombre=Label(cuadro_pi, text="Ingresa tu nombre:")
nombre.config(bg="aquamarine", fg="white")
respuesta_nombre=Entry(cuadro_pi)


#Uso de label para mostrar preguntas

pregunta1=Label(cuadro_pi, text="¿Qué banda canta la canción “The Scientist”?")
pregunta1.config(bg="aquamarine", fg="white")
pregunta2=Label(cuadro_pi, text="¿Qué canción pertenece a Shawn Mendes”?")
pregunta2.config(bg="aquamarine", fg="white")
pregunta3= Label(cuadro_pi, text = "Completa la letra Go home, get ahead light speed")
pregunta3.config(bg="aquamarine", fg="white")
pregunta3_2= Label(cuadro_pi, text = "internet I don’t want to talk about “_____“")
pregunta3_2.config(bg="aquamarine", fg="white")
pregunta4=Label(cuadro_pi, text="¿Quién ganó el premio Grammy al mejor álbum de pop vocal en 2022?")
pregunta4.config(bg="aquamarine", fg="white")
pregunta5=Label(cuadro_pi, text="¿Qué artista canta la canción “Happier than ever”?")
pregunta5.config(bg="aquamarine", fg="white")


#Uso de combobox para desplegar opciones de respuesta
opciones1_pi=Combobox(cuadro_pi,state="readonly",values=["The Beatles", "Coldplay", "Queen", "Imagine Dragons"])
opciones2_pi=Combobox(cuadro_pi,state="readonly",values=["Rolling in the deep", "Stay", "Mercy", "Golden"])
opciones3_pi=Combobox(cuadro_pi,state="readonly",values=["the past", "last summer", "that", "the way that it was"])
opciones4_pi=Combobox(cuadro_pi,state="readonly",values=["Olivia Rodrigo", "Dua Lipa", "Doja Cat", "Billie Eilish"])
opciones5_pi=Combobox(cuadro_pi,state="readonly",values=["Demi Lovato", "Selena Gomez", "Katy Perry", "Billie Eilish"])

opciones1_pi.place(x=130, y=230, width=320, height=25)
opciones2_pi.place(x=130, y=320, width=320, height=25)
opciones3_pi.place(x=130, y=440, width=320, height=25)
opciones4_pi.place(x=130, y=530, width=320, height=25)
opciones5_pi.place(x=130, y=620, width=320, height=25)

final=Button(cuadro_pi,text="Finalizar", command=mensaje_pi)
final.config(relief="raised")

regresar_inicio=Button(cuadro_pi,text="regresar", command=back_pi)
final.config(relief="raised")

siguiente_nivel=Button(cuadro_pi,text="siguiente", command=sig_pi)
final.config(relief="raised")

colocacion()







###ventana secundaria pop español

#contador puntaje


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

intro=Label(cuadro_pe, text = "Contesta las preguntas sobre pop")
intro.config(bg="white", fg="orange")
intro2=Label(cuadro_pe, text = "Al finalizar dar click en el botón final para conocer tu resultado")
intro2.config(bg="white", fg="orange")
nombre=Label(cuadro_pe, text="Ingresa tu nombre:")
nombre.config(bg="orange", fg="white")
respuesta_nombre=Entry(cuadro_pe)


#Uso de combobox para desplegar opciones de respuesta

pregunta1=Label(cuadro_pe, text="¿Qué banda canta la canción “Alejate de Mi”?")
pregunta1.config(bg="orange", fg="white")
pregunta2=Label(cuadro_pe, text="¿Qué canción pertenece a Ha-ash”? ")
pregunta2.config(bg="orange", fg="white")
pregunta3= Label(cuadro_pe, text = "Completa la letra: Si tu te vas ")
pregunta3.config(bg="orange", fg="white")
pregunta3_2= Label(cuadro_pe, text = "y yo me voy __________")
pregunta3_2.config(bg="orange", fg="white")
pregunta4=Label(cuadro_pe, text="¿Quién ganó el premio Grammy al mejor álbum de pop latino en 2017 ?")
pregunta4.config(bg="orange", fg="white")
pregunta5=Label(cuadro_pe, text="¿Qué artista canta la canción “Por ti”?")
pregunta5.config(bg="orange", fg="white")



#Uso de combobox para desplegar opciones de respuesta
opciones1_pe=Combobox(cuadro_pe,state="readonly",values=["Mana", "El Tri", "Camila", "Moderato"])
opciones2_pe=Combobox(cuadro_pe,state="readonly",values=["Ex de verdad", "Tu de que vas", "Perdón", "Espacio Sideral"])
opciones3_pe=Combobox(cuadro_pe,state="readonly",values=["que  vamos  a hacer", "es el fin", "a mi casa", "¿con quién se queda el perro?"])
opciones4_pe=Combobox(cuadro_pe,state="readonly",values=["Luis Miguel", "Shakira", "Bad Bunny", "Jesse & Joy"])
opciones5_pe=Combobox(cuadro_pe,state="readonly",values=["Yuridia", "Rio roma", "Belanova", "Timbiriche"])

opciones1_pe.place(x=130, y=230, width=320, height=25)
opciones2_pe.place(x=130, y=320, width=320, height=25)
opciones3_pe.place(x=130, y=440, width=320, height=25)
opciones4_pe.place(x=130, y=530, width=320, height=25)
opciones5_pe.place(x=130, y=620, width=320, height=25)

final=Button(cuadro_pe,text="Finalizar", command=mensaje_pe)
final.config(relief="raised")

regresar_inicio=Button(cuadro_pe,text="regresar", command=back_pe)
regresar_inicio.config(relief="raised")

siguiente_nivel=Button(cuadro_pe,text="siguiente", command=sig_pe)
siguiente_nivel.config(relief="raised")

fin_pe=Label(cuadro_pe, text = "")
fin_pe.config(bg="white", fg="orange")
fin_pe.place(x=170, y=660)

colocacion()








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

intro=Label(cuadro_m, text = "Contesta las preguntas sobre pop")
intro.config(bg="white", fg="hot pink")
intro2=Label(cuadro_m, text = "Al finalizar dar click en el botón final para conocer tu resultado")
intro2.config(bg="white", fg="hot pink")
nombre=Label(cuadro_m, text="Ingresa tu nombre:")
nombre.config(bg="hot pink", fg="white")
respuesta_nombre=Entry(cuadro_m)


#Uso de combobox para desplegar opciones de respuesta

pregunta1=Label(cuadro_m, text="¿De qué musical es la canción “For Forever”?")
pregunta1.config(bg="hot pink", fg="white")
pregunta2=Label(cuadro_m, text="¿Qué canción pertenece al musical “Be more chill”?")
pregunta2.config(bg="hot pink", fg="white")
pregunta3= Label(cuadro_m, text = "Completa la letra “Honey what you’re waiting")
pregunta3.config(bg="hot pink", fg="white")
pregunta3_2= Label(cuadro_m, text = "for? Shut up ______ “")
pregunta3_2.config(bg="hot pink", fg="white")
pregunta4=Label(cuadro_m, text="¿Cuál personaje canta “One Last time” en Hamilton?")
pregunta4.config(bg="hot pink", fg="white")
pregunta5=Label(cuadro_m, text="¿Quién ganó el premio Tony al mejor musical en 2008?")
pregunta5.config(bg="hot pink", fg="white")


#Uso de combobox para desplegar opciones de respuesta
opciones1_m=Combobox(cuadro_m,state="readonly",values=["Beetlejuice","Rent","Dear Evan Hansen","Mean Girls"])
opciones2_m=Combobox(cuadro_m,state="readonly",values=["Michael in the bathroom","Burn", "Meant to be yours","Dead mom"])
opciones3_m=Combobox(cuadro_m,state="readonly",values=["now  past","Veronica","please","Heather"])
opciones4_m=Combobox(cuadro_m,state="readonly",values=["Eliza","George Washington","Alexander Hamilton","Aaron Burr"])
opciones5_m=Combobox(cuadro_m,state="readonly",values=["Wicked","Crybaby","Matilda","In the Heights"])

opciones1_m.place(x=130, y=230, width=320, height=25)
opciones2_m.place(x=130, y=320, width=320, height=25)
opciones3_m.place(x=130, y=440, width=320, height=25)
opciones4_m.place(x=130, y=530, width=320, height=25)
opciones5_m.place(x=130, y=620, width=320, height=25)

final=Button(cuadro_m,text="Finalizar", command=mensaje_m)
final.config(relief="raised")

regresar_inicio=Button(cuadro_m,text="regresar", command=back_m)
regresar_inicio.config(relief="raised")

siguiente_nivel=Button(cuadro_m,text="siguiente", command=sig_m)
siguiente_nivel.config(relief="raised")
fin_m=Label(cuadro_m, text = "")
fin_m.config(bg="white", fg="hot pink")
fin_m.place(x=170, y=660)

colocacion()




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

intro=Label(cuadro_r, text = "Contesta las preguntas sobre rock")
intro.config(bg="white", fg="darkviolet")
intro2=Label(cuadro_r, text = "Al finalizar dar click en el botón final para conocer tu resultado")
intro2.config(bg="white", fg="darkviolet")
nombre=Label(cuadro_r, text="Ingresa tu nombre:")
nombre.config(bg="darkviolet", fg="white")
respuesta_nombre=Entry(cuadro_r)


#Uso de combobox para desplegar opciones de respuesta

pregunta1=Label(cuadro_r, text="¿De qué banda es la canción “Under Pressure”?")
pregunta1.config(bg="darkviolet", fg="white")
pregunta2=Label(cuadro_r, text="¿Qué canción pertenece a la banda “Aerosmith”?")
pregunta2.config(bg="darkviolet", fg="white")
pregunta3= Label(cuadro_r, text = "Completa la letra Is this the real life?")
pregunta3.config(bg="darkviolet", fg="white")
pregunta3_2= Label(cuadro_r, text = " Is this just ___________ ?")
pregunta3_2.config(bg="darkviolet", fg="white")
pregunta4=Label(cuadro_r, text="¿Qué banda canta “Creep” ?")
pregunta4.config(bg="darkviolet", fg="white")
pregunta5=Label(cuadro_r, text=" ¿Quién ganó el premio Grammy al mejor album de rock en 2013?")
pregunta5.config(bg="darkviolet", fg="white")


#Uso de combobox para desplegar opciones de respuesta
opciones1_r=Combobox(cuadro_r,state="readonly",values=["Queen","Kiss","Rolling Stones","Beatles"])
opciones2_r=Combobox(cuadro_r,state="readonly",values=["All in black", "Satisfaction","Dream On","Let it be"])
opciones3_r=Combobox(cuadro_r,state="readonly",values=["a dream","my imagination", "me", "fantasy"])
opciones4_r=Combobox(cuadro_r,state="readonly",values=["Radiohead", "AC/DC","The White Stripes","Nirvana"])
opciones5_r=Combobox(cuadro_r,state="readonly",values=["Foo fighters", "U2", "Led Zeppelin", "Green Day"])

opciones1_r.place(x=130, y=230, width=320, height=25)
opciones2_r.place(x=130, y=320, width=320, height=25)
opciones3_r.place(x=130, y=440, width=320, height=25)
opciones4_r.place(x=130, y=530, width=320, height=25)
opciones5_r.place(x=130, y=620, width=320, height=25)

final=Button(cuadro_r,text="Finalizar", command=mensaje_r)
final.config(relief="raised")

regresar_inicio=Button(cuadro_r,text="regresar", command=back_r)
regresar_inicio.config(relief="raised")

siguiente_nivel=Button(cuadro_r,text="siguiente", command=sig_r)
siguiente_nivel.config(relief="raised")

colocacion()

ventana_pi.iconify()
ventana_pe.iconify()
ventana_m.iconify()
ventana_r.iconify()



ventana.mainloop()
