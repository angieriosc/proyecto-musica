# Proyecto-TC1028

##  Music pop quiz 

La música, considerada por muchos  “el arte que consiste en dotar a los sonidos y los silencios de una cierta organización” (Pérez, 2021), es algo que forma parte de la vida diaria de muchas personas . Muchos escuchamos música mientras manejamos, cocinamos, trabajamos o simplemente para relajarse después de un día pesado. Es bien cierto que el origen de la música es un misterio para la humanidad, sin embargo sabemos que ha existido por mucho tiempo. La música nos puede transmitir cosas que son dificiles de explicar por eso muchas personas consideran que la música "es un lenguaje hecho arte, más expresivo si cabe que la propia lengua" (López, A).

Este programa es un juego en el que el usuario podrá probar sus conocimientos de musica, dentro del juego habrán diferentes tipos de test para 3 géneros de música; pop (latino e ingles), musicales de Broadway y Rock. Cada uno contará con diferentes tipos de preguntas como adivina el artista, adivina la canción y completa la letra. 

Decidi crear este programa ya que creo que la música es algo que todos o una gran parte de la humannidad difruta escuchar. Es un proyecto interesante ya que permite aprender de una manera divertida y al hacerlo en un formato de juego hace que el usuario disfrute más contestar las preguntas a que si fuera un simple test.


Referencias: 


Pérez, J & Gardey, A (2021) Definición de Música Recuperado de: https://definicion.de/musica/ 

Galindo, M (s/f) El origen de la música. Recuperado de: https://www.musicaeduca.es/revista/colaboradores/4012-el-origen-de-la-musica

López, A (s/f) La música como lenguaje. Recuperado de: http://www.filomusica.com/filo82/lenguaje.html

## Pseudocódigo

	Establecer funciones para abrir y cerrar ventanas (Abra multiples ventanas dentro del programa)

	Crear una pagina principal en la que muestre los diferentes géneros de música para que el usuario elija 


	Sub página Pop en la que muestre botón de Pop Latino y botón de Ingles 
	 Pagina de pop latino
	  Botón menu 
	  Crear variable de puntaje - Puntaje_pe = 0
              
		Pregunta 1 : ¿Qué banda canta la canción “Alejate de Mi”? A- Mana  B-El Tri C-Camila D- Moderato
		respuesta1_pe= lo que ingrese el usuario 
		 Mientras la respuesta no sea A o B o C o D (Validador de respuestas)
                	Por favor contestar con A,B,C y D solamente	
		si la respuesta1_pe = C
			puntaje_pe = puntaje_pe  + 1
		si no puntaje_pe  = puntaje_pe 

		Pregunta 2 : ¿Qué canción pertenece a Ha-ash”? A- Ex de verdad  B- Tu de que vas C- Perdón D- Espacio Sideral
		respuesta2_pe= lo que ingrese el usuario 
		 Mientras la respuesta no sea A o B o C o D (Validador de respuestas)
                	Por favor contestar con A,B,C y D solamente	
		si la respuesta2_pe = A
			puntaje_pe = puntaje_pe  + 1
		si no puntaje_pe  = puntaje_pe 

		Pregunta 3 : Completa la letra Si tu te vas y yo me voy _____ “    “A-  que  vamos  a hacer  B-  es el fin C- a mi casa D- con quién se queda el perro
		respuesta3_pe= lo que ingrese el usuario 
		 Mientras la respuesta no sea A o B o C o D (Validador de respuestas)
                	Por favor contestar con A,B,C y D solamente	
		si la respuesta3_pe = D
			puntaje_pe = puntaje_pe  + 1
		si no puntaje_pe  = puntaje_pe 

		Pregunta 4 : ¿Quién ganó el premio Grammy al mejor álbum de pop latino en 2017 ? A- Luis Miguel B- Shakira C- Bad Bunny D- Jessey Joy 
		respuesta4_pe= lo que ingrese el usuario 
		 Mientras la respuesta no sea A o B o C o D (Validador de respuestas)
                	Por favor contestar con A,B,C y D solamente	
		si la respuesta_pe = A
			puntaje_pe = puntaje_pe  + 1
		si no puntaje_pe  = puntaje_pe 

		Pregunta 5 : ¿Qué artista canta la canción “Por ti”? A- Yuridia B- Rio roma C- Belanova D-Timbiriche
		respuesta= lo que ingrese el usuario 
		 Mientras la respuesta no sea A o B o C o D (Validador de respuestas)
                	Por favor contestar con A,B,C y D solamente	
		si la respuesta = C
			puntaje_pe = puntaje_pe  + 1
		si no puntaje _pe = puntaje_pe 

	       calificacion_pe = puntaje_pe /5 * 100
		Mostrar calificacion_pe
			si calificacion_pe = 20 mostrar 1 estrella
			si calificacion_pe = 40 mostrar 2 estrellas
			si calificacion_pe = 60 mostrar 3 estrellas
			si calificacion_pe = 80 mostrar 4 estrellas
			si calificacion_pe = 100 mostrar 5 estrellas
		
		
		
		
				
	Pagina de pop ingles 
		Crear variable de puntaje - Puntaje_pi = 0
              
		Pregunta 1 : ¿Qué banda canta la canción “The Scientist”? A- The Beatles  B-Coldplay C-Queen D- Imagine Dragons
		respuesta1_pi = lo que ingrese el usuario 
		 Mientras la respuesta no sea A o B o C o D (Validador de respuestas)
                	Por favor contestar con A,B,C y D solamente	
		si la respuesta1_pi = B
			puntaje_pi= puntaje_pi + 1
		si no puntaje_pi = puntaje_pi

		Pregunta 2 : ¿Qué canción pertenece a Shawn Mendes”? A- Rolling in the deep  B- Stay C- Mercy D- Golden
		respuesta2_pi= lo que ingrese el usuario 
		 Mientras la respuesta no sea A o B o C o D (Validador de respuestas)
                	Por favor contestar con A,B,C y D solamente	
		si la respuesta2_pi = C
			puntaje_pi= puntaje_pi + 1
		si no puntaje_pi = puntaje_pi

		Pregunta 3 : Completa la letra Go home, get ahead light speed internet I don’t want to talk about “  “ A- the past  B- last summer C- 				      that D- the way that it was 
		respuesta3_pi= lo que ingrese el usuario 
		 Mientras la respuesta no sea A o B o C o D (Validador de respuestas)
                	Por favor contestar con A,B,C y D solamente	
		si la respuesta3_pi = D
			puntaje_pi= puntaje_pi + 1
		si no puntaje_pi = puntaje_pi

		Pregunta 4 : ¿Quién ganó el premio Grammy al mejor álbum de pop vocal en 2022 ? A- Olivia Rodrigo B- Dua Lipa C- Doja Cat D-Billie Eilish
		respuesta4_pi= lo que ingrese el usuario 
		 Mientras la respuesta no sea A o B o C o D (Validador de respuestas)
                	Por favor contestar con A,B,C y D solamente	
		si la respuesta4_pi = A
			puntaje_pi = puntaje_pi + 1
		si no puntaje_pi = puntaje_pi

		Pregunta 5 : ¿Qué artista canta la canción “Happier than ever”? A-  Demi Lovato B- Selena Gomez C- Katy Perry D-Billie Eilish
		respuesta5_pi= lo que ingrese el usuario 
		 Mientras la respuesta no sea A o B o C o D (Validador de respuestas)
                	Por favor contestar con A,B,C y D solamente	
		si la respuesta5_pi = D
			puntaje_pi = puntaje_pi + 1
		si no puntaje_pi = puntaje_pi


	       calificación_pi = puntaje_pi/5 * 100
		Mostrar calificacion_pi
			si calificacion_pi = 20 mostrar 1 estrella
			si calificacion_pi = 40 mostrar 2 estrellas
			si calificacion_pi = 60 mostrar 3 estrellas
			si calificacion_pi = 80 mostrar 4 estrellas
			si calificacion_pi = 100 mostrar 5 estrellas
	
		
						

	Sub página Musicales

	Crear variable de puntaje - Puntaje_m = 0
              
		Pregunta 1 : ¿De qué musical es la canción “For Forever”? A- Beetlejuice  B- Rent C - Dear Evan Hansen D- Mean Girls
		respuesta_1m= lo que ingrese el usuario 
		 Mientras la respuesta no sea A o B o C o D (Validador de respuestas)
                	Por favor contestar con A,B,C y D solamente	
		si la respuesta_1m = C
			puntaje_m= puntaje_m + 1
		si no puntaje_m = puntaje_m

		Pregunta 2 : ¿Qué canción pertenece al musical “Be more chill”? A- Michael in the bathroom  B- Burn C- Meant to be yours  D- Dead mom
		respuesta_2m= lo que ingrese el usuario 
		 Mientras la respuesta no sea A o B o C o D (Validador de respuestas)
                	Por favor contestar con A,B,C y D solamente	
		si la respuesta_2m = A
			puntaje_m= puntaje_m + 1
		si no puntaje_m = puntaje_m

		Pregunta 3 : Completa la letra Honey what you’re waiting for? Shut up ______  A- now  past  B-  Veronica  C- please  D- Heather
		respuesta_3m = lo que ingrese el usuario 
		 Mientras la respuesta no sea A o B o C o D (Validador de respuestas)
                	Por favor contestar con A,B,C y D solamente	
		si la respuesta_3m = D
			puntaje_m= puntaje_m + 1
		si no puntaje_m = puntaje_m

		Pregunta 4 : ¿Cuál personaje canta “One Last time” en Hamilton? A- Eliza  B- George Washington C- Alexander Hamilton  D- Aaron Burr
		respuesta_4m= lo que ingrese el usuario 
		 Mientras la respuesta no sea A o B o C o D (Validador de respuestas)
                	Por favor contestar con A,B,C y D solamente	
		si la respuesta_4m = B
			puntaje_m = puntaje_m + 1
		si no puntaje_m = puntaje_m

		Pregunta 5 : ¿Quién ganó el premio Tony al mejor musical en 2008? A-  Wicked B- Crybaby C- Matilda D-In the Heights
		respuesta_5m= lo que ingrese el usuario 
		 Mientras la respuesta no sea A o B o C o D (Validador de respuestas)
                	Por favor contestar con A,B,C y D solamente	
		si la respuesta_5m = D
			puntaje_m = puntaje_m + 1
		si no puntaje_m = puntaje_m 

	       calificacio_mn = puntaje_m/5 * 100
		Mostrar calificacion_m
			si calificacion_m = 20 mostrar 1 estrella
			si calificacion_m = 40 mostrar 2 estrellas
			si calificacion_m = 60 mostrar 3 estrellas
			si calificacion_m = 80 mostrar 4 estrellas
			si calificacion_m = 100 mostrar 5 estrellas
	

	Sub página Rock
	
	Crear variable de puntaje - Puntaje_m = 0
          
		Pregunta 1 : ¿De qué banda es la canción “Under Pressure”? A- Queen  B- Kiss - Rolling Stones D- Beatles
		respuesta_1r= lo que ingrese el usuario 
		 Mientras la respuesta no sea A o B o C o D (Validador de respuestas)
			Por favor contestar con A,B,C y D solamente	
		si la respuesta_1r = A
			puntaje_r= puntaje_r + 1
		si no puntaje_r = puntaje_r

		Pregunta 2 : ¿Qué canción pertenece a la banda “Aerosmith”? A- All in black  B- Satisfaction C- Dream On  D- Let it be 
		respuesta_2r= lo que ingrese el usuario 
		 Mientras la respuesta no sea A o B o C o D (Validador de respuestas)
			Por favor contestar con A,B,C y D solamente	
		si la respuesta_2r = B
			puntaje_r= puntaje_r + 1
		si no puntaje_r = puntaje_r

		Pregunta 3 : Completa la letra Is this the real life? Is this just ______ ?  A- a dream  B- my imagination C- me  D- fantasy
		respuesta_3r = lo que ingrese el usuario 
		 Mientras la respuesta no sea A o B o C o D (Validador de respuestas)
			Por favor contestar con A,B,C y D solamente	
		si la respuesta_3r = D
			puntaje_r= puntaje_ + 1
		si no puntaje_r = puntaje_r

		Pregunta 4 : ¿Cuál banda canta “Creep” ? A- Radiohead  B- AC/DC C- The White Stripes  D- Nirvana
		respuesta_4r= lo que ingrese el usuario 
		 Mientras la respuesta no sea A o B o C o D (Validador de respuestas)
			Por favor contestar con A,B,C y D solamente	
		si la respuesta_4r = A
			puntaje_r = puntaje_r + 1
		si no puntaje_r = puntaje_r

		Pregunta 5 : ¿Quién ganó el premio Grammy al mejor album de rock en 2013? A- Foo fighters B- U2 C- Led Zeppelin D- Green Day
		respuesta_5r= lo que ingrese el usuario 
		 Mientras la respuesta no sea A o B o C o D (Validador de respuestas)
			Por favor contestar con A,B,C y D solamente	
		si la respuesta_5r = D
			puntaje_r = puntaje_r + 1
		si no puntaje_r = puntaje_r

	       calificacion_r = puntaje_r/5 * 100
		Mostrar calificacion
			si calificacion_r = 20 mostrar 1 estrella 
			si calificacion_r = 40 mostrar 2 estrellas
			si calificacion_r = 60 mostrar 3 estrellas
			si calificacion_r = 80 mostrar 4 estrellas
			si calificacion_r = 100 mostrar 5 estrellas
	
	Todas las estrellas que se muestren serán imagenes

