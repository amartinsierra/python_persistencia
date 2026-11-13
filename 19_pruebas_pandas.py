import pandas as pd
lista_reproduccion=[
    {"titulo":"canción inventada","duracion":3.20,"valoracion":4},
    {"titulo":"Bohemian Rapsody","duracion":5.40,"valoracion":10},
    {"titulo":"Green summer","duracion":4.10,"valoracion":7}
]
#df=pd.DataFrame(lista_reproduccion)
#print(df)
df=pd.read_csv("empleados.csv", encoding="UTF-8")
"""print(df)
print(df.columns)
print(df.values)"""
for v in df.values:
    print(v[0])
#salario medio
print(f"salario medio: {df["salario"].mean():.2f}")
print(f"salario medio de informática: {df.query("departamento=='informática'")["salario"].mean():.2f}")

#Quiero agruparlos por departamento y con la columna salario medio y edad máxima
grupo=df.groupby("departamento").agg(salario_medio=("salario","mean"),edad_maxima=("edad","max"))
print(grupo.sort_values(by=["salario_medio","edad_maxima"]))