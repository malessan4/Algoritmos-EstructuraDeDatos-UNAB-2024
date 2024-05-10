Algoritmo Ascensor
	
	Definir piso_actual Como Entero
	Definir piso_destino Como Entero
	
	Escribir "Ingrese el piso actual del ascensor "
	Leer piso_actual
	
	Escribir "Ingrese al piso de destino "
	Leer piso_destino
	
	si piso_destino = piso_actual Entonces
		Escribir  "Ya estas en el piso ", piso_destino
	FinSi


	si piso_destino > piso_actual Entonces
		Mientras piso_actual < piso_destino Hacer
			piso_actual <- piso_actual + 1
			Escribir "Subiendo al piso" , piso_actual
		FinMientras
		Escribir "LLegaste al piso ", piso_destino
	FinSi
	
	si piso_destino < piso_actual Entonces
		Mientras piso_actual > piso_destino Hacer
			piso_actual <- piso_actual - 1
			Escribir "Bajando al piso " , piso_actual
		FinMientras
		Escribir "LLegaste al piso ", piso_destino
	FinSi
	

FinAlgoritmo
