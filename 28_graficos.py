import matplotlib.pyplot as plt 
""" meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"] 
consumo1 = [120, 150, 135, 180, 160] 
consumo2 = [45,170,100,80,110]
plt.plot(meses, consumo1,marker="o",label="Tienda Sur") 
plt.plot(meses, consumo2,marker="s",label="Tienda Norte") 
plt.title("Consumo eléctrico mensual") 
plt.xlabel("Mes") 
plt.ylabel("Consumo (kWh)") 
plt.legend()
plt.grid(True)
plt.show() """

edificios = ["Oficinas", "Almacén", "Fábrica", "Tienda"] 
consumo = [350, 220, 580, 190] 
plt.pie( 
consumo, 
labels=edificios, 
autopct="%1.1f%%" #muestra los porcentajes dentro del grafico
) 
plt.title("Distribución del consumo") 
plt.show() 

""" edades = [ 
18, 19, 20, 21, 22, 
23, 24, 25, 25, 26, 
27, 28, 29, 30, 31, 
32, 35, 38, 42, 45 
] 
plt.title("Distribución de edades") 
plt.xlabel("Edades") 
plt.ylabel("Personas") 
plt.hist(edades,bins=5,edgecolor="black") 
plt.show() """