import polars as pl

df = pl.read_csv("../ventas_tiendas.csv")

def tiendas():
    return df["nombre_tienda"].unique().to_list()

def meses():
    return df["mes"].unique().to_list()

#----# funciones relacionadas al 1er cuadro #----#
def datos_tabla_tienda(tienda):
    return df.filter(pl.col("nombre_tienda") == tienda).to_dicts()

def datos_tienda(tienda):
    return df.filter(pl.col("nombre_tienda") == tienda).select(pl.col("facturacion").sum().alias("facturacion_total"),
                                                               pl.col("gastos_personal").sum().alias("gastos_totales")).to_dicts()
def mes_mayor_facturacion(tienda):
    return df.filter(pl.col("nombre_tienda") == tienda).sort(by="gastos_personal", descending=True).row(0)

#----# funciones relacionadas al 2do cuadro #----#
def datos_tabla_mes(mes):
    return df.filter(pl.col("mes") == mes).to_dicts()

def media_facturacion(mes):
    return df.filter(pl.col("mes") == mes).select(pl.col("facturacion").mean().alias("facturacion_media")).to_dicts()

def mayor_gasto_personal(mes):
    return df.filter(pl.col("mes") == mes).sort(by="gastos_personal", descending=True).row(0) 