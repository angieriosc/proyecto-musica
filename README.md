# Proyecto-TC1028

##  Music

Este programa es un juego en el que el usuario podrá probar sus conocimientos de musica, dentro del juego habrán diferentes tipos de test para 3 géneros de música; pop (latino e ingles), musicales de Broadway y Rock. Cada uno contará con diferentes tipos de preguntas como adivina el artista, adivina la canción y completa la letra. 

Creo que es un proyecto interesante ya que desde hace mucho tiempo la humanidad a mostrado mucho interés por la música, y la música es algo que la mayoría de las personas habrá que le guste más un genero que otro pero sigue siendo música.

## Pseudocódigo

Establecer funciones para abrir y cerrar ventanas 

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

		Pregunta 5 : ¿Qué artista canta la canción “Happier than ever”? A-  Demi Lovato B- Selena Gomez C- Katy Perry D-Billie Eilish
		respuesta= lo que ingrese el usuario 
		 Mientras la respuesta no sea A o B o C o D (Validador de respuestas)
                	Por favor contestar con A,B,C y D solamente	
		si la respuesta = D
			puntaje_pe = puntaje_pe  + 1
		si no puntaje _pe = puntaje_pe 

	       calificacion = puntaje_pe /5 * 100
		Mostrar calificacion
			si calificacion = 20 mostrar 1 estrella
			si calificacion = 40 mostrar 2 estrellas
			si calificacion = 60 mostrar 3 estrellas
			si calificacion = 80 mostrar 4 estrellas
			si calificacion = 100 mostrar 5 estrellas
		
		
		
		
				
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


	       calificación = puntaje_pi/5 * 100
		Mostrar calificacion
			si calificacion = 20 mostrar 1 estrella
			si calificacion = 40 mostrar 2 estrellas
			si calificacion = 60 mostrar 3 estrellas
			si calificacion = 80 mostrar 4 estrellas
			si calificacion = 100 mostrar 5 estrellas
	
		
						

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

	       calificacion = puntaje_m/5 * 100
		Mostrar calificacion
			si calificacion = 20 mostrar 1 estrella
			si calificacion = 40 mostrar 2 estrellas
			si calificacion = 60 mostrar 3 estrellas
			si calificacion = 80 mostrar 4 estrellas
			si calificacion = 100 mostrar 5 estrellas
	

Sub página Rock
	
		

