# Importo posibles librerías

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind


# ANÁLISIS 3 - Análisis del rendimiento según su contexto socio-económico

# Leo el csv

sp = pd.read_csv("../../data/StudentsPerformance_depurado.csv", sep =",")


# Gráfico de barras de las medias por competencia agrupadas por la variable lunch

rendimiento_lunch = sp.groupby("lunch")[["math_score", "reading_score", "writing_score", "global_score"]].mean()
rendimiento_lunch = rendimiento_lunch.T #trasponer los datos para poder sacar el gráfico que quiero
rend = rendimiento_lunch.plot(kind="bar", figsize=(10, 6), width=0.8, color=["lightgreen", "brown"])
plt.title("Rendimiento académico según el School Lunch Program")
plt.xticks(ticks=range(4), labels=["Matemáticas", "Lectura", "Escritura", "Rendimiento global"], rotation=0)

for container in rend.containers:
    rend.bar_label(container, fmt="%.2f", padding=3, fontsize=9)

plt.ylim(0, 100)
plt.legend(title="School Lunch Program")
plt.tight_layout()

plt.savefig("../../img/Grafico_3_1.jpg", dpi=300, bbox_inches="tight")


# Compruebo la igualdad de medias a través del estadístico t-Student, para ver si las diferencias son estadísticamente significativas o no.

variables = ["math_score", "reading_score", "writing_score", "global_score"]

for variable in variables:

    standard = sp[sp["lunch"] == "standard"][variable]
    free_reduced = sp[sp["lunch"] == "free/reduced"][variable]

    t, p = ttest_ind(standard, free_reduced, equal_var=False)

    print("\n", variable)
    print("Estadístico t:", round(t, 4))
    print("p-valor:", round(p, 4))

    if p < 0.05:
        print("Existe una diferencia estadísticamente significativa")
    else:
        print("No existe una diferencia estadísticamente significativa")


print("Análisis 3 realizado, creado el gráfico y comprobado las significación de las diferencias")

# FIN