# Importo posibles librerias

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ANÁLISIS 1 - Análisis general del rendimiento académico

# Leemos el csv

sp = pd.read_csv("../../data/StudentsPerformance_depurado.csv", sep =",")

# Gráfico de cajas - Distribución de las distintas competencias y guardo el gráfico en la carpeta de "img"

datos = [sp["math_score"], sp["reading_score"], sp["writing_score"], sp["global_score"]]
plt.figure(figsize=(9, 6))
box = plt.boxplot(datos, patch_artist=True, tick_labels=["Matemáticas", "Lectura", "Escritura", "Global"], orientation="vertical", medianprops={"color": "black", "linewidth": 2})
colores = ["green", "green", "green", "blue"]

for caja, color in zip(box["boxes"], colores):
    caja.set_facecolor(color)
    
plt.title("Distribución de las notas por competencia")
plt.ylabel("Notas")
plt.ylim(-10, 120)
plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.savefig("../../img/Grafico_1_1.jpg", dpi=300, bbox_inches="tight")


# Gráfico de barras del rendimiento de los estudiantes en cada competencia

notas_medias = sp[["math_score", "reading_score", "writing_score", "global_score"]].mean()
colores = ["green", "green", "green", "blue"]
plt.figure(figsize=(9, 5))
notas_medias.index = ["Matemáticas", "Lectura", "Escritura", "Global"]
barras = plt.bar(notas_medias.index, notas_medias.values, color=colores)

for barra in barras:
    altura = barra.get_height()
    plt.text(barra.get_x() + barra.get_width() / 2, altura + 0.5, f"{altura:.2f}", ha="center", va="bottom")

plt.title("Nota media por competencias")
plt.ylabel("Nota media")
plt.ylim(0, 110)

plt.savefig("../../img/Grafico_1_2.jpg", dpi=300, bbox_inches="tight")



# Calculamos el porcentaje de alumnos que representan los estudiantes de bajo rendimmiento en las 3 competencias (notas <50)

bajo_rendimiento = sp[(sp["math_score"] < 50) & (sp["reading_score"] < 50) & (sp["writing_score"] < 50)]
num_alumnos = len(bajo_rendimiento)
porcentaje = (num_alumnos / len(sp)) * 100
print("Alumnos con bajo rendimiento:", num_alumnos)
print(f"Porcentaje de alumnos: {porcentaje:.2f}%")


# Gráfico de sectores para ver la distribución del bajo rendimiento en las 3 competencias a la vez

porcentaje_bajo = len(bajo_rendimiento) / len(sp) * 100
porcentaje_resto = 100 - porcentaje_bajo
etiquetas = ["Bajo rendimiento", "Resto de estudiantes"]
valores = [porcentaje_bajo, porcentaje_resto]
plt.figure(figsize=(7, 7))
plt.pie(valores, labels=etiquetas, autopct="%1.2f%%", startangle=90, explode=(0.1, 0), colors=["red", "lightblue"])
plt.title("Distribución del alumnado según rendimiento")

plt.savefig("../../img/Grafico_1_3.jpg", dpi=300, bbox_inches="tight")


# Contexto del grupo de bajo rendimiento, siendo este que las 3 puntuaciones sean menores de 50 (sobre 100)

gender_bajorend = bajo_rendimiento["gender"].mode().unique()
race_bajorend = bajo_rendimiento["race_ethnicity"].mode().unique()
parental_bajorend = bajo_rendimiento["parental_level_of_education"].mode().unique()
lunch_bajorend = bajo_rendimiento["lunch"].mode().unique()
test_bajorend = bajo_rendimiento["test_preparation_course"].mode().unique()

print("Las características mayoritarias del grupo de bajo rendimiento son: ")
print("")
print("Gender: ", gender_bajorend.value_counts())
print("----------------------")
print("Race/Ethnicity: ", race_bajorend.value_counts())
print("----------------------")
print("Parental level of Education: ", parental_bajorend.value_counts())
print("----------------------")
print("School Lunch Program: ", lunch_bajorend.value_counts())
print("----------------------")
print("Test Preparation Course: ", test_bajorend.value_counts())


# Calculamos el porcentaje de alumnos que representan los estudiantes de alto rendimmiento en las 3 competencias (notas >70)

alto_rendimiento = sp[(sp["math_score"] > 70) & (sp["reading_score"] > 70) & (sp["writing_score"] > 70)]
num_alumnos_alto = len(alto_rendimiento)
porcentaje = (num_alumnos_alto / len(sp)) * 100
print("Alumnos con alto rendimiento:", num_alumnos_alto)
print(f"Porcentaje de alumnos: {porcentaje:.2f}%")


# Gráfico de sectores para ver la distribución del alto rendimiento en las 3 competencias a la vez

porcentaje_alto =( num_alumnos_alto / len(sp)) * 100
porcentaje_resto = 100 - porcentaje_alto
etiquetas = ["Alto rendimiento", "Resto de estudiantes"]
valores = [porcentaje_alto, porcentaje_resto]
plt.figure(figsize=(7, 7))
plt.pie(valores, labels=etiquetas, autopct="%1.2f%%", startangle=90, explode=(0.1, 0), colors=["green", "lightblue"])
plt.title("Distribución del alumnado según rendimiento")

plt.savefig("../../img/Grafico_1_4.jpg", dpi=300, bbox_inches="tight")


# Contexto del grupo de alto rendimiento, siendo este que las 3 puntuaciones sean mayores de 70 (sobre 100)

gender_altorend = alto_rendimiento["gender"].mode().unique()
race_altorend = alto_rendimiento["race_ethnicity"].mode().unique()
parental_altorend = alto_rendimiento["parental_level_of_education"].mode().unique()
lunch_altorend = alto_rendimiento["lunch"].mode().unique()
test_altorend = alto_rendimiento["test_preparation_course"].mode().unique()

print("Las características mayoritarias del grupo de alto rendimiento son: ")
print("")
print("Gender: ", gender_altorend.value_counts())
print("----------------------")
print("Race/Ethnicity: ", race_altorend.value_counts())
print("----------------------")
print("Parental level of Education: ", parental_altorend.value_counts())
print("----------------------")
print("School Lunch Program: ", lunch_altorend.value_counts())
print("----------------------")
print("Test Preparation Course: ", test_altorend.value_counts())



print("Análisis 1 terminado y creación de gráficos hecha")


## FIN
