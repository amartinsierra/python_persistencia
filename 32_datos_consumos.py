import numpy as np
consumos=np.array([1250, 1380, 980, 1450, 1520, 1100, 1600])
dias=np.array(["Lunes", "Martes", "Miércoles", "Jueves","Viernes", "Sábado", "Domingo"])


#1. Consumo total semanal
print(f"Consumo total semanal {np.sum(consumos)}")
#2. Consumo medio diario
print(f"Consumo medio diario {np.average(consumos)}")
#3. Dias con mayor y menor consumo

print(f"Día de mayor consumo {dias[(np.argmax(consumos))]} con {np.amax(consumos)} kw/h")
print(f"Día de menor consumo {dias[(np.argmin(consumos))]} con {np.amin(consumos)} kw/h")


#4. Días con consumo superior a la media
#??
media=np.average(consumos)
print(f"Dias consumo superior media: {dias[consumos>media]}")
#6. Días con consumo un 20% inferior a la media
#??
media_reducida=np.average(consumos)*0.8
print(f"Dias consumo 80% inferior media: {dias[consumos<media_reducida]}")
#7. Coste total, sabiendo que de lunes a viernes el coste del Kw es de 0,02 y en fin de semana del 0,018

tarifas = np.array([0.02, 0.02, 0.02, 0.02, 0.02, 0.018, 0.018])
coste_total = np.sum(consumos * tarifas)
print(f"7. Coste total semanal: {coste_total:.2f} €") 
#
##5. Porcentaje de consumo cada día
total=np.sum(consumos)
for dia,consumo in zip(dias,consumos):
    print(f"El día {dia} ha consumido {consumo} kw/h que supone un {((consumo/total)*100).round(2)} % del total") 
##8. Mostrar consumo de cada dia
for dia,energia in zip(dias,consumos):
    print(f"{dia} se consumió: {energia} kw")