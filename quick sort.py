import matplotlib.pyplot as plt
import numpy as np
import time

def atualizar_grafico(dados, ax, cores, tempo, algoritmo):
    ax.cla()
    ax.bar(range(len(dados)), dados, color=cores)
    ax.set_title(f"{algoritmo} - Tempo: {tempo:.2f} s")  # Mostra o tempo no título
    ax.set_ylabel(algoritmo)  # Nome do algoritmo fixo no eixo Y
    ax.set_ylim(0, max(dados) + 10)  # Define limite superior fixo para visualização
    plt.pause(0.001)

def particionar(dados, inicio, fim, ax, algoritmo):
    pivo = dados[fim]
    i = inicio - 1
    cores = ['maroon'] * len(dados)

    for j in range(inicio, fim):
        if dados[j] < pivo:
            i += 1
            dados[i], dados[j] = dados[j], dados[i]
            cores[i], cores[j] = 'purple', 'purple'
            atualizar_grafico(dados, ax, cores, time.time() - start_time, algoritmo)
            cores[i], cores[j] = 'maroon', 'maroon'

    dados[i + 1], dados[fim] = dados[fim], dados[i + 1]
    atualizar_grafico(dados, ax, ['maroon'] * len(dados), time.time() - start_time, algoritmo)
    return i + 1

def quick_sort(dados, inicio, fim, ax, algoritmo):
    if inicio < fim:
        pi = particionar(dados, inicio, fim, ax, algoritmo)
        quick_sort(dados, inicio, pi - 1, ax, algoritmo)
        quick_sort(dados, pi + 1, fim, ax, algoritmo)

def merge(dados, esquerda, meio, direita, ax, algoritmo):
    left = dados[esquerda:meio + 1]
    right = dados[meio + 1:direita + 1]
    i = j = 0
    k = esquerda
    cores = ['maroon'] * len(dados)

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            dados[k] = left[i]
            i += 1
        else:
            dados[k] = right[j]
            j += 1
        cores[k] = 'purple'
        atualizar_grafico(dados, ax, cores, time.time() - start_time, algoritmo)
        k += 1

    while i < len(left):
        dados[k] = left[i]
        i += 1
        k += 1
        cores[k - 1] = 'purple'
        atualizar_grafico(dados, ax, cores, time.time() - start_time, algoritmo)

    while j < len(right):
        dados[k] = right[j]
        j += 1
        k += 1
        cores[k - 1] = 'purple'
        atualizar_grafico(dados, ax, cores, time.time() - start_time, algoritmo)

def merge_sort(dados, esquerda, direita, ax, algoritmo):
    if esquerda < direita:
        meio = (esquerda + direita) // 2
        merge_sort(dados, esquerda, meio, ax, algoritmo)
        merge_sort(dados, meio + 1, direita, ax, algoritmo)
        merge(dados, esquerda, meio, direita, ax, algoritmo)

def heapify(dados, n, i, ax, algoritmo):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2
    cores = ['maroon'] * len(dados)

    if esquerda < n and dados[esquerda] > dados[maior]:
        maior = esquerda

    if direita < n and dados[direita] > dados[maior]:
        maior = direita

    if maior != i:
        dados[i], dados[maior] = dados[maior], dados[i]
        cores[i], cores[maior] = 'purple', 'purple'
        atualizar_grafico(dados, ax, cores, time.time() - start_time, algoritmo)
        heapify(dados, n, maior, ax, algoritmo)

def heap_sort(dados, ax, algoritmo):
    n = len(dados)
    for i in range(n // 2 - 1, -1, -1):
        heapify(dados, n, i, ax, algoritmo)

    for i in range(n - 1, 0, -1):
        dados[i], dados[0] = dados[0], dados[i]
        atualizar_grafico(dados, ax, ['purple' if j <= i else 'maroon' for j in range(len(dados))], time.time() - start_time, algoritmo)
        heapify(dados, i, 0, ax, algoritmo)

def insertion_sort(dados, ax, algoritmo):
    for i in range(1, len(dados)):
        chave = dados[i]
        j = i - 1
        cores = ['maroon'] * len(dados)

        while j >= 0 and chave < dados[j]:
            dados[j + 1] = dados[j]
            j -= 1
            cores[j + 1] = 'purple'
            atualizar_grafico(dados, ax, cores, time.time() - start_time, algoritmo)

        dados[j + 1] = chave
        cores[j + 1] = 'purple'
        atualizar_grafico(dados, ax, cores, time.time() - start_time, algoritmo)

def visualizar_algoritmos(dados):
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    axs = axs.flatten()
    
    plt.ion()
    
    global start_time

    dados_quick = dados.copy()
    dados_merge = dados.copy()
    dados_heap = dados.copy()
    dados_insertion = dados.copy()

    start_time = time.time()
    quick_sort(dados_quick, 0, len(dados_quick) - 1, axs[0], "Quick Sort")
    quick_time = time.time() - start_time

    start_time = time.time()
    merge_sort(dados_merge, 0, len(dados_merge) - 1, axs[1], "Merge Sort")
    merge_time = time.time() - start_time

    start_time = time.time()
    heap_sort(dados_heap, axs[2], "Heap Sort")
    heap_time = time.time() - start_time

    start_time = time.time()
    insertion_sort(dados_insertion, axs[3], "Insertion Sort")
    insertion_time = time.time() - start_time

    axs[0].set_title(f"Quick Sort - Tempo: {quick_time:.2f} s")
    axs[1].set_title(f"Merge Sort - Tempo: {merge_time:.2f} s")
    axs[2].set_title(f"Heap Sort - Tempo: {heap_time:.2f} s")
    axs[3].set_title(f"Insertion Sort - Tempo: {insertion_time:.2f} s")

    plt.ioff()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    np.random.seed(0)
    dados = np.random.randint(1, 100, 50)
    visualizar_algoritmos(dados)
