import mysql.connector as con
def crear_conexion():
    return con.connect(host="localhost",
               user="root",
               password="root",
               port=3306,
               database="mundo")
    
def borrar_tablas():
    db=crear_conexion()
    cursor=db.cursor()
    cursor.execute("delete from continentes")
    cursor.execute("delete from paises")
    db.commit()
    db.close()
def crear_continentes(continentes):  #["Asia","Americas",....]
    sql_insert="insert into continentes(continente) values(%s)"
    db=crear_conexion()
    cursor=db.cursor()
    lista_tuplas=[(c,) for c in continentes] #crea una lista de tuplas del tipo [("Asia",),("Europe",)]
    cursor.executemany(sql_insert,lista_tuplas)
    db.commit()
    db.close()
def devolver_continentes():
    sql="select * from continentes"
    db=crear_conexion()
    cursor=db.cursor(dictionary=True)  
    cursor.execute(sql)  
    resultado=cursor.fetchall()
    db.close()
    return resultado
def crear_paises(paises): #[{"pais":"pais1","poblacion":333,"bandera":"http:...","idContinente":2},...]
    sql_insert="insert into paises(pais,poblacion,bandera,idContinente) values(%s,%s,%s,%s)"
    db=crear_conexion()
    cursor=db.cursor()
    #lista_tuplas=[(p["pais"],p["poblacion"],p["bandera"],p["idContinente"]) for p in paises]
    lista_tuplas=[tuple(p.values()) for p in paises]
    cursor.executemany(sql_insert,lista_tuplas)
    db.commit()
    db.close()
def paises_por_continente(id_continente):
    sql="select * from paises where idContinente=%s"
    db=crear_conexion()
    cursor=db.cursor(dictionary=True)
    cursor.execute(sql)
    resultado=cursor.fetchall()
    db.close()
    return resultado