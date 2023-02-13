"""Ejercicio 11: Salario y horas extra

El cálculo de una nómina tiene en cuenta el salario bruto asociado a las horas «normales» que debe hacer el empleado y las horas «extra» trabajadas en el mes. Las horas extra se remuneran según las siguientes normas administrativas:
Tarifa por hora aumentada en un 125 % para las horas entre la 36.ª y la 43.ª.
Tarifa por hora aumentada en un 150 % para las horas a partir de la 44.ª.
El aumento se realiza sobre la tarifa por hora normal, calculado a partir del salario mensual bruto para un año de 52 semanas repartidas en 12 meses, sobre la base de 35 horas trabajadas por semana.
Escribir el algoritmo que calcula el importe de las horas extra que hay que pagar, a partir del salario mensual bruto y de la cantidad de horas extra.
Se podrá suponer que el cálculo siempre se usa para una cantidad de horas superior a 8. El problema general supone el estudio previo del capítulo siguiente, que trata de la alternativa."""

#EJERCICIO 11

Entrada:
salario_mensual_bruto: int
horas_extra: int

Precondiciones:
salario_mensual_bruto > 0
horas_extra >= 0

Realizacion:
salario_hora = salario_mensual_bruto / 35
salario_extra = 0
if horas_extra <= 7:
    salario_extra=horas_extra*salario_hora*1.25
else:
    salario_extra=7*salario_hora*1.25+(horas_extra-7)*salario_hora*1.5

Resultado:
salario_extra: int #Salario extra

Postcondiciones:
salario_extra >= 0
