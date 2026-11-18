import polars as pl
import streamlit as st


def cargar_datos():

    alumnos = pl.read_csv("alumnos.csv")
    notas = pl.read_csv("notas.csv")

    datos = notas.join(
        alumnos,
        on="id_alumno",
        how="inner"
    )

    return datos


def obtener_cursos():

    datos = cargar_datos()

    return sorted(datos["curso"].unique().to_list())


def obtener_asignaturas():

    datos = cargar_datos()

    return sorted(datos["asignatura"].unique().to_list())


def obtener_grupos():

    datos = cargar_datos()

    return sorted(datos["grupo"].unique().to_list())


def obtener_evaluaciones():

    datos = cargar_datos()

    return sorted(datos["evaluacion"].unique().to_list())
#a partir de los filtros recibidos, filtramos el dataframe global
#eta función será llamada por las demás
def obtener_datos_filtrados(curso, asignatura, evaluacion, grupo):

    resultado =  cargar_datos()

    if curso != "Todos":
        resultado = resultado.filter(
            pl.col("curso") == curso
        )

    if asignatura != "Todas":
        resultado = resultado.filter(
            pl.col("asignatura") == asignatura
        )

    if evaluacion != "Todas":
        resultado = resultado.filter(
            pl.col("evaluacion") == evaluacion
        )

    if grupo != "Todos":
        resultado = resultado.filter(
            pl.col("grupo") == grupo
        )

    return resultado

def obtener_indicadores(curso, asignatura, evaluacion, grupo):

    datos = obtener_datos_filtrados(
        curso, asignatura, evaluacion, grupo
    )

    indicadores = datos.select(
        pl.col("id_alumno").unique().count().alias("alumnos"),
        pl.col("nota").mean().alias("media"),
        pl.col("nota").max().alias("maxima"),
        pl.col("nota").min().alias("minima"),
        (
            (pl.col("nota") >= 5).mean() * 100
        ).alias("porcentaje_aprobados")
    )
    return indicadores.row(0,named=True) ##devuelve los indicadores en un diccionario
