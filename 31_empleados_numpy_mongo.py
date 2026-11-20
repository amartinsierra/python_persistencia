import pymongo as py
import numpy as np
def crear_conexion():
    url="mongodb://localhost:27017"
    return py.MongoClient(url)
serv=crear_conexion()
col_empleados=serv.empresa.empleados
datos=list(col_empleados.find())
serv.close()
print(datos)

salarios=np.array([e["salario"] for e in datos])
edades=np.array([e["edad"] for e in datos])
departamentos=np.array([e["departamento"] for e in datos])

print(f"Salario medio: {np.average(salarios)}")
print(f"Edad mayor: {np.amax(edades)}")
print(f"Departamentos: {np.unique(departamentos)}")