# Importo posibles librerías

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind


# ANÁLISIS 6 - Análisis de correlaciones entre asignaturas

# Leo el csv

sp = pd.read_csv("../../data/StudentsPerformance_depurado.csv", sep =",")


# Calculamos el mapa de correlaciones

correlaciones = sp[["math_score", "reading_score", "writing_score"]].corr()
sns.heatmap(correlaciones, annot=True, cmap="coolwarm", vmin=-1, vmax=1)

plt.title("Matriz de correlaciones entre competencias")
plt.savefig("../../img/Grafico_6_1.jpg", dpi=300, bbox_inches="tight")


print("Análisis 6 realizado y con su gráfico")

# FIN
