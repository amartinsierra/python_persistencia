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
