import streamlit as st
import matplotlib.pyplot as plt

import formacion_repository as repo


st.set_page_config(
    page_title="Análisis académico",
    layout="wide"
)
st.sidebar.title("Filtros")

curso = st.sidebar.selectbox("Curso",["Todos"] + repo.obtener_cursos())

asignatura = st.sidebar.selectbox("Asignatura",["Todas"] + repo.obtener_asignaturas())

grupo = st.sidebar.selectbox("Grupo",["Todos"] + repo.obtener_grupos())

evaluacion = st.sidebar.selectbox("Evaluación",["Todas"] + repo.obtener_evaluaciones())

#Dashboard
st.title("Dashboard de rendimiento académico")
#indicadores
indicadores = repo.obtener_indicadores(
    curso,
    asignatura,
    evaluacion,
    grupo
)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Alumnos evaluados",
    indicadores["alumnos"]
)

col2.metric(
    "Nota media",
    f"{indicadores['media']:.2f}"
)

col3.metric(
    "Nota máxima",
    f"{indicadores['maxima']:.2f}"
)

col4.metric(
    "Nota mínima",
    f"{indicadores['minima']:.2f}"
)

col5.metric(
    "Aprobados",
    f"{indicadores['porcentaje_aprobados']:.1f}%"
)