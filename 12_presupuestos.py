import csv,streamlit as st
#a partir de un presupuesto, devuelve la lista de 
#casas que se puede permitir
def posibles(presupuesto):
    with open("houses.csv","r") as f:
        todos=list(csv.DictReader(f))
        return [h for h in todos if int(h["price"])<=int(presupuesto)]

pres=st.text_input("Dime tu presupuesto: ")
if st.button("Calcular"):   
    st.table(posibles(pres))
    

presupuesto = st.number_input("Dime tu presupuesto: ")
with open("houses.csv", "r") as f:
    disponibles=list(filter(lambda p:float(p["price"])<=presupuesto,csv.DictReader(f)))
    st.table(disponibles)