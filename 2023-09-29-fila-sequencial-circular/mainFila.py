from FilaSequencialCircularNumPy import * 
# Importando a classe Fila do módulo FilaSequencialCircularNumPy

# Criação de uma instância f da classe Fila; é a fila que será manipulada 
f = Fila()


if f.estaVazia():
    print('Fila esta vazia.')

print('Tamanho da fila:', len(f))

# Um loop for é usado para enfileirar (adicionar) elementos à fila f. 
# O loop adiciona os números 10, 20, 30, até 70 à fila, multiplicando i por 10 em cada iteração.
try:
    for i in range(1,8):
        f.enfileira(i*10)
    print('Tamanho da fila:', len(f))
    print(f)

    # Tentativa de enfileirar o elemento 55 à fila f. 
    # Como a fila já está cheia (porque o tamanho máximo padrão é 10 e já adicionaram 7 elementos),
    # isso deve levantar uma exceção FilaException
    f.enfileira(55)
    print('Tamanho da fila:', len(f))
    print(f)

    # Desenfileira (remove) o primeiro elemento da fila f e o armazena na variável 'carga'
    carga = f.desenfileira()
    print('Carga removida:', carga)
    print(f) 
    # Imprime a carga (elemento removido) e o conteúdo atual da fila após a operação de desenfileirar.

    # Chama o método elemento(3) para obter o elemento na terceira posição da fila (lembrando que a posição começa em 1) e o armazena na variável 'conteudo'
    conteudo = f.elemento(3)
    print(f'Elemento(3): {conteudo}')
    # Chama o método busca(50) para procurar o elemento 50 na fila e armazena a posição da primeira ocorrência na variável 'posicao'
    posicao = f.busca(50)
    print(f'Posicao do elemento 50: {posicao}')

    # Você inicia um loop que tentará remover 15 elementos da fila f. 
    # Mas a fila já está vazia após as operações anteriores, isso deve levantar exceções 'FilaException'
    for i in range(15):
        print('removendo:', f.desenfileira())
    print(f)
    # Tentativa de desenfileirar 15 elementos da fila em um loop e imprimir "removendo" junto com cada elemento removido. 
    # Depois disso, imprime o conteúdo da fila novamente (que deve estar vazia).
except FilaException as ae: 
# Exceções do tipo 'FilaException' que podem ser levantadas durante as operações na fila; imprime a mensagem de exceção
    print(ae)
print(f)

# Em resumo, este código demonstra várias operações em uma fila sequencial circular, 
# como enfileirar, desenfileirar, verificar se está vazia, buscar elementos e lidar com exceções específicas da fila. 
# Ele serve como um exemplo de como usar a classe Fila que foi definida anteriormente.