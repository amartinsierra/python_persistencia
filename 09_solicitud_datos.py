import streamlit as st
nombre=st.text_input("Introduce tu nombre")
edad=st.number_input("Introduce tu edad",value=0)
afiliado=st.checkbox("Afiliado")
curso=st.radio("Elige curso: ",["Python","C++","Java"])
centro=st.selectbox("Elige centro: ",["Leganés","Getafe","Alcobendas","San Blas"])
if st.button("Pulsar"):
    st.success(f"Te llamas {nombre}, tienes {edad} años, has elegido el curso {curso} en el centro {centro}")
    
aula = [ 
    {"id": 1, "nombre": "Juan", "edad": 25}, 
    {"id": 2, "nombre": "Ana", "edad": 30}, 
    {"id": 3, "nombre": "Pedro", "edad": 22} 
] 
st.table(aula) 
