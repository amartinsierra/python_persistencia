import pandas as pd
dt=pd.read_csv("ventas_tiendas.csv")
""" tienda=input("Introduce el nombre de la tienda: ")


dtquery=dt.query("nombre_tienda==@tienda")
#dtquery=dt[dt["nombre_tienda"]==tienda]
print(f"La facturación total de la tienda {tienda}  es {dtquery["facturacion"].sum()}") """

#mostrar mayor gasto de personal de todas las empresas
dfgrupo=dt.groupby("nombre_tienda").agg(gastos_personal=("gastos_personal","sum"))
print(dfgrupo["gastos_personal"].max())

print(dt.groupby("nombre_tienda")["gastos_personal"].sum().max()) 

tienda=input("Introduce el nombre de la tienda: ")

dtquery=dt.query("nombre_tienda==@tienda")
print(dtquery)

print("El mes con mayor facturación es: ",  dtquery
      .sort_values(by="facturacion",ascending=False) #ordena de mayor a menor
      .iloc[0] #se queda con el primer registro del dataframe ordenado
      .to_dict()["mes"]) #convierte en un diccionario y extrae la propiedad deseada

#Nombre de la tienda más antigua
print("Tienda más antigua: ",dt.sort_values(by="año_apertura", ascending=True)
      .iloc[0]
      .to_dict()["nombre_tienda"]) 

""" edad_vieja=dt["año_apertura"].min() #el año
condicion_vieja=dt["año_apertura"]==edad_vieja #filtramos
tienda_vieja=dt[condicion_vieja] #filas
nombre_tienda_vieja=tienda_vieja["nombre_tienda"].unique()[0] #usamos unique para que no se repita!!! (si no, se me repite 6 veces)
print(f"La tienda más antigua es {nombre_tienda_vieja},inaugurada en el año {edad_vieja}")  """
