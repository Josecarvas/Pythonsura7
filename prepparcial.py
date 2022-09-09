#crear un menu de dos opciones
# el primero que me pregunte los pueblos y el segundo que los muestre
# 
x =0
print("************Menu***********")
print("1. Agregar empanadas")
print("2. Mostrar empanadas")
print("3. Salir")
Empanadas=[]

while (x!=3):
    opcion={}
    ingredientes=[] #ingreso este otro dentro del While porque es necesario que no alamacene lo de otras empanadas
    x=int(input("Ingrese una opcion del Menu"))
    if(x==1):
        print("ingresando Empanada: ")
        opcion["nombre"]=input("Ingrese nombre de la empanada ")
        for i in range(3):
            ingredientes.append(input(f"Ingrese el ingrediente de la empanada {i+1} :"))
            opcion["ingredientes"]=ingredientes
        opcion["precio"]=int(input("Ingrese el valor de la empanada $ "))
        Empanadas.append(opcion)
    elif(x==2):
        print("Mostrando las empanadas.... ")
        print(Empanadas)
    elif(x==3):
        print("hasta Pronto...")
        break
    else:
        print("ingrese una opcion valida:")
