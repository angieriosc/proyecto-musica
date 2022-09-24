# Proyecto-TC1028

## Convert

Una unidad de medida es un valor designado que se "usa para medir la magnitud física de un objeto, sustancia o fenómeno" (Unidades de medida, 2019). Las unidades de medida tienen una gran importancia en nuestra vida ya que  permiten calcular cosas como la longitud, la masa, la capacidad, la superficie, el volumen, la temperatura, ó el tiempo. La temperatura es una medida relativa, las escalas que se basan en puntos de referencia deben ser usadas para medir la temperatura con precisión. Elegí las 3 unidades de temperatura más conocidas ya que las escalas de temperatura "nos permiten medir la energia del calor de una manera ligeramente diferente"(Martha, 2003). 

Este programa es un convertidor de unidades en el que el usuario podrá saber la conversión de diferentes medidas de temperatura en Kelcin, Celsius, Fahrenheit y la longitud del sistema internacional de medidas y el sistema ingles. Esto facilitara los procesos al usuario de manera rápida y eficaz.

Decidi crear este programa ya que creo que las unidades de medida forman parte de nuestra vida, y existen ocasiones en las que no estamos familiarizados con el sistema de unidades inglés. Por lo qué, un convertidor de unidades sería una herramienta muy útil. 

Referencias: 

Unidades de medida. (2019, 8 agosto). Significados. Recuperado 22 de septiembre de 2022, de https://www.significados.com/unidades-de-medida/
Day,M & Carphi,A (2003)	Temperatura. Recuperado 22 de septiembre de 2022, de https://www.visionlearning.com/es/library/Ciencias-Generales/3/Temperatura/48

## Pseudocódigo
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

print-("Hola bienvenido a este programa. Aquí podrás convertir tus unidades de una manera fácil y rápida.")
Para continuar ingresa tu nombre completo;
Nombre=input()

Mientras que la respuesta no sea mayor a 2 caracteres:

	Dato invalido 
	Para continuar ingresa tu nombre completo
	Nombre=input 

edad=input("Ingresa tu edad:")

Mientras que la respuesta no sea menor a 113 ni mayor que 0: 

	Dato invalido 
	Ingresa tu edad:
	edad=input 

Elige una opción para continuar (contestar solo con letras)
¿Qué quieres convertir?
A-Temperatura
B- Medidas de longitud 
respuesta_1=input
Mientras que la respuesta no sea A o B:
	Respuesta invalida 
	¿Qué quieres convertir?
	A-Temperatura
	B- Medidas de longitud 
	respuesta_1=input

Si la respuesta es igual a "a":
	Elige que deseas convertir 
	1- centímetros a pulgadas
	2- pulgadas a centímetros 
	3- pies a metros 
	4- metros a pies
	5- yardas a metros
	6- metros a yardas
	7- millas a kilometros
	8- kilómetros a millas 
	
	Mientras que la respuesta no sea menor o igual a 8 ni mayor que 0 
		Respuesta invalida, favor de contestar con 1,2,3,4,5,6,7 ó 8.
		Elige que deseas convertir: 
		1- centímetros a pulgadas
		2- pulgadas a centímetros 
		3- pies a metros 
		4- metros a pies
		5- yardas a metros
		6- metros a yardas
		7- millas a kilómetros
		8- kilómetros a millas 

	Si la respuesta es 1:
		Ingresa los centímetros=input
		función cm_a_in (cm)
		la respuesta es: 
		
	Si la respuesta es 2:
		Ingresa las pulgadas=input
		función in_a_cm (in)
		la respuesta es: 

	Si la respuesta es 3:
		Ingresa los pies=input
		función ft_a_m (ft)
		la respuesta es: 

	Si la respuesta es 4:
		Ingresa los metros=input
		función m_a_ft (m)
		la respuesta es: 

	Si la respuesta es 5:
		Ingresa las yardas=input
		función yd_a_m (yd)
	        la respuesta es: 

	Si la respuesta es 6:
		Ingresa los metros=input
		función m_a_yd (m)
		la respuesta es: 

	Si la respuesta es 7:
		Ingresa los millas=input
		función mi_a_km (mi)
		la respuesta es: 

	Si la respuesta es 8:
		Ingresa los km=input
		función km_a_mi (km)
		la respuesta es: 

Si la respuesta es igual "b":

	Elige que deseas convertir 
	1- Celcius a Kelvin
	2- Kelvin a Celcius
	3- Fahrenheit a Celsius
	4- Celsius a Fahrenheit
	5- Kelvin a Fahrenheit
	6- Fahrenheit a Celsius
	
	Mientras que la respuesta no sea menor o igual a 6 ni mayor que 0 
		Respuesta invalida, favor de contestar con 1,2,3,4,5, ó 6
		Elige que deseas convertir: 
		1- Celcius a Kelvin
		2- Kelvin a Celcius
		3- Fahrenheit a Celsius
		4- Celsius a Fahrenheit
		5- Kelvin a Fahrenheit
		6- Fahrenheit a Celsius

	Si la respuesta es 1:
		Ingresa los grados celsius=input
		función ce_a_ke (celsius)
		la respuesta es: 

	Si la respuesta es 2:
		Ingresa los grados kelvin=input
		función ke_a_ce (kelvin)
		la respuesta es: 

	Si la respuesta es 3:
		Ingresa los grados fahrenheit=input
		función fa_a_ce (fahrenheit)
		la respuesta es: 

	Si la respuesta es 4:
		Ingresa los grados celsius=input
		función ce_a_ke (celsius)
		la respuesta es: 

	Si la respuesta es 5:
		Ingresa los grados kelvin=input
		función ke_a_fa (kelvin)
		la respuesta es: 

	Si la respuesta es 6:
		Ingresa los grados fahrenheit=input
		función fa_a_ke (fahrenheit)
		la respuesta es: 





