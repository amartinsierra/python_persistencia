import streamlit as st
saludo=""
with st.sidebar:
    st.write("Menú navegación")
    st.text_input("Dato:")
    if st.button("pulsar"):
        saludo="Estoy en navegación"
st.write(saludo)