import numpy as np
datos=np.array([10,2,11,8,20])
datos2=np.array([[4,8,-1],[5,3,11]])
print(datos[0]) #10
print(datos2[1][1]) #3

print(datos2[datos2>0])
print(np.extract(datos2>0,datos2))

""" for fila in datos2:
    for celda in fila:
        print(celda)


a1=np.array([200,120,30])
a2=np.array([130,50,85])
suma=np.add(a1,a2)

print(np.average(suma))

edades=np.array([23,34,18,22,67,45,31])
print(f"Edad mayor: {np.amax(edades)}")
print(f"Posición del mayor: {np.argmax(edades)}")
print(f"Posición del menor: {np.argmin(edades)}")
a1=np.array([[3,2,7],[9,4,1]]) 
print(np.sort(a1)) #[[2 3 7] [1 4 9]] 
#esto es una ordenación de mayor a menor 
print(-np.sort(-a1)) #[[7 3 2]   [9 4 1]]  """