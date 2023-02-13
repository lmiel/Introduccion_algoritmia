"""Ejercicio 8: Porcentajes, IVA e inversiones
1. Escribir un algoritmo que calcula el precio con todos los impuestos incluidos (TII) para un precio sin impuestos y un porcentaje de IVA dado.

2. Escribir un algoritmo que calcula el importe de los intereses generados por un capital invertido a un interés dado durante un tiempo dado, expresado en meses."""
#EJERCICIO 7 PARTE I

Entrada:
precio_sin_IVA: int
porcentaje_IVA: int

Precondiciones:
precio_sin_IVA > 0
0<= porcentaje_IVA <= 100

Realizacion:
precio_con_IVA = precio_sin_IVA + (precio_sin_IVA * porcentaje_IVA / 100)

Resultado:
precio_con_IVA: int #Precio con IVA incluido

Postcondiciones:
precio_con_IVA > precio_sin_IVA

#EJERCICIO 7 PARTE II

Entrada:
capital_inicial: int
interes_mensual: int
meses: int

Precondiciones:
capital_inicial > 0
0 <= interes_mensual <= 100
meses > 0

Realizacion:
capital_final= capital_inicial*(1 + interes_mensual / 100)^meses

Resultado:
capital_final: int #Capital final tras el periodo de tiempo

Postcondiciones:
capital_final > capital_inicial

