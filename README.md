# Proyecto-TC1028

## Convertidor de unidades

Una unidad de medida es un valor designado que se "usa para medir la magnitud física de un objeto, sustancia o fenómeno" (Unidades de medida, 2019). Las unidades de medida tienen una gran importancia en nuestra vida ya que  permiten calcular cosas como la longitud, la masa, la capacidad, la superficie, el volumen, la temperatura, ó el tiempo. La temperatura es una medida relativa, las escalas que se basan en puntos de referencia deben ser usadas para medir la temperatura con precisión. Elegí las 3 unidades de temperatura más conocidas ya que las escalas de temperatura "nos permiten medir la energia del calor de una manera ligeramente diferente"(Martha, 2003). 

Este programa es un convertidor de unidades en el que el usuario podrá saber la conversión de diferentes medidas de temperatura en Kelcin, Celsius, Fahrenheit y la longitud del sistema internacional de medidas y el sistema ingles. Esto facilitara los procesos al usuario de manera rápida y eficaz.

Decidi crear este programa ya que creo que las unidades de medida forman parte de nuestra vida, y existen ocasiones en las que no estamos familiarizados con el sistema de unidades inglés. Por lo qué, un convertidor de unidades sería una herramienta muy útil. 

Referencias: 

Unidades de medida. (2019, 8 agosto). Significados. Recuperado 22 de septiembre de 2022, de https://www.significados.com/unidades-de-medida/

Day,M & Carphi,A (2003)	Temperatura. Recuperado 22 de septiembre de 2022, de https://www.visionlearning.com/es/library/Ciencias-Generales/3/Temperatura/48

Kuchling, A (2022). Expresiones Regulares. Recuperado 11 de octubre de 2022 de https://docs.python.org/es/3/howto/regex.html 

## Pseudocódigo

Importar las expresiones regulares con la biblioteca RegEx. Este lenguaje se encuentra dentro de python en el módulo Re que permite comparar cadenas con patrones predeterminados 

#Funciones temperatura

  ce_a_ke(c):
  
    k=c+273.15
    return k
	
 ke_a_ce(k):
 
    c=k-273.15
    return c
	
 fa_a_ce():
 
    c=(5*(f-32))/9
    return c
	
 ce_a fa():
 
    f=((9*c)/5)+32
    return f
	
 ke_a_fa():
 
    f=(((9*(k-273.15))/9)+32
    return f
	
 fa_a_ke():
 
    k=(((5*(f-32))/9)+273.15
    return k

#Funciones medidas

 cm_a_in(cm):
 
    in=cm/2.54
    return in
	
 in_a_cm(in):
 
    cm=in*2.54
    return cm
	
 ft_a_m(ft):
 
    m=ft*0.3048
    return m
	
 m_a_ft(m):
 
    ft=m/0.3048
    return ft
	
 yd_a_m(yd):
 
    m=yd*0.914
    return m
	
 m_a_yd(m):
 
    yd=m/0.914
    return m
	
 mi_km(mi):
 
    km=mi*1.609
    return km
	
 km_a_mi():
 
    mi=km/1.609
    return mi
 
 funcion comprobar_nombre(nombre):

    patron_nombre = nombre + espacio + apellido1 + espacio + apellido2
    mientras re.search(patron_nombre,nombre) no coincidan:
	imprimir "Nombre inválido favor de escribir tu nombre completo"
	nombre =input ("\nPara continuar ingresa tu nombre completo:\n"
    return nombre

 funcion comprobar_edad(edad):
   
    mientras edad>110 or edad<=0:
      imprimir "Respuesta inválida favor de responder de nuevo"
      edad=int(input("¿Cuántos años tienes?\n"))
    return edad


 funcion verificar_correo(mail):
    
    patron=letras,numeros y signos + @ + letras + . + 2 a 3 caracteres
    mientras re.search(patron,mail)no coinciden:
        imprimir "correo invalido favor de ingresar de nuevo su correo")¡
        mail=input("Ingresa tu correo electrónico:")
    return mail


 función comprobar_respuesta_1(respuesta_1):
    
    mientras respuesta_1 en minusculas sea diferente a "a" y respuesta_1 en minusculas sea diferente a "b": 
        imprimir("Respuesta no válida favor de contestar solo con A ó B\n")
        respuesta_1=input()
    return respuesta_1

 función comprobar_respuesta_2(respuesta_2):
    
    mientras respuesta_2 sea mayor que 8 y menor o igual a 0:
        imprimir("Respuesta no válida favor de contestar solo con 1,2,3,4,5,6,7 ó 8")
        respuesta_2=int(input())
    return respuesta_2
 
 función comprobar_respuesta_3(respuesta_3):
    
    mientras respuesta_3 sea mayor a 6 o menor o igual a 0:
        imprimir("Respuesta no válida favor de contestar solo con 1,2,3,4,5 ó 6 /n")
        respuesta_3=int(input())
    return respuesta_3
    
 función mostrar_opciones_a():    
    
    imprimir"Elige que deseas convertir:"
    imprimir"1- centímetros a pulgadas"
    imprimir"2- pulgadas a centímetros" 
    imprimir"3- pies a metros"
    imprimir"4- metros a pies"
    imprimir"5- yardas a metros"
    imprimir "6- metros a yardas"
    imprimir "7- millas a kilometros"
    imprimir "8- kilómetros a millas"

    r2=int(input())
    respuesta_2=comprobar_respuesta_2(r2)
    si la respuesta_2 es igual 1:
        cm=float(input("Ingresa los centímetros: "))
        imprimir("la respuesta es: ",cm_a_in(cm),"pulgadas")
 
    si la respuesta_2 es igual 2:
        inch=float(input("Ingresa las pulgadas: "))
        imprimir("la respuesta es: ",in_a_cm (inch),"centímetros")

    si la respuesta_2 es igual 3:
        ft=float(input("Ingresa las pulgadas: "))
        imprimir("la respuesta es: ",ft_a_m (ft),"metros")

    si la respuesta_2 es igual 4:
        m=float(input("Ingresa los metros: "))
        imprimir("la respuesta es: ",m_a_ft(m),"pies")

    si la respuesta_2 es igual 5:
        yd=float(input("Ingresa las yardas: "))
        imprimir("la respuesta es: ",yd_a_m(yd),"metros")

    si la respuesta_2 es igual 6:
        m=float(input("Ingresa los metros: "))
        imprimir("la respuesta es: ",m_a_yd(m),"yardas")
        
    si la respuesta_2 es igual7:
        mi=float(input("Ingresa los millas: "))
        imprimir("la respuesta es: ",mi_a_km(mi),"kilómetros")

    si la respuesta_2 es igual8:
        km=float(input("Ingresa los km: "))
        imprimirt("la respuesta es: ",km_a_mi(km),"millas")


 funcion mostrar_opciones_b():
 
    imprimir "Elige que deseas convertir:"
    imprimir "1- Celcius a Kelvin"
    imprimir "2- Kelvin a Celcius" 
    imprimir "3- Fahrenheit a Celsius"
    imprimir "4- Celsius a Fahrenheit"
    imprimir "5- Kelvin a Fahrenheit"
    imprimir "6- Fahrenheit a Celsius"
    
    r3=int(input())
    respuesta_3=comprobar_respuesta_3(r3)
    si la respuesta_3 es igual a 1:
        c=float(input("Ingresa los grados Celsius: "))
        imprimir "la respuesta es: ",ce_a_ke(c),"grados Kelvin"
		
    si la respuesta_3 es igual a 2:
        k=float(input("Ingresa los grados Kelvin: "))
        imprimir "la respuesta es: ",ke_a_ce (k),"grados Celcius"

    si la respuesta_3 es igual a 3:
        f=float(input("Ingresa los grados Fahrenheit: "))
        imprimir "la respuesta es: ",fa_a_ce(f),"grados Celcius"
  
    si la respuesta_3 es igual a 4:
        c=float(input("Ingresa los grados Celsius: "))
        imprimir "la respuesta es: ",ce_a_fa (c),"grados Fahrenheit"

    si la respuesta_3 es igual a 5:
        k=float(input("Ingresa los grados Kelvin: "))
        imprimir "la respuesta es: ",ke_a_fa(k),"grados Fahrenheit"

    si la respuesta_3 es igual a 6:
        f=float(input("Ingresa los grados Fahrenheit: "))
        imprimir "la respuesta es: ",fa_a_ke(f),"grados Kelvin"
        

 funcion comprobar_r4_r5(r):
 
    mientras r sea diferente a "1" o r sea diferente a "2":
        imprimir "Respuesta invalida favor de contestar con 1 o 2"
        r=input()
    return r


 funcion crear_diccionario():
 
    diccionario={"nombre":nombre,"edad":edad,"email":correo,"conversiones realizadas":cantidad_c,"conversiones de medida":respuestas_lista_med,"conversiones de temperatura":respuestas_lista_temp}
    lista_con_diccionarios agregar (diccionario)

 funcion mostrar_diccionario(lista_con_diccionarios):
 
    para el elemento en lista_con_diccionarios:
        para la llave en elemento:
            imprimir llave + ": " + str(elemento[llave]) +"\n"



	ban=1
	lista_con_diccionarios=[]
	mientras ban==1:
    imprimir "Hola bienvenido a este programa.")
    imprimir "Aquí podrás convertir tus unidades de una manera fácil y rápida.")
   
    nombre=input ("Para continuar ingresa tu nombre completo:\n")
    llamar funcion comprobar_nombre(nombre)
    
    edad=input("¿Cuántos años tienes?\n")
    llamar funcion comprobar_edad(edad)
    
    correo=input("Ingresa tu correo electrónico:\n")
    llamar funcion verificar_correo(correo)
    
    respuestas_lista_temp=[]
    respuestas_lista_med=[] 
    
    cantidad_c=int(input("¿Cuántas converciones vas a realizar?\n"))
    for i in range (0,cantidad_c):

        imprimir "Elige una opción para continuar (contestar solo con letras)"
        imprimir "¿Qué quieres convertir?"
        imprimir "A-Medidas de longitud"
        imprimir "B-Temperatura "

        r1=input()
        respuesta_1=comprobar_respuesta_1(r1)
        si respuesta_1  es igual a "a":
            mostrar_opciones_a()
        si respuesta_1 es igual a "b":
            mostrar_opciones_b()

    
    imprimir "Tus converciones de temperatura fueron:",respuestas_lista_temp
    imprimir "Tus converciones de medida fueron:",respuestas_lista_med
    llamar funcion crear_diccionario()

    imprimir "¿Quiéres continuar con el programa? 1.Si 2.No"
    r4=input()
    r4=comprobar_r4_r5(r4)
    si r4 es igual a "1":
        ban=1
    si r4 es igual a "2":
        imprimir "¿Quiéres conocer el historial de conversiones? 1.Si 2.No"
        r5=input()
        r5=comprobar_r4_r5(r5)
        si r5 es igual a "1":
            imprimir "mostrar_diccionario(lista_con_diccionarios)
            imprimir "El programa ha terminado"
            ban=0
        si r5 es igual a "2":
            imprimir "El programa ha terminado"
            ban=0

