#variables con eleentos del misto tipo
#lista numeros pares

numerospares =[]
#generar un ciclo wuile que de 10 vueltas
contador = 0 

while(contador<10):

    numero = int(input("ingrese un numero par"))
    if (numero % 2 == 0):
        numerospares.append(numero)
        contador=contador+1
    
for observador in numerospares:
        print(observador)