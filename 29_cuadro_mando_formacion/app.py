import streamlit as st
import matplotlib.pyplot as plt

import formacion_repository as repo


st.set_page_config(
    page_title="Análisis académico",
    layout="wide"
)
#####################
##Funciones para gráficos#######
def grafico_notas_asignaturas(datos): #Recibe dataframe
    fig,gr=plt.subplots()
    gr.bar(
        datos["asignatura"].to_list(),
        datos["nota_media"].to_list()
    )

    gr.set_title("Nota media por asignatura")
    gr.set_xlabel("Asignatura")
    gr.set_ylabel("Nota media")
    gr.set_ylim(0,10)
    return fig

def grafico_evolucion_evaluaciones(datos):
    fig,gr=plt.subplots()
    gr.plot(
        datos["evaluacion"].to_list(),
        datos["nota_media"].to_list(),
        marker="o"
    )

    gr.set_title("Evolución de las notas")
    gr.set_xlabel("Evaluación")
    gr.set_ylabel("Nota media")

    gr.set_xticks(datos["evaluacion"].to_list())
    gr.set_ylim(0, 10)

    plt.grid(alpha=0.3)
    return fig

def grafico_distribucion_notas(datos):
    fig, gr = plt.subplots()
    gr.hist(
        datos["nota"].to_list(),
        bins=10,
        range=(0, 10),
        edgecolor="black"
    )

    gr.set_title("Distribución de calificaciones")
    gr.set_xlabel("Nota")
    gr.set_ylabel("Número de calificaciones")

    gr.set_xticks(range(0, 11))
    return fig



#########################




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

#estadísticas por asignatura
st.subheader("Estadísticas por asignatura")

estadisticas_asignaturas = repo.obtener_estadisticas_asignaturas(
    curso,
    asignatura,
    evaluacion,
    grupo
)

st.dataframe(estadisticas_asignaturas)

#estadísticas por alumno
st.subheader("Rendimiento por alumno")

estadisticas_alumnos = repo.obtener_estadisticas_alumnos(
    curso,
    asignatura,
    evaluacion,
    grupo
)

st.dataframe(estadisticas_alumnos)


#graficos
st.subheader("Representación gráfica")

tab1, tab2, tab3 = st.tabs([
    "Notas por asignatura",
    "Evolución de evaluaciones",
    "Distribución de notas"
])
with tab1:
    fig=grafico_notas_asignaturas(estadisticas_asignaturas)
    st.pyplot(fig)
    plt.close(fig)
    

with tab2:
    evolucion=repo.obtener_evolucion_evaluaciones(curso,asignatura,grupo)
    fig=grafico_evolucion_evaluaciones(evolucion)
    st.pyplot(fig)
    plt.close(fig)

with tab3:

    fig = grafico_distribucion_notas(repo.obtener_datos_filtrados(curso,asignatura,evaluacion,grupo)) #función que devuelve todos los datos filtrados

    st.pyplot(fig)
    plt.close(fig)