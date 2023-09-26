import math
import numpy as np
np.set_printoptions(precision=2, suppress=True)
import matplotlib.pyplot as plot
import libreria as lib

def clics(mat, vect, clic):
    if clic == 0:
        return vect
    elif clic == 1:
        return lib.acc_mat_vect(mat, vect)
    else:
        return lib.acc_mat_vect(mat, clics(mat, vect, clic - 1))

#Experimento Canicas
def canicas(mat, vect, clic):
    if len(mat) != len(mat[0]):
        return print("Error")
    resultado = clics(mat, vect, clic)
    return resultado

#Probabilistico clasico
def sis_proba(mat, vect, clic):
    resultado = clics(mat, vect, clic)
    resultado = (round(i, 2) for i in resultado)
    return resultado

#Probabilistico mas de dos rendijas
def sis_proba_dos(mat, vect, clic):
    resultado = clics(mat, vect, clic)
    resultado = (round(i, 2) for i in resultado)
    return resultado

#Sistema cauntico
def mod_cua(c):
    return abs(c)**2

def sis_cuantico(mat, vect, clic):
    resultado = clics(mat, vect, clic)
    return resultado

def graficar(resultado):
    x = np.array([x for x in range(len(resultado))])
    y = np.array([round(resultado[x]*10, 2) for x in range(len(resultado))])
    plot.bar(x, y, color = "g", align = "center")
    plot.title("Probabilidad de ubicacion en %")
    plot.savefig("figura.png")
    plot.show()
