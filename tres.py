#crear un menu de dos opciones
# el primero que me pregunte los pueblos y el segundo que los muestre
# 
contador =0
print("************Menu***********")
print("1. Agregar pueblos")
print("2. Mostrar ruta")
print("3. Salir")
pueblos=[]
while (contador!=3):
    pueblo={}
    contador=int(input("Ingrese una opcion del Menu"))
    if(contador==1):
        print("ingresando pueblo: ")
        pueblo["nombre"]=input("Ingrese un pueblo a donde viajas")
        pueblo["distancia"]=int(input("Ingrese a que distancia esta"))
        pueblo["poblacion"]=input("Ingrese la poblacion del pueblo")
        pueblos.append(pueblo)
    elif(contador==2):
        print("Monstrando Rutas")
        print(pueblos)
    elif(contador==3):
        print("hasta Pronto...")
        break
    else:
        print("ingrese una opcion valida:")
