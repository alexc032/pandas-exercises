import pandas as pd
import numpy as np

#Sintaxis y ejemplos basicos
data = {"nombre": ["Ana", "Mateo", "Sofía", "Carlos", "Elena"],
    "edad": [16, 17, 16, 18, 17],
    "horas_estudio": [5, 2, None, 6, 3],
    "calificacion": [92, 65, 80, 95, 74]}

df = pd.DataFrame(data)
#print(df.isna().sum())
#print(df.info())
#print(df.shape)
#print(df["calificacion"])

#Practica1
df["aprobo"] = (df["calificacion"] >= 70).astype(int)
print(df)

#Ex1
solo_mayores = df[df["edad"] >= 17]
mayores = solo_mayores[["nombre", "calificacion"]]
print(mayores)

#Ex2
df["puntos_por_hora"] = (df["calificacion"] / df["horas_estudio"])
print(df)

#Ex3
aprobados = df[df["aprobo"] == 1]
promedio = aprobados["calificacion"].mean()
print(promedio)