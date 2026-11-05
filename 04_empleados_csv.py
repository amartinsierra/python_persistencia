import csv
"""
with open("empleados.csv","r") as f:
    next(f) #se salta la primra fila
    datos=csv.reader(f,delimiter=",")
    for row in datos:
        print(row)
with open("empleados.csv","r") as f:
    datos=csv.DictReader(f)
    for row in datos:
        print(row)
with open("empleados.csv","r") as f:
    datos=list(csv.reader(f))
    print(datos)
with open("empleados.csv","r") as f:
    datos=list(csv.DictReader(f))
    print(datos)
"""
#solicita la introudcción de un departamento y te muestra
#los nombres de las personas de ese deprtamento
dep=input("Introduce departamento")
with open("empleados.csv","r") as f:
    datos=csv.DictReader(f)
    for emp in datos:
        if emp["departamento"]==dep:
            print(emp["empleado"])
#nombre del empleado con mayor salario
with open("empleados.csv","r") as f:
    lista_empleados=list(csv.DictReader(f))
    empleado_max=max(lista_empleados,key=lambda e:e["salario"])
    print(f"El empleado {empleado_max["empleado"]} gana {empleado_max["salario"]}")