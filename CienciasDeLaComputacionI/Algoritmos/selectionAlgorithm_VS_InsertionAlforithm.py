# VER LA UTILIDAD DE LOS ALGORITMOS DE ORDENAMIENTO SELECTION Y INSERTION EN ARREGLOS ALEATORIOS
import random

ordenedArr= list(range(1, 101))
randomArr= ordenedArr.copy()
random.shuffle(randomArr)
reversedArr= list(range(100, 0, -1))

# Algoritmo de Selection
def selectionSort(arr, pasos = 0, ciclos = 0):
    arrLen = len(arr)
    pasos += 1  
    for i in range(arrLen):
        minIndex = i
        ciclos += 1
        pasos += 1  
        for j in range(i + 1, arrLen):
            pasos += 1 
            if arr[j] < arr[minIndex]:
                minIndex = j
                pasos += 1 
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
        pasos += 1
    return arr, pasos, ciclos

# Algoritmo de Insertion
def insertionSort(arr, pasos = 0, ciclos = 0):
    arrLen = len(arr)
    pasos += 1 
    for i in range(1, arrLen):
        key = arr[i]
        j = i - 1
        ciclos += 1
        pasos += 2  
        while j >= 0 and key < arr[j]:
            pasos += 1  
            arr[j + 1] = arr[j]
            j -= 1
            pasos += 2  
        pasos += 1 
        arr[j + 1] = key
        pasos += 1
    return arr, pasos, ciclos

# Pasamos ambos arreglos por los algoritmos de Selection y Insertion y contamos pasos y ciclos
selectionArrOrdened, selectionPasosOne, selectionCiclosOne = selectionSort(ordenedArr.copy())
selectionArrRandom, selectionPasosTwo, selectionCiclosTwo = selectionSort(randomArr.copy())
selectionArrReversed, selectionPasosTree, selectionCiclosTree = selectionSort(reversedArr.copy())
insertionArrOrdened, insertionPasosOne, insertionCiclosOne = insertionSort(ordenedArr.copy())
insertionArrRandom, insertionPasosTwo, insertionCiclosTwo = insertionSort(randomArr.copy())
insertionArrReversed, insertionPasosTree, insertionCiclosTree = insertionSort(reversedArr.copy())
# Imprimimos los resultados
print("\n*** RESULTADOS DE ALGORITMO DE SELECTION:")
print("1. Arreglo Ordenado:", "\n- Pasos:", selectionPasosOne, "\n- Ciclos:", selectionCiclosOne)
print("\n 2. Arreglo Aleatorio:", "\n- Pasos:", selectionPasosTwo, "\n- Ciclos:", selectionCiclosTwo)
print("\n3. Arreglo Reverso:", "\n- Pasos:", selectionPasosTree, "\n- Ciclos:", selectionCiclosTree)
print("\n\n*** RESULTADOS DEL ALGORITMO DE INSERTION:")
print("1. Arreglo Ordenado:", "\n- Pasos:", insertionPasosOne, "\n- Ciclos:", insertionCiclosOne)
print("\n 2. Arreglo Aleatorio:", "\n- Pasos:", insertionPasosTwo, "\n- Ciclos:", insertionCiclosTwo)
print("\n3. Arreglo Reverso:", "\n- Pasos:", insertionPasosTree, "\n- Ciclos:", insertionCiclosTree)


# Introducción
# Codigo
# Resultados
# Conclusiones -> Notación Gran 0, Gran omega, Gran Theta, eficiencia de los algoritmos, casos mejores, peores y promedio. -> Cual de los dos es el mejor algoritmo para cada caso.