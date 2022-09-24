from tkinter import*
from tkinter import ttk

#Funciones temperatura
def ce_a_ke(c):
    k=c+273.15
    return k

def ke_a_ce(k):
    c=k-273.15
    return c

def fa_a_ce(f):
    c=(5*(f-32))/9
    return c

def ce_a_fa(c):
    f=((9*c)/5)+32
    return f

def ke_a_fa(k):
    f=((9*(k-273.15))/9)+32
    return f

def fa_a_ke(f):
    k=((5*(f-32))/9)+273.15
    return k

#Funciones medidas
def cm_a_in(cm):
    inch=cm/2.54
    return inch
    
def in_a_cm(inch):
    cm=inch*2.54
    return cm
    
def ft_a_m(ft):
    m=ft*0.3048
    return m

def m_a_ft(m):
    ft=m/0.3048
    return ft

def yd_a_m(yd):
    m=yd*0.914
    return m

def m_a_yd(m):
    yd=m/0.914
    return m	

def mi_km(mi):
    km=mi*1.609
    return km

def km_a_mi(km):
    mi=km/1.609
    return mi

def comprobar_nombre(nombre):
    caracteres_nombre=len(nombre)
    while caracteres_nombre<2:
      print("\nNombre inválido favor de escribir un nombre que contenga como mínimo 2 caracteres")
      nombre=input ("Para continuar ingresa tu nombre completo: ")
      caracteres_nombre=len(nombre)
    
def comprobar_edad(edad):
    while edad>110 or edad<=0:
      print("\Respuesta inválida favor de responder de nuevo")
      edad=int(input("¿Cuántos años tienes?\n"))

    
def comprobar_respuesta_1(respuesta_1):
    while respuesta_1.lower()!= "a" and respuesta_1.lower()!= "b": 
        print("Respuesta no válida favor de contestar solo con A ó B\n")
        respuesta_1=input()
    return respuesta_1

def comprobar_respuesta_2(respuesta_2):
    while respuesta_2>8 or respuesta_2<=0:
        print("Respuesta no válida favor de contestar solo con 1,2,3,4,5,6,7 ó 8")
        respuesta_2=int(input())
    return respuesta_2

def comprobar_respuesta_3(respuesta_3):
    while respuesta_3>6 or respuesta_3<=0:
        print("Respuesta no válida favor de contestar solo con 1,2,3,4,5 ó 6 /n")
        respuesta_3=int(input())
    return respuesta_3



print("Hola bienvenido a este programa.")
print("Aquí podrás convertir tus unidades de una manera fácil y rápida.")
nombre=input ("Para continuar ingresa tu nombre completo: ")
comprobar_nombre(nombre)

edad=int(input("¿Cuántos años tienes?\n"))
comprobar_edad(edad)

print("Elige una opción para continuar (contestar solo con letras)")
print("¿Qué quieres convertir?")
print("A-Medidas de longitud")
print("B-Temperatura ")

r1=input()
respuesta_1=comprobar_respuesta_1(r1)


if respuesta_1 == "a":
    print("Elige que deseas convertir:") 
    print("1- centímetros a pulgadas")
    print("2- pulgadas a centímetros") 
    print("3- pies a metros")
    print("4- metros a pies")
    print("5- yardas a metros")
    print("6- metros a yardas")
    print("7- millas a kilometros")
    print("8- kilómetros a millas")
    r2=int(input())
    respuesta_2=comprobar_respuesta_2(r2)

    if respuesta_2 == 1:
        cm=float(input("Ingresa los centímetros: "))
        print("la respuesta es: ",cm_a_in(cm))
		
    elif respuesta_2 == 2:
        inch=float(input("Ingresa las pulgadas: "))
        print("la respuesta es: ",in_a_cm (inch))

    elif respuesta_2 == 3:
        ft=float(input("Ingresa las pulgadas: "))
        print("la respuesta es: ",ft_a_m (ft))

    elif respuesta_2 == 4:
        m=float(input("Ingresa los metros: "))
        print("la respuesta es: ",m_a_ft(m)) 

    elif respuesta_2 == 5:
        yd=float(input("Ingresa las yardas: "))
        print("la respuesta es: ",yd_a_m(yd)) 

    elif respuesta_2 == 6:
        m=float(input("Ingresa los metros: "))
        print("la respuesta es: ",m_a_yd(m)) 

    elif respuesta_2 == 7:
        mi=float(input("Ingresa los millas: "))
        print("la respuesta es: ",mi_a_km(mi))

    elif respuesta_2 == 8:
        km=float(input("Ingresa los km"))
        print("la respuesta es: ",km_a_mi(km))

if respuesta_1 == "b":
    print("Elige que deseas convertir:") 
    print("1- Celcius a Kelvin")
    print("2- Kelvin a Celcius") 
    print("3- Fahrenheit a Celsius")
    print("4- Celsius a Fahrenheit")
    print("5- Kelvin a Fahrenheit")
    print("6- Fahrenheit a Celsius")

    r3=int(input())
    respuesta_3=comprobar_respuesta_3(r3)

    if respuesta_3 == 1:
        c=float(input("Ingresa los grados Celsius: "))
        print("la respuesta es: ",ce_a_ke(c),"grados Kelvin")
		
    elif respuesta_3 == 2:
        k=float(input("Ingresa los grados Kelvin: "))
        print("la respuesta es: ",ke_a_ce (k),"grados Celcius")

    elif respuesta_3 == 3:
        f=float(input("Ingresa los grados Fahrenheit: "))
        print("la respuesta es: ",fa_a_ce(f),"grados Celcius")

    elif respuesta_3 == 4:
        c=float(input("Ingresa los grados Celsius: "))
        print("la respuesta es: ",ce_a_fa (c),"grados Fahrenheit") 

    elif respuesta_3 == 5:
        k=float(input("Ingresa los grados Kelvin: "))
        print("la respuesta es: ",ke_a_fa(k),"grados Fahrenheit") 

    elif respuesta_3 == 6:
        f=float(input("Ingresa los grados Fahrenheit: "))
        print("la respuesta es: ",fa_a_ke(f),"grados Kelvin") 

