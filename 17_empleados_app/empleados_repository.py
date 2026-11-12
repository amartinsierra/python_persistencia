import pymongo as py
def crear_conexion():
    url="mongodb://localhost:27017"
    return py.MongoClient(url)

def nuevo_empleado(empleado,edad,salario,departamento):
    serv=crear_conexion()
    col_empleados=serv.empresa.empleados
    col_empleados.insert_one({"empleado":empleado,"edad":edad,"salario":salario,"departamento":departamento})
    serv.close()

def departamentos():
    serv=crear_conexion()
    col_empleados=serv.empresa.empleados
    departamentos=list(set(map(lambda e:e["departamento"],col_empleados.find())))
    serv.close()
    return departamentos
def empleados_por_departamento(departamento):
    serv = crear_conexion()
    col_empleados = serv.empresa.empleados
    empleados = list(col_empleados.find({"departamento":departamento}))
    serv.close()
    return empleados
def empleados_por_salarios(min,max):
    serv = crear_conexion()
    col_empleados = serv.empresa.empleados
    empleados = list(col_empleados.find({"salario":{"$gte":min,"$lte":max}}))
    serv.close()
    return empleados

