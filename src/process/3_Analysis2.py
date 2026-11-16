# Importo posibles librerías

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind


# ANÁLISIS 2 - Análisis del rendimiento según el género

# Leemos el csv

sp = pd.read_csv("../../data/StudentsPerformance_depurado.csv", sep =",")


# Obtenemos el gráfico de las competencias por sexo y lo guardamos en img

rendimiento_sexo = sp.groupby("gender")[["math_score", "reading_score", "writing_score", "global_score"]].mean()
rendimiento_sexo = rendimiento_sexo.T #trasponer los datos para poder sacar el gráfico que quiero
rend = rendimiento_sexo.plot(kind="bar", figsize=(10, 6), width=0.8, color=["purple", "grey"])
plt.title("Rendimiento académico según el sexo")
plt.xticks(ticks=range(4), labels=["Matemáticas", "Lectura", "Escritura", "Rendimiento global"], rotation=0)

for container in rend.containers:
    rend.bar_label(container, fmt="%.2f", padding=3, fontsize=9)

plt.ylim(0, 100)
plt.legend(title="Sexo")
plt.tight_layout()

plt.savefig("../../img/Grafico_2_1.jpg", dpi=300, bbox_inches="tight")


# Calculamos si las diferencias son estadísticamente significativas o no, con el test t-Student. Asumimos muestras independientes sin igualdad de varianzas.

variables = ["math_score", "reading_score", "writing_score", "global_score"]

for variable in variables:

    mujeres = sp[sp["gender"] == "female"][variable]
    hombres = sp[sp["gender"] == "male"][variable]

    t, p = ttest_ind(mujeres, hombres, equal_var=False)

    print("\n", variable)
    print("Estadístico t:", round(t, 4))
    print("p-valor:", round(p, 4))

    if p < 0.05:
        print("Existe una diferencia estadísticamente significativa")
    else:
        print("No existe una diferencia estadísticamente significativa")


print("Análisis 2 realizado con su gráfico y el test de igualdad de medias t-Student")

# FIN