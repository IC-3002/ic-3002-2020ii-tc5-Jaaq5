
#Tarea corta 05
#Analisis de algoritmos
#Jose Alexander Artavia Quesada
#2015098028


def burbuja(A):
    n = len(A)
    for i in range(1, n):
        for j in range(0, n - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)


def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp
#------------------------------------------------------------------------------------------#

'''
	Funcion que realiza el algoritmo de ordenamiento
	burbuja, con un booleano de condicional si la lista no
	realiza cambios de posicion
	E: una lista de n de largo
	S: la lista  ordenada ascendentemente
	R: entrada tipo list

'''

def burbuja_optimizado(lista):
    largo_lista = len(lista)
    lista_ordenada = True
    for i in range(1, largo_lista):
        for j in range(0, largo_lista - i):
            if lista[j] > lista[j + 1]:
                swap(lista, j, j + 1)
                lista_ordenada = False
        if lista_ordenada == True:
            return lista

    return lista
    raise NotImplementedError()
   
#print(burbuja_optimizado([2,1,4,5,77,88,9]))

