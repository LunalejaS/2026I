# EJERCICIO PARA CONTAR PASOS Y CICLOS DEL ALGORITMO DE BUBBLE 
import random

# Generamos 3 arreglos como test para el algoritmo de Bubble
ordenedArr= list(range(1, 101))
randomArr= ordenedArr.copy()
random.shuffle(randomArr)
reversedArr= list(range(100, 0, -1))

# Definimos el algoritmo de Bublee y contamos pasos y ciclos
arrList = [ordenedArr, randomArr, reversedArr]
arrNames = ["Arreglo Ordenado", "Arreglo Aleatorio", "Arreglo Invertido"]
for i in range(3):
    arr = arrList[i].copy()
    nameArr = arrNames[i]
    steps = 1 
    cycles = 0
    arrLen = len(arr)
    
    # Comparamos hasta que el ciclo externo se ejecuta 99 veces (no 100), porque la ultima comparación se hace en el ciclo interno
    for j in range(arrLen - 1):
        # Por cada iteración del ciclo externo, se cuenta:
        # 1 paso: Verficar la condición del ciclo externo
        # 1 paso: Incrementar el contador del ciclo externo
        # 1 paso: Iniciar el ciclo interno
        steps += 3
        for k in range(0, arrLen - j - 1):
            # Por cada iteración del ciclo interno, se cuenta:
            # 1 paso: Verificar la condición del ciclo interno
            # 1 paso: Incrementar el contador del ciclo interno
            # 1 ciclo: Ejecutar el bloque del ciclo interno
            cycles += 1
            steps += 2
            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]
                # El swap cuenta como 3 operaciones: 1 para guardar el valor de arr[k] en una variable temporal, 1 para asignar el valor de arr[k + 1] a arr[k], y 1 para asignar el valor de la variable temporal a arr[k + 1]
                steps += 3
            # Un ultimo paso que termina el ciclo interno, ya sea porque se cumple la condición o porque no se cumple y se sigue iterando
            steps += 1
    print(f"\n{nameArr}:")
    print(f"- Pasos: {steps}")
    print(f"- Ciclos: {cycles}")