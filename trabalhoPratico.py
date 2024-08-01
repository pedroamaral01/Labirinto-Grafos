from collections import deque
import time

def leArquivo(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as arq:
        labirinto = [list(line.strip()) for line in arq]
    return labirinto

def definiInicioFim(labirinto):
    inicio, fim = None, None
    for i, row in enumerate(labirinto):
        for j, char in enumerate(row):
            if char == 'S':
                inicio = (i, j)
            elif char == 'E':
                fim = (i, j)
    return inicio, fim

def moverCima(posicaoAtual, labirinto):
    x, y = posicaoAtual
    if x > 0 and labirinto[x-1][y] not in ('#', '█'):
        return (x-1, y)
    return posicaoAtual  

def moverBaixo(posicaoAtual, labirinto):
    x, y = posicaoAtual
    if x < len(labirinto) - 1 and labirinto[x+1][y] not in ('#', '█'):
        return (x+1, y)
    return posicaoAtual

def moverEsquerda(posicaoAtual, labirinto):
    x, y = posicaoAtual
    if y > 0 and labirinto[x][y-1] not in ('#', '█'):
        return (x, y-1)
    return posicaoAtual

def moverDireita(posicaoAtual, labirinto):
    x, y = posicaoAtual
    if y < len(labirinto[0]) - 1 and labirinto[x][y+1] not in ('#', '█'):
        return (x, y+1)
    return posicaoAtual

def buscaEmLargura(labirinto, inicio, fim):
    armazena = deque([inicio])
    visitado = set([inicio])
    parente = {inicio: None}

    while armazena:
        posicaoAtual = armazena.popleft()
        if posicaoAtual == fim:
            break

        # Movimentos possíveis
        movimentos = [
            moverCima(posicaoAtual, labirinto),
            moverBaixo(posicaoAtual, labirinto),
            moverEsquerda(posicaoAtual, labirinto),
            moverDireita(posicaoAtual, labirinto)
        ]

        for novaPosicao in movimentos:
            if novaPosicao not in visitado and novaPosicao != posicaoAtual:
                armazena.append(novaPosicao)
                visitado.add(novaPosicao)
                parente[novaPosicao] = posicaoAtual

    caminho = []
    if fim in parente:
        passo = fim
        while passo is not None:
            caminho.append(passo)
            passo = parente[passo]
        caminho.reverse()

    return caminho if caminho else "Caminho não encontrado."

def buscaEmProfundidade(labirinto, inicio, fim):
    pilha = [inicio]
    visitado = set([inicio])
    parente = {inicio: None}
    
    while pilha:
        posicaoAtual = pilha.pop()
        if posicaoAtual == fim:
            break

        # Movimentos possíveis
        movimentos = [
            moverCima(posicaoAtual, labirinto),
            moverBaixo(posicaoAtual, labirinto),
            moverEsquerda(posicaoAtual, labirinto),
            moverDireita(posicaoAtual, labirinto)
        ]

        for novaPosicao in movimentos:
            if novaPosicao not in visitado and novaPosicao != posicaoAtual:
                pilha.append(novaPosicao)
                visitado.add(novaPosicao)
                parente[novaPosicao] = posicaoAtual

    caminho = []
    if fim in parente:
        passo = fim
        while passo is not None:
            caminho.append(passo)
            passo = parente[passo]
        caminho.reverse()

    return caminho if caminho else "Caminho não encontrado."

def main():
    while True:
        arquivo = input("Informe o arquivo (0 para sair): ")
        if arquivo == '0':
            break

        try:
            labirinto = leArquivo(arquivo)
            inicio, fim = definiInicioFim(labirinto)
            
            print("Processando com Busca em Largura...")
            start_time = time.time()
            caminhoLargura = buscaEmLargura(labirinto, inicio, fim)
            buscaL_time = time.time() - start_time
            print("Caminho Busca em Largura:", caminhoLargura)
            print("Tempo Busca em Largura: {:.5f} s".format(buscaL_time))
            
            print("\nProcessando com Busca em Profundidade...")
            start_time = time.time()
            caminhoProfundidade = buscaEmProfundidade(labirinto, inicio, fim)
            buscaL_time = time.time() - start_time
            print("Caminho Busca em Profundidade:", caminhoProfundidade)
            print("Tempo Busca em Profundidade: {:.5f} s".format(buscaL_time))

        except FileNotFoundError:
            print("Arquivo não encontrado. Tente novamente.")

if __name__ == "__main__":
    main()
