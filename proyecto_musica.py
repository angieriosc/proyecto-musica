"""
importamos la biblioteca RegEx para el uso de una verificación de datos\
por medio de patrones previamente establecidos
"""
import re 

"""
============= Funciones de conversión temperatura =============
"""

def ce_a_ke(c):
    """
    (uso de operadores, uso de funciones)
    recibe: 1 valor que corresponde a los grados celcius
    suma 273.15 a el valor y agrega el valor generado a la lista\
    de temperaturas.
    devuelve:el resultado de la operación cuya unidad son grados kelvin
    """
    k=c+273.15
    respuestas_lista_temp.append(k)
    return k

def ke_a_ce(k):
    """
    (uso de operadores, uso de funciones)
    recibe: 1 valor que corresponde a los grados kelvin
    resta 273.15 a el valor recibido y agrega el valor generado a \
    la lista de temperaturas.
    devuelve:el resultado de la operación que representa los grados celsius
    """
    c=k-273.15
    respuestas_lista_temp.append(c)
    return c

def fa_a_ce(f):
    """
    (uso de operadores, uso de funciones)
    recibe: 1 valor que corresponde a los grados fahrenheit  
    se resta 32 al valor recibido se multiplica por 5 y lo \
    obtenido se divide entre 9 y agrega el valor generado a \
    la lista de temperaturas.
    devuelve:el resultado de la operación cuya unidad son grados 
    """
    c=(5*(f-32))/9
    respuestas_lista_temp.append(c)
    return c

def ce_a_fa(c):
    """
    (uso de operadores, uso de funciones)
    recibe: 1 valor que corresponde a los grados celcius
    multiplica el valor recibido por 9 divide el resultado \
    entre 5 y al final se le suman 32 y agrega el valor generado a \
    la lista de temperaturas.
    devuelve:el resultado de la operación cuya unidad son grados fahrenheit
    """
    f=((9*c)/5)+32
    respuestas_lista_temp.append(f)
    return f

def ke_a_fa(k):
    """
    (uso de operadores, uso de funciones)
    recibe: 1 valor que corresponde a los grados kelvin
    resta 273.15 al valor recibido, multiplica el resultado por 9/5 \
    y se le suman 32 y agrega el valor generado a la lista \
     de temperaturas.
    devuelve:el resultado de la operación cuya unidad son grados fahrenheit
    """    
    f=(k-273.15)*(9/5)+32
    respuestas_lista_temp.append(f)
    return f

def fa_a_ke(f):
    """
    (uso de operadores, uso de funciones)
    recibe: 1 valor que corresponde a los grados fahrenheit
    resta 32 al valor recibido se multiplica el resultado por 5/9 \
    y se le suman 273.15 y agrega el valor generado a \
    la lista de temperaturas.
    devuelve:el resultado de la operación cuya unidad son grados kelvin
    """
    k=((f-32)*(5/9))+273.15
    respuestas_lista_temp.append(k)
    return k

"""
============= Funciones de conversión medidas =============
"""

def cm_a_in(cm):
    """
    (uso de operadores, uso de funciones)
    recibe: 1 valor que corresponde a los centrimetros 
    divir el valor recibido entre 2.54 y agrega el valor generado a \
    la lista de medidas.
    devuelve:el resultado de la operación cuya unidad son pulgadas
    """
    inch=cm/2.54
    respuestas_lista_med.append(inch)
    return inch
    
def in_a_cm(inch):
    """
    (uso de operadores, uso de funciones)
    recibe: 1 valor que corresponde a las pulgadas  
    se multiplica el valor recibido por 2.54vy agrega el valor generado a\
    la lista de medidas.
    devuelve:el resultado de la operación cuya unidad son centimetros 
    """
    cm=inch*2.54
    respuestas_lista_med.append(cm)
    return cm
    
def ft_a_m(ft):
    """
    (uso de operadores, uso de funciones)
    recibe: 1 valor que corresponde a los pies  
    multiplica el valor recibido por 0.3048 y agrega el valor generado a\
    la lista de medidas.
    devuelve:el resultado de la operación cuya unidad son metros
    """
    m=ft*0.3048
    respuestas_lista_med.append(m)
    return m

def m_a_ft(m):
    """
    (uso de operadores, uso de funciones)
    recibe: 1 valor que corresponde a los metros  
    divide el valor recibido entre 0.3048 y agrega el valor generado a \
    la lista de medidas.
    devuelve:el resultado de la operación cuya unidad son pies
    """
    ft=m/0.3048
    respuestas_lista_med.append(ft)
    return ft

def yd_a_m(yd):
    """
    (uso de operadores, uso de funciones)
    recibe: 1 valor que corresponde a las yardas
    multiplica el valor recibido por 0.914 y agrega el valor generado a \
    la lista de medidas.
    devuelve:el resultado de la operación cuya unidad son 
    """ 
    m=yd*0.914
    respuestas_lista_med.append(m)
    return m

def m_a_yd(m):
    """
    (uso de operadores, uso de funciones)
    recibe: 1 valor que corresponde a los metros  
    divide el valor recibido entre 0.914 y agrega el valor generado a \
    la lista de  medidas.
    devuelve:el resultado de la operación cuya unidad son yardas
    """
    yd=m/0.914
    respuestas_lista_med.append(yd)
    return yd	

def mi_a_km(mi):
    """
    (uso de operadores, uso de funciones)
    recibe: 1 valor que corresponde a las millas
    multiplica el valor recibido por 1.609 y agrega el valor generado a \
    la lista de  medidas.
    devuelve:el resultado de la operación cuya unidad son kilometros
    """    
    km=mi*1.609
    respuestas_lista_med.append(km)
    return km

def km_a_mi(km):
    """
    (uso de operadores, uso de funciones)
    recibe: 1 valor que corresponde a los kilometros
    divide el valor recibido entre 1.609 y agrega el valor generado a \
    la lista de  medidas.
    devuelve:el resultado de la operación cuya unidad son millas
    """    
    mi=km/1.609
    respuestas_lista_med.append(mi)
    return mi


"""
============= Funciones de comprobación =============
"""

def comprobar_nombre(name):
    """
    (uso de funciones, expresiones regulares en biblioteca RegEx,ciclos)
    recibe: variable str que corresponde al nombre del usuario
    se crea un patron que ayudara a comprobar que existan 3 cadenas \
    y mediante un ciclo se utiliza la funcion re.search() si la variable\
    recibida no cuenta con el patron establecido entra en el ciclo y le \
    vuelve a preguntar el nombre. Si si cuenta con el patron rompe el ciclo.
    devuelve:el nombre verificado
    """  
    patron_nombre='^[a-zA-Z\u00C0-\u017F]+[ ]+[a-zA-Z\u00C0-\u017F]+[ ]+\
[a-zA-Z\u00C0-\u017F]'
    while re.search(patron_nombre,name)==None:
        print("Nombre inválido favor de escribir tu nombre completo(con \
los dos apellidos)")
        name=input ("\nPara continuar ingresa tu nombre completo:\n")
    return name


def comprobar_edad(edad):
    """
    (uso de funciones, condicionales ,ciclos)
    recibe: variable int que corresponde a la edad del usuario
    mediante un ciclo se  checa si el valor ingresado es menor a 0 ó mayor\
    a 110 si cumple con alguna de estas caracteristicas entra en el ciclo\
    y vuelve a preguntar la edad, hasta que de un dato mayor a 0 y menor a\
    110
    devuelve:la edad verificada.
    """  
    while edad>=110 or edad<=0:
      print("Respuesta inválida favor de responder de nuevo")
      edad=int(input("¿Cuántos años tienes?\n"))
    return edad


def verificar_correo(mail):
    """
    (uso de funciones, expresiones regulares en biblioteca RegEx,ciclos)
    recibe: variable str que corresponde al correo del usuario
    se crea un patron que ayudara a comprobar que exista un formato \
    de letras,numeros,guiones o puntos + un arroba + letras + un punto +\
    un ultimo texto que contenga de 2 a 3 caracteres.mediante un ciclo se\
    utiliza la funcion re.search() si la variable recibida no cuenta con\
    el patron establecido entra en el ciclo y le vuelve a preguntar el\
    correo. Si si cuenta con el patron rompe el ciclo.
    devuelve: el correo verificado.
    """  
    patron='^[a-zA-Z 0-9 ._]+[@]\w+[a-zA-Z]+[.]\w{2,3}$'
    while re.search(patron,mail)== None:
        print ("correo invalido favor de ingresar de nuevo su correo")
        mail=input("\nIngresa tu correo electrónico:\n")
    return mail

 
def comprobar_respuesta_1(respuesta_1):
    """(uso de funciones,ciclos,operadores booleanos y manipulación \
    de cadenas)
    recibe: variable str que corresponde a la respuesta de que tipo de \
    conversión quieres realizar.
    mediante un ciclo se  checa si la variable ingresada en minúsculas\
    es diferente a "a" y "b", si es diferente a ambos entra al ciclo y \
    vuelve a preguntar la respuesta, hasta que el usuario responda a o b\
    devuelve:la respuesta 1 verificada.
    """  
    while respuesta_1.lower()!= "a" and respuesta_1.lower()!= "b": 
        print("Respuesta no válida favor de contestar solo con A ó B\n")
        respuesta_1=input()
    return respuesta_1


def comprobar_respuesta_2(respuesta_2):
    """(uso de funciones,ciclos y operadores booleanos)
    recibe: variable int que corresponde a la respuesta de que conversión\
    de medida quieres realizar.
    mediante un ciclo se  checa si la variable ingresada es mayor a 8\
    o menor o igual a 0 si cumple alguna de estas condiciones entra al \
    ciclo y vuelve a preguntar la respuesta, hasta que el usuario ingrese\
    un valor menor o igual a 8 y mayor a 0.
    devuelve: la respuesta 2 verificada.
    """  
    while respuesta_2>8 or respuesta_2<=0:
        print("Respuesta no válida favor de contestar solo con \
        1,2,3,4,5,6,7 ó 8")
        respuesta_2=int(input())
    return respuesta_2


def comprobar_respuesta_3(respuesta_3):
    """(uso de funciones,ciclos y operadores booleanos)
    recibe: variable int que corresponde a la respuesta de que conversión \
    de temperatura quieres realizar.
    mediante un ciclo se  checa si la variable ingresada es mayor a 6\
    o menor o igual a 0 si se cumple alguna de estas condiciones entra al \
    ciclo y vuelve a preguntar la respuesta, hasta que el usuario ingrese\
    un valor menor o igual a 6 y mayor a 0.
    devuelve: la respuesta 3 verificada
    """  
    while respuesta_3>6 or respuesta_3<=0:
        print("Respuesta no válida favor de contestar solo con\
        1,2,3,4,5 ó 6 /n")
        respuesta_3=int(input())
    return respuesta_3

 
def mostrar_opciones_a():
    """(uso de funciones y condicionales)
    recibe: no recibe ningun parametro
    muestra las opciones comprueba la respuesta con la funcion \
    comprobar_respuesta_2(r2)de conversiones de medida y mediante \
    condicionale se llama a la función que corresponde a la respuesta 2\
    muestra el dato que el usuario debe ingresar y ejecuta \
    la funcion de conversión de medida correspondiente al final imprime\
    el resultado de la conversión
    devuelve: no devuelve ningun valor
    """  

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

  
def mostrar_opciones_b():
    """(uso de funciones y condicionales)
    recibe: no recibe ningun parametro
    muestra las opciones de conversiones de temperatura y mediante \
    condicionales se llama a la función comprobar_respuesta_3(r3)con \
    el dato previamente ingresado en r3 ymuestra el dato que el usuario \
    debe ingresar y ejecuta la funcion de conversión de temperatura\
    correspondiente y al final imprime el resultado de la conversión.\
    devuelve: no devuelve ningun valor
    """  

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
        

def comprobar_r4_r5(r):
    """(uso de funciones,ciclos y operadores booleanos)
    recibe: variable str que corresponde a la respuesta de si quieres \
    continuar con el programa y si quieres ver el historial de conversiones.
    mediante un ciclo se checa que la variable no sea diferente a 1 y 2 \
    si lo es, entra al ciclo y vuelve a preguntar la respuesta, hasta que\
    el usuario ingrese un "1" o un "2".
    devuelve: la respuesta verificada
    """  
    while r!="1" and r!="2":
        print("Respuesta invalida favor de contestar con 1 o 2")
        r=input()
    return r


def crear_diccionario():
    """(uso de funciones,diccionarios, listas)
    recibe: no recibe variables 
    Se crea un diccionario, se registan las llaves y se les dan los valores\
    con los datos previamente capturados y verificados por el programa.\
    Después se agrega el diccionario creado a  una lista con diccionarios \
    previamente establecida.
    devuelve: no devuelve nada ya que en python si se guardan las \
    modificaciones en las listas a pesar de que este en una función.
    """ 
    diccionario={"nombre":nombre,"edad":edad,"email":correo,\
                "conversiones realizadas":cantidad_c,\
                "conversiones de medida":respuestas_lista_med,\
                "conversiones de temperatura":respuestas_lista_temp}
    lista_con_diccionarios.append(diccionario)
    

def mostrar_diccionario(lista_con_diccionarios):
    """(uso de funciones,diccionarios, listas,ciclos for)
    recibe: lista con diccionarios creados 
    Con un ciclo for se entra en los elementros de lista con diccionarios\
    y se entra a cada llave del diccionario para que imprima la llave ":"\
    más el valor de la llave al final de los datos de un diccionario salte\
    un espacio para imprimir los datos del siguiente usuario.
    devuelve: no devuelve nada ya que imprime los valores en la función.
    """ 
    for i in lista_con_diccionarios:
        for llave in i:
            print(llave + ": " + str(i[llave]))
        print("\n")

"""
============= Parte principal del programa =============
"""

"""
Como el programa se va a repetir hasta que un usuario decida terminaro\
se utuliza un ciclo while y se declara una variable que inicia el código
"""

ban=1

lista_con_diccionarios=[]

while ban==1:
    #Bienvenida al programa
    print("Hola bienvenido a este programa.")
    print("Aquí podrás convertir tus unidades de una manera fácil y rápida.")
    
    nombre=input ("Para continuar ingresa tu nombre completo:\n")
    comprobar_nombre(nombre)
    
    edad=int(input("¿Cuántos años tienes?\n"))
    comprobar_edad(edad)

    correo=input("Ingresa tu correo electrónico:\n")
    verificar_correo(correo)

    cantidad_c=int(input("¿Cuántas converciones vas a realizar?\n"))
    
    #Creación de listas para guardar los resultados de las conversiónes
    respuestas_lista_temp=[]
    respuestas_lista_med=[]
    
    """
    Uso de for para que repita el programa dependiendo cuantas conversiones\
    quiso hacer el usuario
    """
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





        
