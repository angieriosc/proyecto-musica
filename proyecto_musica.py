#importamos la biblioteca RegEx para el uso de una verificación de datos por medio de patrones previamente establecidos
import re 

#Funciones temperatura (se realizan operaciones para obtener el resultado de la conversión y luego se añaden a la lista de temperaturas)
def ce_a_ke(c):
    k=c+273.15
    respuestas_lista_temp.append(k)
    return k

def ke_a_ce(k):
    c=k-273.15
    respuestas_lista_temp.append(c)
    return c

def fa_a_ce(f):
    c=(5*(f-32))/9
    respuestas_lista_temp.append(c)
    return c

def ce_a_fa(c):
    f=((9*c)/5)+32
    respuestas_lista_temp.append(f)
    return f

def ke_a_fa(k):
    f=((9*(k-273.15))/9)+32
    respuestas_lista_temp.append(f)
    return f

def fa_a_ke(f):
    k=((5*(f-32))/9)+273.15
    respuestas_lista_temp.append(k)
    return k

#Funciones medidas(se realizan operaciones para obtener el resultado de la conversión y luego se añaden a la lista de medidas)
def cm_a_in(cm):
    inch=cm/2.54
    respuestas_lista_med.append(inch)
    return inch
    
def in_a_cm(inch):
    cm=inch*2.54
    respuestas_lista_med.append(cm)
    return cm
    
def ft_a_m(ft):
    m=ft*0.3048
    respuestas_lista_med.append(m)
    return m

def m_a_ft(m):
    ft=m/0.3048
    respuestas_lista_med.append(ft)
    return ft

def yd_a_m(yd):
    m=yd*0.914
    respuestas_lista_med.append(m)
    return m

def m_a_yd(m):
    yd=m/0.914
    respuestas_lista_med.append(yd)
    return yd	

def mi_a_km(mi):
    km=mi*1.609
    respuestas_lista_med.append(km)
    return km

def km_a_mi(km):
    mi=km/1.609
    respuestas_lista_med.append(mi)
    return mi

#Función que contiene un ciclo while que verifica que sea un nombre real
#Primero se establece el patrón (Acepta valores de a-z en minúsculas y mayúsculas
#El código \u00C0-\u017F es un valor que permite que el usuario ingrese su nombre con acentos
#Si la busqueda del patron en el nombre no coincide se entra en el ciclo
#Al final uso return para regresar el nombre verificado
def comprobar_nombre(name):
    patron_nombre='^[a-zA-Z\u00C0-\u017F]+[ ]+[a-zA-Z\u00C0-\u017F]+[ ]+[a-zA-Z\u00C0-\u017F]'
    while re.search(patron_nombre,name)==None:
        print("Nombre inválido favor de escribir tu nombre completo(con los dos apellidos)")
        name=input ("\nPara continuar ingresa tu nombre completo:\n")
    return name

#Función que contiene un ciclo while que verifica que sea una edad posible

def comprobar_edad(edad):
    while edad>=110 or edad<=0:
      print("Respuesta inválida favor de responder de nuevo")
      edad=int(input("¿Cuántos años tienes?\n"))
    return edad


#Función que contiene un ciclo while y mediante la funcion de re.search que verifica que el correo ingresado por el usuario
#cuente con el formato que suelen tener la mayoría de los correos
#el signo ? indica que puede aparecer o no
def verificar_correo(mail):
    patron='^[a-zA-Z 0-9 ._]+[@]\w+[a-zA-Z]+[.]\w{2,3}$'
    while re.search(patron,mail)== None:
        print ("correo invalido favor de ingresar de nuevo su correo")
        mail=input("\nIngresa tu correo electrónico:\n")
    return mail

#Función que contiene un ciclo while que verifica que la respuesta sea a o b
#Se utiliza .lower para que no afecte si el usuario ingresa la respuesta en mayúsculas   
def comprobar_respuesta_1(respuesta_1):
    while respuesta_1.lower()!= "a" and respuesta_1.lower()!= "b": 
        print("Respuesta no válida favor de contestar solo con A ó B\n")
        respuesta_1=input()
    return respuesta_1

#Función que contiene un ciclo while que verifica que la respuesta 2 entre dentro del rango de opciones posibles 
def comprobar_respuesta_2(respuesta_2):
    while respuesta_2>8 or respuesta_2<=0:
        print("Respuesta no válida favor de contestar solo con 1,2,3,4,5,6,7 ó 8")
        respuesta_2=int(input())
    return respuesta_2

#Función que contiene un ciclo while que verifica que la respuesta 3 entre dentro del rango de opciones posibles 
def comprobar_respuesta_3(respuesta_3):
    while respuesta_3>6 or respuesta_3<=0:
        print("Respuesta no válida favor de contestar solo con 1,2,3,4,5 ó 6 /n")
        respuesta_3=int(input())
    return respuesta_3

#Función que se ejecuta si el usuario elige la opción a (conversión de medidas)  
def mostrar_opciones_a():
#Muestra las opciones de conversiones de medidas al usuario #muestra las opciones de conversiones de medidas al usuario    
    print("Elige que deseas convertir:") 
    print("1- centímetros a pulgadas")
    print("2- pulgadas a centímetros") 
    print("3- pies a metros")
    print("4- metros a pies")
    print("5- yardas a metros")
    print("6- metros a yardas")
    print("7- millas a kilometros")
    print("8- kilómetros a millas")
#Se crea una variable para la respuesta 
    r2=int(input())
#Se manda llamar a la funcion que comprueba la respuesta
    respuesta_2=comprobar_respuesta_2(r2)

#Uso de if para obtener los resultados de las conversiones dependiendo de la opción que haya escogido el usuario
    if respuesta_2 == 1:
        cm=float(input("Ingresa los centímetros: "))
        print("la respuesta es: ",cm_a_in(cm),"pulgadas")
 
    elif respuesta_2 == 2:
        inch=float(input("Ingresa las pulgadas: "))
        print("la respuesta es: ",in_a_cm (inch),"centímetros")

    elif respuesta_2 == 3:
        ft=float(input("Ingresa las pulgadas: "))
        print("la respuesta es: ",ft_a_m (ft),"metros")

    elif respuesta_2 == 4:
        m=float(input("Ingresa los metros: "))
        print("la respuesta es: ",m_a_ft(m),"pies")

    elif respuesta_2 == 5:
        yd=float(input("Ingresa las yardas: "))
        print("la respuesta es: ",yd_a_m(yd),"metros")

    elif respuesta_2 == 6:
        m=float(input("Ingresa los metros: "))
        print("la respuesta es: ",m_a_yd(m),"yardas")
        
    elif respuesta_2 == 7:
        mi=float(input("Ingresa los millas: "))
        print("la respuesta es: ",mi_a_km(mi),"kilómetros")

    elif respuesta_2 == 8:
        km=float(input("Ingresa los km: "))
        print("la respuesta es: ",km_a_mi(km),"millas")

#Función que se ejecuta si el usuario elige la opción b (conversión de temperaturas)   
def mostrar_opciones_b():

    print("Elige que deseas convertir:") 
    print("1- Celcius a Kelvin")
    print("2- Kelvin a Celcius") 
    print("3- Fahrenheit a Celsius")
    print("4- Celsius a Fahrenheit")
    print("5- Kelvin a Fahrenheit")
    print("6- Fahrenheit a Celsius")
#Se crea una variable para la respuesta
    r3=int(input())
#Se manda llamar a la funcion que comprueba la respuesta
    respuesta_3=comprobar_respuesta_3(r3)
#Uso de if para obtener los resultados de las conversiones dependiendo de la opción que haya escogido el usuario
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
        
#Función que comprueba las respuestas r4 y r5 
#Se utiliza un ciclo while para que el usuario conteste con 1 o 2 
def comprobar_r4_r5(r):
    while r!="1" and r!="2":
        print("Respuesta invalida favor de contestar con 1 o 2")
        r=input()
    return r

#Función que crea un diccionario con los datos de el usuario que utilizo el programa
#Se utiliza la función .append () para agregar el diccionario creado a una lista 
def crear_diccionario():
    diccionario={"nombre":nombre,"edad":edad,"email":correo,"conversiones realizadas":cantidad_c,"conversiones de medida":respuestas_lista_med,"conversiones de temperatura":respuestas_lista_temp}
    lista_con_diccionarios.append(diccionario)
    
#Función que despliega la información guardada en la lista de diccionarios
#Uso de for para imprimir cada llave y su valor que se encuentran en el diccionario guardado en la lista de diccionarios 
def mostrar_diccionario(lista_con_diccionarios):
    for i in lista_con_diccionarios:
        for llave in i:
            print(llave + ": " + str(i[llave]) +"\n")


#Creación de variable que hace que el ciclo while comience
ban=1
#Creación de lista vacia que se llenara con la información que del usuario
lista_con_diccionarios=[]
#Ciclo while que permite que el programa continue corriendo hasta que el usuario quiera detenerlo
while ban==1:
#Bienvenida al programa y una breve explicación de lo que podrás realizar
    print("Hola bienvenido a este programa.")
    print("Aquí podrás convertir tus unidades de una manera fácil y rápida.")
    nombre=input ("Para continuar ingresa tu nombre completo:\n")
    #Se manda a llamar la función que comprueba al nombre
    comprobar_nombre(nombre)
    edad=int(input("¿Cuántos años tienes?\n"))
    #Se manda a llamar la función que comprueba la edad
    comprobar_edad(edad)
    #Se manda a llamar la función que verifica que el correo sea válido
    correo=input("Ingresa tu correo electrónico:\n")
    verificar_correo(correo)

    cantidad_c=int(input("¿Cuántas converciones vas a realizar?\n"))
    #Creación de listas para guardar los resultados de las converciónes de medidas y temperatura 
    respuestas_lista_temp=[]
    respuestas_lista_med=[]
    #Uso de for para que repita el programa dependiendo cuantas conversiones quiso hacer el usuario
    for i in range (0,cantidad_c):

        print("Elige una opción para continuar (contestar solo con letras)")
        print("¿Qué quieres convertir?")
        print("A-Medidas de longitud")
        print("B-Temperatura ")

        r1=input()
        respuesta_1=comprobar_respuesta_1(r1)
        if respuesta_1.lower()== "a":
            mostrar_opciones_a()
        elif respuesta_1.lower()== "b":
            mostrar_opciones_b()

    #Se imprimen las listas con los resultados del usuario
    print("Tus converciones de temperatura fueron:",respuestas_lista_temp)
    print("Tus converciones de medida fueron:",respuestas_lista_med)
    dic=crear_diccionario()

    print("¿Quiéres continuar con el programa? 1.Si 2.No")
    r4=input()
    r4=comprobar_r4_r5(r4)
    if r4=="1":
        ban=1
    elif r4=="2":
        print("¿Quiéres conocer el historial de conversiones? 1.Si 2.No")
        r5=input()
        r5=comprobar_r4_r5(r5)
        if r5=="1":
            mostrar_diccionario(lista_con_diccionarios)
            print("El programa ha terminado")
            ban=0
        elif r5=="2":
            print("El programa ha terminado")
            ban=0





        
