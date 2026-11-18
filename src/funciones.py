# IMPORTO LIBRERIAS
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

def ejecutar_depuracion():

    # LEO BASE DE DATOS

    sp = pd.read_csv(r"../data/StudentsPerformance.csv", sep=",")


    # REEMPLAZO EL VALOR "none" DE LA VARIABLE "test_preparation_course"

    sp["test_preparation_course"] = sp["test_preparation_course"].replace("none", "not completed")


    # CREACIÓN NOTA GLOBAL "global_score"

    sp["global_score"] = (sp["math_score"] + sp["reading_score"] + sp["writing_score"])/3
    sp["global_score"] = sp["global_score"].round(2)


    # GUARDAR LA NUEVA BASE DEPURADA

    sp.to_csv("../data/StudentsPerformance_depurado.csv", index=False, encoding="utf-8-sig")

    return print("Depuración terminada y creación del nuevo csv hecho")


def ejecutar_analisis_1():

    # ANÁLISIS 1 - Análisis general del rendimiento académico

    # Leemos el csv

    sp = pd.read_csv("../data/StudentsPerformance_depurado.csv", sep =",")

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

    plt.savefig("../img/Grafico_1_1.jpg", dpi=300, bbox_inches="tight")


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

    plt.savefig("../img/Grafico_1_2.jpg", dpi=300, bbox_inches="tight")


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

    plt.savefig("../img/Grafico_1_3.jpg", dpi=300, bbox_inches="tight")


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

    plt.savefig("../img/Grafico_1_4.jpg", dpi=300, bbox_inches="tight")


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

    return print("Análisis 1 terminado y creación de gráficos hecha")


def ejecutar_analisis_2():

    # ANÁLISIS 2 - Análisis del rendimiento según el género

    # Leemos el csv

    sp = pd.read_csv("../data/StudentsPerformance_depurado.csv", sep =",")


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

    plt.savefig("../img/Grafico_2_1.jpg", dpi=300, bbox_inches="tight")


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


    return print("Análisis 2 realizado con su gráfico y el test de igualdad de medias t-Student")



def ejecutar_analisis_3():

    # Leo el csv

    sp = pd.read_csv("../data/StudentsPerformance_depurado.csv", sep =",")


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

    plt.savefig("../img/Grafico_3_1.jpg", dpi=300, bbox_inches="tight")


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

    return print("Análisis 3 realizado, creado el gráfico y comprobado las significación de las diferencias")


def ejecutar_analisis_4():

    # Leo el csv

    sp = pd.read_csv("../data/StudentsPerformance_depurado.csv", sep =",")


    # Primero vamos a ver la distribución de estudiantes por nivel educativo familiar

    orden = ["some high school", "high school", "some college", "associate's degree", "bachelor's degree", "master's degree"]
    porcentajes = sp["parental_level_of_education"].value_counts(normalize=True).reindex(orden) * 100
    datos = porcentajes.plot(kind="bar", figsize=(10, 6), color="teal")
    datos.bar_label(datos.containers[0], fmt="%.1f%%", padding=3)

    plt.title("Nivel educativo de los padres")
    plt.ylabel("Porcentaje de estudiantes (%)")
    plt.xlabel("Nivel educativo")
    plt.xticks(rotation=35, ha="right")
    #plt.tight_layout()

    plt.savefig("../img/Grafico_4_1.jpg", dpi=300, bbox_inches="tight")


    # Ahora vamos a ver el rendimiento académico medio según el nivel educativo de los padres

    rendimiento_padres = sp.groupby("parental_level_of_education")[["math_score", "reading_score", "writing_score", "global_score"]].mean()
    rendimiento_padres = rendimiento_padres.reindex(orden)
    rendimiento_padres = rendimiento_padres.T
    ren = rendimiento_padres.plot(kind="bar", figsize=(13, 6), width=0.8)

    for barras in ren.containers:
        ren.bar_label(barras, fmt="%.1f", padding=2, fontsize=8)

    ren.set_title("Rendimiento académico según el nivel educativo de los padres")
    ren.set_ylabel("Puntuación media")
    ren.set_xticklabels(["Matemáticas", "Lectura", "Escritura", "Rendimiento global"], rotation=0)
    ren.legend(title="Nivel educativo de los padres", bbox_to_anchor=(1.02, 1), loc="upper left")
    plt.tight_layout()

    plt.savefig("../img/Grafico_4_2.jpg", dpi=300, bbox_inches="tight")


    # Vamos a ver la distribución del rendimiento global según el nivel educativo de los padres

    orden = ["some high school", "high school", "some college", "associate's degree", "bachelor's degree", "master's degree"]
    dat = [sp.loc[sp["parental_level_of_education"] == nivel, "global_score"].dropna() for nivel in orden]

    plt.figure(figsize=(12, 6))
    plt.boxplot(dat, tick_labels=orden)
    plt.title("Distribución del rendimiento global según la educación de los padres")
    plt.xlabel("Nivel educativo de los padres")
    plt.ylabel("Rendimiento global")
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()

    plt.savefig("../img/Grafico_4_3.jpg", dpi=300, bbox_inches="tight")

    return print("Análisis 4 realizado y creados los gráficos")



def ejecutar_analisis_5():

    # Leo el csv

    sp = pd.read_csv("../data/StudentsPerformance_depurado.csv", sep =",")


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

    plt.savefig("../img/Grafico_5_1.jpg", dpi=300, bbox_inches="tight")


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


    return print("Análisis 5 realizado con su gráfico y el test de igualdad de medias t-Student")



def ejecutar_analisis_6():

    # Leo el csv

    sp = pd.read_csv("../data/StudentsPerformance_depurado.csv", sep =",")

    # Calculamos el mapa de correlaciones

    correlaciones = sp[["math_score", "reading_score", "writing_score"]].corr()
    sns.heatmap(correlaciones, annot=True, cmap="coolwarm", vmin=-1, vmax=1)

    plt.title("Matriz de correlaciones entre competencias")
    plt.savefig("../img/Grafico_6_1.jpg", dpi=300, bbox_inches="tight")

    return print("Análisis 6 realizado y con su gráfico")


def ejecutar_analisis_7():

    # Leo el csv

    sp = pd.read_csv("../data/StudentsPerformance_depurado.csv", sep =",")

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

    plt.savefig("../img/Grafico_7_1.jpg", dpi=300, bbox_inches="tight")

    # Observando los valores más comunes en el contexto del grupo de bajo rendimiento:

    gender_bajorend = sp["gender"][sp["performance_level"] == "low"].mode().unique()
    race_bajorend = sp["race_ethnicity"][sp["performance_level"] == "low"].mode().unique()
    parental_bajorend = sp["parental_level_of_education"][sp["performance_level"] == "low"].mode().unique()
    lunch_bajorend = sp["lunch"][sp["performance_level"] == "low"].mode().unique()
    test_bajorend = sp["test_preparation_course"][sp["performance_level"] == "low"].mode().unique()

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

    # Observando los valores más comunes en el contexto del grupo de alto rendimiento:

    gender_altorend = sp["gender"][sp["performance_level"] == "excellent"].mode().unique()
    race_altorend = sp["race_ethnicity"][sp["performance_level"] == "excellent"].mode()
    parental_altorend = sp["parental_level_of_education"][sp["performance_level"] == "excellent"].mode().unique()
    lunch_altorend = sp["lunch"][sp["performance_level"] == "excellent"].mode().unique()
    test_altorend = sp["test_preparation_course"][sp["performance_level"] == "excellent"].mode().unique()

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

    return print("Análisis 7 realizado con su gráfico y se han contextualizado los grupos de bajo y alto rendimiento")

   
