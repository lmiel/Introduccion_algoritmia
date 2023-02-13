"""Ejercicio 10: Área del triángulo
1. Escribir un algoritmo que calcula el área de un triángulo del que se da la medida de un lado y la de la altura relativa a este lado.

2. ¿Se puede utilizar este algoritmo para un triángulo rectángulo si se dan las medidas de sus dos lados perpendiculares?"""

#EJERCICIO 10 PARTE I

Entrada:
lado: int
altura: int

Precondiciones:
lado > 0
altura > 0

Realizacion:
area_triangulo=(lado*altura)/2

Resultado:
area_triangulo: float #Area del triangulo

Postcondiciones:
area_triangulo > 0

#EJERCICIO 10 PARTE II

Entrada:
lado1: int
lado2: int

Precondiciones:
lado1 > 0
lado2 > 0

Realizacion:
area_triangulo=(lado1*lado2)/2

Resultado:
area_triangulo: float #Area del triangulo

Postcondiciones:
area_triangulo > 0
