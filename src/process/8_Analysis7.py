# Importo posibles librerías

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind


# ANÁLISIS 6 - Análisis de correlaciones entre asignaturas

# Leo el csv

sp = pd.read_csv("../../data/StudentsPerformance_depurado.csv", sep =",")


# ANÁLISIS 7 - Crear un indicador global de rendimiento académico y analizar los grupos de bajo y alto rendimiento

# Lo primero es crear una variable clasificatoria en base a la variable ya creada global_score en base a:
"""
    Rendimiento	    Puntuación
    Bajo	         0-49,99
    Medio	         50-69,99
    Alto	         70-84,99
    Excelente	     85-100
"""

sp["performance_level"] = pd.cut(sp["global_score"], bins=[0, 50, 70, 85, 100], labels=["low", "medium", "high", "excellent"], right=False)
sp["performance_level"].value_counts().sort_index()
perf = sp["performance_level"].value_counts(normalize=True).sort_index() * 100
perf.round(2)


# Y ahora hacemos el gráfico de su distribución

porcen = sp["performance_level"].value_counts(normalize=True).sort_index() * 100
perf = porcen.plot(kind="bar", color="magenta", figsize=(8, 6))
perf.bar_label(perf.containers[0], fmt="%.1f%%", padding=3)

plt.title("Distribución de estudiantes según su rendimiento medio")
plt.ylabel("Porcentaje de estudiantes (%)")
plt.xlabel("Performance level")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("../../img/Grafico_7_1.jpg", dpi=300, bbox_inches="tight")


# Observando los valores más comunes en el contexto del grupo de bajo rendimiento:

gender_bajorend = sp["gender"][sp["performance_level"] == "low"].mode()
race_bajorend = sp["race_ethnicity"][sp["performance_level"] == "low"].mode()
parental_bajorend = sp["parental_level_of_education"][sp["performance_level"] == "low"].mode()
lunch_bajorend = sp["lunch"][sp["performance_level"] == "low"].mode()
test_bajorend = sp["test_preparation_course"][sp["performance_level"] == "low"].mode()

print("Las características mayoritarias del grupo de bajo rendimiento son: ")
print("")
print("Gender: ", gender_bajorend.unique())
print("----------------------")
print("Race/Ethnicity: ", race_bajorend.unique())
print("----------------------")
print("Parental level of Education: ", parental_bajorend.unique())
print("----------------------")
print("School Lunch Program: ", lunch_bajorend.unique())
print("----------------------")
print("Test Preparation Course: ", test_bajorend.unique())


# Observando los valores más comunes en el contexto del grupo de alto rendimiento:

gender_altorend = sp["gender"][sp["performance_level"] == "excellent"].mode()
race_altorend = sp["race_ethnicity"][sp["performance_level"] == "excellent"].mode()
parental_altorend = sp["parental_level_of_education"][sp["performance_level"] == "excellent"].mode()
lunch_altorend = sp["lunch"][sp["performance_level"] == "excellent"].mode()
test_altorend = sp["test_preparation_course"][sp["performance_level"] == "excellent"].mode()

print("Las características mayoritarias del grupo de alto rendimiento son: ")
print("")
print("Gender: ", gender_altorend.unique())
print("----------------------")
print("Race/Ethnicity: ", race_altorend.unique())
print("----------------------")
print("Parental level of Education: ", parental_altorend.unique())
print("----------------------")
print("School Lunch Program: ", lunch_altorend.unique())
print("----------------------")
print("Test Preparation Course: ", test_altorend.unique())


print("Análisis 7 realizado con su gráfico y se han contextualizado los grupos de bajo y alto rendimiento")

# FIN
