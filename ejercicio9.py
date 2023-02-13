"""Ejercicio 9: Media aritmética ponderada
1. Escribir un algoritmo que calcula la media aritmética de tres números dados.

2. La misma pregunta para una media ponderada cuando se dan los números y los coeficientes de ponderación."""

#EJERCICIO 9 PARTE I

Entrada:
numero1: int
numero2: int
numero3: int

Precondiciones:
#No hay precondiciones

Realizacion:
media_aritmetica=(numero1+numero2+numero3)/3

Resultado:
media_aritmetica: float #Media aritmetica de los tres numeros

Postcondiciones:
#No hay postcondiciones

#EJERCICIO 9 PARTE II

Entrada:
numero1: float
numero2: float
numero3: float
coeficiente1: float
coeficiente2: float
coeficiente3: float

Precondiciones:
0 <= coeficiente1 <= 1
0 <= coeficiente2 <= 1
0 <= coeficiente3 <= 1
coeficiente1 + coeficiente2 + coeficiente3 = 1

Realizacion:
media_ponderada=(numero1*coeficiente1+numero2*coeficiente2+numero3*coeficiente3)

Resultado:
media_ponderada: float #Media ponderada de los tres numeros

Postcondiciones:
#No hay postcondiciones
