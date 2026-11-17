# Importo posibles librerías

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind


# ANÁLISIS 5 - Análisis del rendimiento según la preparación previa de los exámenes

# Leo el csv

sp = pd.read_csv("../../data/StudentsPerformance_depurado.csv", sep =",")


# ANÁLISIS 5 - Análisis del rendimiento según la preparación previa de los exámenes

rendimiento_previo = sp.groupby("test_preparation_course")[["math_score", "reading_score", "writing_score", "global_score"]].mean()
rendimiento_previo = rendimiento_previo.T #trasponer los datos para poder sacar el gráfico que quiero
rend = rendimiento_previo.plot(kind="bar", figsize=(10, 6), width=0.8, color=["brown", "grey"])
plt.title("Rendimiento académico según la preparación previa de los exámenes")
plt.xticks(ticks=range(4), labels=["Matemáticas", "Lectura", "Escritura", "Rendimiento global"], rotation=0)

for container in rend.containers:
    rend.bar_label(container, fmt="%.2f", padding=3, fontsize=9)

plt.ylim(0, 100)
plt.legend(title="test preparation course")
plt.tight_layout()

plt.savefig("../../img/Grafico_5_1.jpg", dpi=300, bbox_inches="tight")


# Calculamos si las diferencias son estadísticamente significativas o no, con el test t-Student. Asumimos muestras independientes sin igualdad de varianzas.

variables = ["math_score", "reading_score", "writing_score", "global_score"]

for variable in variables:

    completado = sp[sp["test_preparation_course"] == "completed"][variable]
    no_completado = sp[sp["test_preparation_course"] == "not completed"][variable]

    t, p = ttest_ind(completado, no_completado, equal_var=False)

    print("\n", variable)
    print("Estadístico t:", round(t, 4))
    print("p-valor:", round(p, 4))

    if p < 0.05:
        print("Existe una diferencia estadísticamente significativa")
    else:
        print("No existe una diferencia estadísticamente significativa")


print("Análisis 5 realizado con su gráfico y el test de igualdad de medias t-Student")

# FIN