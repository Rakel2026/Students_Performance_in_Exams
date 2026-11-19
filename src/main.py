# importamos las funciones
import funciones
import time

print("Vamos a realizar un EDA sobre el 'Rendimiento de los estudiantes en los exámenes'.")

print("Para ello tenemos que seguir los pasos adecuados e intentar llegar a conclusiones para poder continuar con el estudio.")

print ("Primero vamos a realizar la depuración de la base de datos.")
funciones.ejecutar_depuracion()
print("---------------------------------")
time.sleep(5)

print("Ahora comenzamos con nuestro Análisis 1: Análisis general del rendimiento académico")
funciones.ejecutar_analisis_1()
print("---------------------------------")
time.sleep(5)

print("Continuamos con el Análisis 2: Análisis del rendimiento según el género")
funciones.ejecutar_analisis_2()
print("---------------------------------")
time.sleep(5)

print("Seguimos con el Análisis 3: Análisis del rendimiento según su contexto socio-económico")
funciones.ejecutar_analisis_3()
print("---------------------------------")
time.sleep(5)

print("Ahora realizamos el Análisis 4: Análisis del rendimiento según el nivel educativo de los padres")
funciones.ejecutar_analisis_4
print("---------------------------------")
time.sleep(5)

print("Continuamos con el Análisis 5: Análisis del rendimiento según la preparación previa de los exámenes")
funciones.ejecutar_analisis_5()
print("---------------------------------")
time.sleep(5)

print("Seguimos con el Análisis 6: Análisis de correlaciones entre asignaturas")
funciones.ejecutar_analisis_6()
print("---------------------------------")
time.sleep(5)

print("Ahora realizamos el Análisis 7: Crear un indicador global de rendimiento académico y analizar los grupos de bajo y alto rendimiento")
funciones.ejecutar_analisis_7()
print("---------------------------------")
time.sleep(5)

print("PROCESO DE ANÁLISIS DESCRIPTIVO Y VISUALIZACIÓN DE DATOS TERMINADO")
