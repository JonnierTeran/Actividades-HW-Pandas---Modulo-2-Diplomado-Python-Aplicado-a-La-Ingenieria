# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 23:30:00 2022

@author: jonnier andres teran
"""

# Taller N1 - Modulo 2   "LOS DATOS Y YO"
# Autor: Jonnier Andres Teran Morales
# Correo= Jonnier.teran@upb.edu.co
# ID No. 502195
# id: 1003064599
# Cel: 3245644212

from email.policy import default
import pandas as pd
import numpy as np

dataF = pd.read_excel("dataEstud.xlsx")

#Ejercicio 1  IMC 
# Calculamos el imc de cada estudiante y lo agregamos en una nueva columna del dataFame y lo Mostramos inmediatamente por pantalla y en el explorador de variables
imc = (dataF["weight"]/((dataF["height"])**2)).round(0)
dataF["IMC"] = imc
print(dataF)

#Ejercicio 2  el capital obtenido en la inversión
# Calculamos el capital obtenido en la inversión, Lo agregamos a una nueva columna de nuestro DataFrame y ademas lo mostramos por pantalla y podemos observarlo en el explorador de variables
Cap_Final = ((dataF["money to invest"])*(dataF["annual interest"]/ (100 + 1))**dataF["years of investment"])
dataF["Compound interest"] =  Cap_Final
print("El capital Final es:\n",)
print(Cap_Final)


#Ejercicio 3 
#Creamos una columna en el DataFrame para determinar el porcentaje de descuento obtenido de acuerdo a la hora en que fue realizada la compra. Y otra columna para el precio final obtenido.
#Generamos 2 listas una con las horas y otra con los porcentajes de descuento y las asignamos correspondientemente, luego creamos la nueva columna en el dataFrame con la informacion del porcentaje de descuento obtenido teniendo en cuenta la hora de compra

Hrs_List = [
     (dataF["time to buy bread after baking"] <= 6),
     (dataF["time to buy bread after baking"] <= 12 ),
     (dataF["time to buy bread after baking"] <= 18 ),
     (dataF["time to buy bread after baking"] <= 24 )
]
Discount_List = [10,20,30,40]
dataF["discount obtained"] = np.select(Hrs_List,Discount_List,default="Error, indefinite discount")

# Ejercicio 4
# . Debe organizar en el DataFrame (nueva columna) las extensiones de forma que si el sexo de la persona es M, debe poner como extensión 11 y si el sexo es F, debe poner como extensión 10.
#Generamos 2 listas una con los Generos y otra con las Extensiones y las asignamos correspondientemente el genero, luego creamos la nueva columna en el dataFrame con la informacion del numero telefonico junto a la nueva extension.
Sex_List = [
    (dataF["sex"] == "F"),
    (dataF["sex"] == "M" )
]
extension_date = [dataF["phone number"] + "-10", dataF["phone number"] + "-11"]
dataF["Generate by extensions"] = np.select(Sex_List,extension_date,default="undefined")

# Mostramos todo nuestro dataFrame
print(dataF)