import streamlit as st
import tiendas_repository as repo
import matplotlib.pyplot as plt
def crear_grafico():
    datos=repo.facturacion_total_tiendas()
    tiendas = [t["nombre_tienda"] for t in datos] 
    facturaciones=[t["facturacion_total"] for t in datos]
    
    plt.pie( 
    facturaciones, 
    labels=tiendas, 
    autopct="%1.1f%%" #muestra los porcentajes dentro del grafico
    ) 
    plt.title("Distribución de facturación total de tiendas") 
    return plt
tienda_sel=None
mes_sel=None
with st.sidebar:
    st.subheader("Filtrado de datos")
    tienda_sel=st.selectbox("Seleccione tienda",repo.tiendas(),index=None,key=1)
    mes_sel=st.selectbox("Seleccione mes",repo.meses(),index=None,key=2)
    
    
if tienda_sel!=None:
    st.table(repo.datos_tabla_tienda(tienda_sel))
    datos=repo.datos_tienda(tienda_sel)
    tupla=repo.mes_mayor_facturacion(tienda_sel)
    #st.write(f"Total facturacion {datos[0]["facturacion_total"]}, gastos totales {datos[0]["gastos_totales"]}, mes con mayor facturacion {tupla[1]}")
    col1,col2,col=st.columns(3)
    col1.metric("Total facturacion",datos[0]["facturacion_total"])
    col2.metric("Gastos totales",datos[0]["gastos_totales"])
    col.metric("Ms con mayor facturacion",repo.mes_mayor_facturacion(tienda_sel)[1])
    ##dibujamos grafico de facturación total
    grafico=crear_grafico()
    st.pyplot(grafico)
if mes_sel!=None:
    st.table(repo.datos_tabla_mes(mes_sel))
    
    
   