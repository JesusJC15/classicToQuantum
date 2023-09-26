import math
import numpy as np

np.set_printoptions(precision=2, suppress=True)


def suma_cplx(c1, c2):
    """suma de complejos
    (cplx, cplx -> cplx)
    """
    parte_r = c1[0] + c2[0]
    parte_i = c1[1] + c2[1]
    return parte_r, parte_i


def resta_cplx(c1, c2):
    """resta de complejos
    (cplx, cplx -> cplx)
    """
    parte_r = c1[0] - c2[0]
    parte_i = c1[1] - c2[1]
    return parte_r, parte_i


def multi_cplx(c1, c2):
    """multiplicacion de complejos
    (cplx, cplx -> cplx)
    """
    parte_r = (c1[0] * c2[0]) - (c1[1] * c2[1])
    parte_i = (c1[0] * c2[1]) + (c2[0] * c1[1])
    return parte_r, parte_i


def divi_cplx(c1, c2):
    """division de complejos
    (cplx, cplx -> cplx)
    """
    parte_r = ((c1[0] * c2[0]) + (c1[1] * c2[1])) / (c2[0] * (c2[0]) + (c2[1] * c2[1]))
    parte_i = ((c2[0] * c1[1]) - (c1[0] * c2[1])) / (c2[0] * (c2[0]) + (c2[1] * c2[1]))
    return parte_r, parte_i


def mod_cplx(c1):
    """modulo de un numero complejo
    (cplx -> real)
    """
    modulo = math.sqrt((c1[0] * c1[0]) + (c1[1] * c1[1]))
    return modulo


def conj_cplx(c1):
    """conjugado de un numero complejo
    (cplx -> cplx)
    """
    parte_r = c1[0]
    parte_i = -(c1[1])
    return parte_r, parte_i


def repre_cartesiana(c1):
    """representacion cartesiana de un numero complejo
    (real, angulo) -> (cplx)
    """
    a = c1[0] * math.cos(c1[1])
    b = c1[0] * math.sin(c1[1])
    return a, b


def repre_polar(c1):
    """representacion polar de un numero complejo
    (cplx) -> (real, angulo)
    """
    r = mod_cplx(c1)
    angle = math.atan2(c1[1], c1[0])
    return r, angle


def fase_cplx(c1):
    """fase o argumento de un numero complejo
    (cplx) -> real
    """
    fase = math.atan2(c1[1], c1[0])
    return fase


def sum_vect_cplx(v1, v2):
    """suma de vectores de numeros complejos
    (vect,vect) -> vect
    """
    result = []
    if len(v1) != len(v2):
        return print("Los vectores no tienen la misma longitud")
    else:
        for i in range(len(v1)):
            sum_vect = v1[i] + v2[i]
            result.append(sum_vect)
    return result


def nega_vect_cplx(v1):
    """negacion de un vector complejo
    (vect) -> vect
    """
    result = []
    for ele in v1:
        nega = -ele
        result.append(nega)
    return result


def multi_esc_vect(esc, v1):
    """multiplicación de un escalar por un vector complejo
    (cplx, vect) -> vect
    """
    result = []
    for ele in v1:
        multi = esc * ele
        result.append(multi)
    return result


def suma_mat_cplx(A, B):
    """suma de matrices de numeros complejos
    (mat, mat) -> mat
    """
    result = []
    if len(A) != len(B):
        print("las matrices no tienen las mismas dimensiones")
    else:
        for j in range(len(A)):
            for k in range(len(A)):
                suma_mat = A[j][k] + B[j][k]
                result.append(suma_mat)
    return result


def inv_mat_cplx(A):
    """negacion de una matriz de numeros complejos
    (mat) -> mat
    """
    for j in range(len(A)):
        for k in range(len(A)):
            A[j][k] = -A[j][k]
    return A


def mult_esc_mat_cplx(p, A):
    """multiplicacion de escalar por matriz compleja
    (cplx, mat) -> mat
    """
    for j in range(len(A)):
        for k in range(len(A)):
            A[j][k] = p * (A[j][k])
    return A


def mat_tra_cplx(A):
    """transpuesta de una matriz
    (mat) -> mat
    """
    A = np.transpose(A)
    return A


def mat_conj_cplx(A):
    """conjugada de una matriz
    (mat) -> mat
    """
    A = np.conjugate(A)
    return A


def mat_adj_cplx(A):
    """adjunta de una matriz
    (mat) -> mat
    """
    A = mat_conj_cplx(A)
    A = mat_tra_cplx(A)
    return A


def prod_mat(A, B):
    """producto de dos matrices
    (mat, mat) -> mat
    """
    producto = np.dot(A, B)
    return producto


def acc_mat_vect(A, v):
    """accion de una matriz sobre un vector
    (mat, vect) -> real
    """
    prod_esca = np.dot(A, v)
    return prod_esca


def prod_int_vect(v1, v2):
    """producto interno de dos vectores
    (vect, vect) -> cplx
    """
    prod_interno = np.dot(np.conjugate(v1), v2)
    return prod_interno


def norma_vect(v):
    """calcula la norma de un vector complejo
    (vect) -> real
    """
    nor_vect = np.linalg.norm(v)
    return nor_vect


def dis_vect(v1, v2):
    """calcula la distancia entre dos vectores complejos
    (vect, vect) -> real"""
    dist = np.linalg.norm(v1 - v2)
    return dist


def val_vect_pro_mat(A):
    """valores y vectores propios de una matriz
    (mat) -> mat, mat
    """
    val_pro, vect_prop = np.linalg.eig(A)
    return val_pro, vect_prop


def es_unit(A):
    """revisar si una matriz es unitaria
    (mat) -> mat, str
    """
    A_conj_tras = np.conjugate(A.T)
    prod = np.dot(A, A_conj_tras)
    A_iden = np.identity(A.shape[0], dtype=complex)
    unit = np.allclose(prod, A_iden)
    if unit:
        return A, print("La matriz es unitaria")
    else:
        return A, print("La matriz no es unitaria")


def es_hermi(A):
    """revisar si una matriz es hermitiana
    (mat) -> mat, str
    """
    A_conj_tras = np.conjugate(A.T)
    hermi = np.allclose(A, A_conj_tras)
    if hermi:
        return A, print("La matriz es hermitiana")
    else:
        return A, print("La matriz no es hermitiana")


def prod_tensor(A, B):
    """producto tensor entre dos matrices o vectores
    (mat, mat) -> mat
    """
    produc_tens = np.kron(A, B)
    return produc_tens
