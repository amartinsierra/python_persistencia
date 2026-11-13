import pandas as pd
presupuesto=float(input("Introduzca su presupuestyo disponible: "))
df=pd.read_csv("houses.csv",encoding="UTF-8")
print(df.query("price<=@presupuesto").sort_values(by=["price"],ascending=False))