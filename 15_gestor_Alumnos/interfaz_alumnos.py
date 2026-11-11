import streamlit as st
import operaciones_bd as opbd
tab_nuevo_alumno,tab_alumnos_cursos, tab_buscar_alumno=st.tabs(["Nuevo alumno","Buscar por curso","Buscar por DNI"])

    
with tab_nuevo_alumno:
    dni=st.text_input("DNI del alumno: ")
    nombre=st.text_input("Nombre del alumno: ",key="nombre")
    email=st.text_input("Email del alumno: ")
    curso=st.text_input("Curso del alumno: ")
    nota=st.text_input("Nota del alumno: ")
    if st.button("Alta alumno"):
        if opbd.buscar_alumno(dni)==None:
            opbd.alta_alumno(dni,nombre,email,curso,nota)
        else:
            st.toast("El dni ya existe!!")
with tab_alumnos_cursos:
    curso=st.selectbox("Selecciona curso",opbd.cursos())
    if curso:
        col_nombre,col_email,col_dni,col_nota,col_eliminar=st.columns([2,3,1,1,2])
        alumnos=opbd.buscar_alumnos_curso(curso)
        for a in alumnos:
            col_nombre.write(a["nombre"])
            col_email.write(a["email"])
            col_dni.write(a["dni"])
            col_nota.write(a["nota"])
            if col_eliminar.button("Eliminar",key=f"eliminar{a["dni"]}"):
                opbd.eliminar_alumno(a["dni"])
                st.rerun()
with tab_buscar_alumno:
    dni=st.text_input("Introduce el DNI: ")
    if st.button("Buscar alumno"):
        alumno=opbd.buscar_alumno(dni)
        if alumno==None:
            st.toast("El dni no existe!!")
        else:
            st.write(f"Nombre :**{alumno["nombre"]}**")
            st.write(f"Email :**{alumno["email"]}**")
            st.write(f"Curso :**{alumno["curso"]}**")
            st.write(f"Nota :**{alumno["nota"]}**")

