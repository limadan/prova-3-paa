import time
import matplotlib.pyplot as plt
import numpy as np

# Funções úteis
def valida_casa(i, j, tabuleiro, n):
    """Verifica se a posição i, j é válida e não foi visitada."""
    return 0 <= i < n and 0 <= j < n and tabuleiro[i][j] == -1

def resolver_passo(i, j, movimento_i_atual, tabuleiro, movimento_i, movimento_j, n, comparacoes, movimentos):
    """Função recursiva que tenta resolver o passeio do cavalo."""
    if movimento_i_atual == n * n:
        return True, comparacoes, movimentos

    for k in range(8):
        comparacoes += 1
        proximo_i = i + movimento_i[k]
        proximo_j = j + movimento_j[k]

        if valida_casa(proximo_i, proximo_j, tabuleiro, n):
            tabuleiro[proximo_i][proximo_j] = movimento_i_atual
            movimentos += 1

            sucesso, comparacoes, movimentos = resolver_passo(proximo_i, proximo_j, movimento_i_atual + 1, tabuleiro, movimento_i, movimento_j, n, comparacoes, movimentos)
            if sucesso:
                return True, comparacoes, movimentos

            # Backtracking
            tabuleiro[proximo_i][proximo_j] = -1
            movimentos += 1

    return False, comparacoes, movimentos

def resolver_passeio_do_cavalo(n, inicio_i, inicio_j):
    """Tenta resolver o passeio do cavalo a partir da posição inicial."""
    # Movimentos possíveis do cavalo
    movimento_i = [2, 1, -1, -2, -2, -1, 1, 2]
    movimento_j = [1, 2, 2, 1, -1, -2, -2, -1]

    # Inicializa o tabuleiro com -1 (não visitado)
    tabuleiro = [[-1 for _ in range(n)] for _ in range(n)]

    # Número de comparações e movimentos
    comparacoes = 0
    movimentos = 0

    # Posiciona o cavalo na posição inicial
    tabuleiro[inicio_i][inicio_j] = 0
    movimentos += 1

    # Chama a função recursiva para resolver o passeio
    inicio_tempo = time.time()
    sucesso, comparacoes, movimentos = resolver_passo(inicio_i, inicio_j, 1, tabuleiro, movimento_i, movimento_j, n, comparacoes, movimentos)
    if(sucesso):
        print("Sucesso ao encontrar solução")
        print(tabuleiro)
    else:
        print("Não há solução")
    fim_tempo = time.time()

    tempo_gasto = fim_tempo - inicio_tempo

    return sucesso, movimentos, comparacoes, tempo_gasto

# Simulações e coleta de dados
def simular_varias_casas_iniciais(tamanho, casas_iniciais):
    """Simula o passeio do cavalo para diferentes casas iniciais em um tabuleiro 8x8."""
    resultados = np.zeros((10, 4))  # Matriz 10x4 para armazenar os resultados

    for idx, casa_inicial in enumerate(casas_iniciais):
        i_inicial, j_inicial = casa_inicial
        print(f"Simulando para casa inicial: ({i_inicial}, {j_inicial}) no tabuleiro {tamanho}x{tamanho}")
        sucesso, movimentos, comparacoes, tempo_gasto = resolver_passeio_do_cavalo(tamanho, i_inicial, j_inicial)
        
        # Armazenando os resultados na matriz
        resultados[idx, 0] = i_inicial * tamanho + j_inicial  # Convertendo (i, j) em uma única posição
        resultados[idx, 1] = movimentos
        resultados[idx, 2] = comparacoes
        resultados[idx, 3] = tempo_gasto
    
    return resultados

# Plotagem dos gráficos
def plotar_resultados_matriz(resultados):
    """Plota gráficos baseados na matriz de resultados."""
    casas_iniciais = resultados[:, 0]
    movimentos = resultados[:, 1]
    comparacoes = resultados[:, 2]
    tempos = resultados[:, 3]

    plt.figure(figsize=(15, 5))

    # Gráfico de casa inicial x Movimentações
    plt.subplot(1, 3, 1)
    plt.plot(casas_iniciais, movimentos, marker='o', label="Movimentações")
    plt.title("Casa Inicial vs Movimentações")
    plt.xlabel("Casa Inicial")
    plt.ylabel("Movimentações")
    plt.grid(True)

    # Gráfico de casa inicial x Comparações
    plt.subplot(1, 3, 2)
    plt.plot(casas_iniciais, comparacoes, marker='o', label="Comparações", color='orange')
    plt.title("Casa Inicial vs Comparações")
    plt.xlabel("Casa Inicial")
    plt.ylabel("Comparações")
    plt.grid(True)

    # Gráfico de casa inicial x Tempo computacional
    plt.subplot(1, 3, 3)
    plt.plot(casas_iniciais, tempos, marker='o', label="Tempo Computacional", color='green')
    plt.title("Casa Inicial vs Tempo Computacional")
    plt.xlabel("Casa Inicial")
    plt.ylabel("Tempo (segundos)")
    plt.grid(True)

    plt.tight_layout()
    plt.show()
    """Plota gráficos baseados na matriz de resultados."""
    casas_iniciais = resultados[:, 0]
    movimentos = resultados[:, 1]
    comparacoes = resultados[:, 2]
    tempos = resultados[:, 3]

    plt.figure(figsize=(15, 5))

    # Gráfico de casa inicial x Movimentações
    plt.subplot(1, 3, 1)
    plt.plot(casas_iniciais, movimentos, marker='o', label="Movimentações")
    plt.title("Casa Inicial vs Movimentações")
    plt.xlabel("Casa Inicial")
    plt.ylabel("Movimentações")
    plt.grid(True)

    # Gráfico de casa inicial x Comparações
    plt.subplot(1, 3, 2)
    plt.plot(casas_iniciais, comparacoes, marker='o', label="Comparações", color='orange')
    plt.title("Casa Inicial vs Comparações")
    plt.xlabel("Casa Inicial")
    plt.ylabel("Comparações")
    plt.grid(True)

    # Gráfico de casa inicial x Tempo computacional
    plt.subplot(1, 3, 3)
    plt.plot(casas_iniciais, tempos, marker='o', label="Tempo Computacional", color='green')
    plt.title("Casa Inicial vs Tempo Computacional")
    plt.xlabel("Casa Inicial")
    plt.ylabel("Tempo (segundos)")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Definir as 10 casas iniciais arbitrárias para o tabuleiro 8x8
casas_iniciais = [(0, 7), (7, 0)]

# Executa as simulações
resultados_matriz = simular_varias_casas_iniciais(8, casas_iniciais)

# Exibe os resultados
print("Matriz de resultados (Casa Inicial, Movimentos, Comparações, Tempo Computacional):")
print(resultados_matriz)

# Plota os gráficos baseados nos resultados da matriz
plotar_resultados_matriz(resultados_matriz)
