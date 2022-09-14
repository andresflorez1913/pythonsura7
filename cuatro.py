# menu empanadas inteligentes, 1 agregar empnada
contador=0
empanadas=[]

print("1. Aregar empanada ")
print("2. Mostrar Empanada")
print("3. salir")
while(contador!=3):
    empanada={}
    ingredientes=[]
    contador=int(input("Digite la opcion"))
    if(contador==1):
      empanada['nombre']=input("ingrese nombre de la empanada ")
      for i in range (3):
        ingredientes.append(input("Digite el ingrediente ", i+1))
        empanada['ingredientes']=ingredientes
        empanada['precio']=int(input("ingrese el precio: $"))
        empanadas.append(empanada)
        print(Agregando empanada)
    elif(contador==2):
        print("Mostrando empanada")
        print(empanadas)
    elif(contador==3):
        print("salir")
        break
    else:
        print("opcion invalida")
        