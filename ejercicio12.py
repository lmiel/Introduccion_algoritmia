"""Ejercicio 12: Cuenta de depósito
Se considera las cuentas de depósitos alojadas en un banco por los clientes. Solo se permite hacer una retirada si el saldo que queda en la cuenta no es negativo.
1. Definir el tipo de datos CUENTA..
2. Definir las operaciones aplicables.
En determinadas circunstancias y para determinados clientes, la banca autoriza un descubierto limitado y temporal.
3. Volver a hacer las definiciones previas para permitir estos descubiertos."""

#EJERCICIO 12

Entrada:
cuenta: CUENTA
cantidad_ingresar: int
cantidad_retirar: int

Clase CUENTA:
saldo: int
descubierto: bool
cliente: str
ingresar_saldo(cantidad): saldo = saldo + cantidad
retirar_saldo(cantidad): 
    if saldo > cantidad:
        saldo = saldo - cantidad
    else:
        if descubierto == True:
            saldo = saldo - cantidad
        else:
            print("No se puede retirar dinero")

imprimir_saldo(): print(saldo)

#Establecemos nuestro algoritmo como ingresar y retirar dinero de la cuenta con un descubierto e imprimir el saldo
Precondiciones:
cuenta inicializada
cantidad > 0

Realizacion:
cuenta.ingresar_saldo(cantidad_ingresar)
cuenta.retirar_saldo(cantidad_retirar)
cuenta.imprimir_saldo()

Resultado:
cuenta: CUENTA con saldo actualizado

Postcondiciones:
saldo = saldo + cantidad_ingresar - cantidad_retirar





