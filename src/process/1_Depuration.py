# IMPORTO LIBRERIAS
import pandas as pd
import os

os.getcwd()

# LEO BASE DE DATOS

sp = pd.read_csv(r"../../data/StudentsPerformance.csv", sep=",")


# REEMPLAZO EL VALOR "none" DE LA VARIABLE "test_preparation_course"

sp["test_preparation_course"] = sp["test_preparation_course"].replace("none", "not completed")


# CREACIÓN NOTA GLOBAL "global_score"

sp["global_score"] = (sp["math_score"] + sp["reading_score"] + sp["writing_score"])/3
sp["global_score"] = sp["global_score"].round(2)


# GUARDAR LA NUEVA BASE DEPURADA

sp.to_csv("../../data/StudentsPerformance_depurado.csv", index=False, encoding="utf-8-sig")

print("Depuración terminada y creación del nuevo csv hecho")


## FIN