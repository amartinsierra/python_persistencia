import polars as pl

#df = pl.read_csv("ventas_tiendas.csv")
df = pl.scan_csv("ventas_tiendas.csv")
tienda=input("Nombre de la tienda: ")
total = df.filter(pl.col("nombre_tienda") == tienda).collect()["facturacion"].sum()
print(f"Facturación total: {total} €")

#########################################
df = pl.read_csv("ventas_tiendas.csv")
fila_max_gasto = (df.group_by("nombre_tienda")
                .agg(pl.col("gastos_personal").sum())
                .sort("gastos_personal", descending=True)
                .row(0, named=True)
)
print(
    f"Tienda con mayor gasto de personal: {fila_max_gasto['nombre_tienda']}"
    f" ({fila_max_gasto['gastos_personal']})"
) 

##########################################################

mes_buscado=df.filter(pl.col("nombre_tienda")==tienda).sort("facturacion",descending=True).row(0)[1]
print(f"Mes con mayor facturación de{tienda} es {mes_buscado}")

#############################con scan########################
df = pl.scan_csv("ventas_tiendas.csv")

fila_max_gasto = (df.group_by("nombre_tienda")
                .agg(pl.col("gastos_personal").sum())
                .sort("gastos_personal", descending=True)
                .collect()
                .row(0, named=True)
)
print(
    f"Tienda con mayor gasto de personal: {fila_max_gasto['nombre_tienda']}"
    f" ({fila_max_gasto['gastos_personal']})"
) 

mes_buscado=df.filter(pl.col("nombre_tienda")==tienda).sort("facturacion",descending=True).collect().row(0)[1]
print(f"Mes con mayor facturación de{tienda} es {mes_buscado}")