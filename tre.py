# crear un menu de 2 opciones
contador=0
pueblos=[]
print("Enamorate de Antioquia ")
print("1. Agregar pueblos ")
print("2. Mostrar rutas ")
print("3. salir ")
while(contador !=3):
  pueblo={}
  contador=int(input("Digita una opcion"))
  if(contador==1):
    print("agregando pueblo: ")
    pueblo['nombre']=input("ingrese el nombre del pueblo: ")
    pueblo['distancia']=int(input("ingrese la distancia: "))
    pueblo['poblacion']=int(input("ingrese el nombre del pueblo: "))
    pueblos.append(pueblo)
  elif(contador==2):
    print("mostrar rutas: ")
    print(pueblos)
  elif(contador==3):
   print("saliendo: ")
   break
else:
    print("opcion invalida")
