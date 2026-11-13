import pandas as pd
df=pd.read_json("alumnos.json",encoding="UTF-8")
print(f"Nota media global: {df["nota"].mean():.2f}")
grupo=df.groupby("curso").agg(nota_mayor=("nota","max"),total_alumnos=("nombre","count"))
print(grupo)