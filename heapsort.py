#!/usr/bin/python
# -*- coding: UTF-8 -*-

# A função "Estrutura" cria uma subárvore utilizando a raíz como índice 
# O parâmetro "tamanho" é o tamanho da árvore heap
def Estrutura(vetor, tamanho, indice): 
    maior = indice  # Initializando maior como raíz da árvore
    esq = 2 * indice + 1    # O resultado da operação é o índice a esquerda
    di= 2 * indice + 2     # O resultado da operação é o índice a direita
  
    # Verifica se o filho a esquerda existe e se é maior que a raíz
    if esq < tamanho and vetor[indice] < vetor[esq]: 
       maior = esq 
  
    # Verifica se o filho a direita existe e se é maior que a raíz
    if di < tamanho and vetor[maior] < vetor[di]: 
       maior = di 
  
    #Muda a raíz quando for necessário
    if maior != indice: 
        vetor[indice],vetor[maior] = vetor[maior],vetor[indice]  #troca raíz 
  
        # Cria a subárvore 
        Estrutura(vetor, tamanho, maior) 
        
  
# Função principal que irá ordenar o vetor 
def HEAPsort(vetor): 
    tamanho = len(vetor) 
  
    # Contrói a "árvore heap máxima", de acordo com o tamanho do vetor de entrada.
    # Como o último pai estará no nível ((n//2)-1), comecei por esta posição.
    for indice in range((tamanho//2)-1, -1, -1): 
        Estrutura(vetor, tamanho, indice) 
  
    # Extrai os elementos do vetor um por um
    for indice in range(tamanho-1, 0, -1): 
        vetor[indice], vetor[0] = vetor[0], vetor[indice]   #inverte os elementos
        Estrutura(vetor, indice, 0) 
  
def Mostrar(vetor):
     tamanho = len(vetor) 
     print ("O vetor ordenado fica:") 
     for indice in range(tamanho): 
         print ("%d" %vetor[indice]), 
         
# Chamando as funções e definindo o vetor de entrada
def main():
    
    print("Iniciando o algorítmo de ordenação HeapSort...\n")         
    vetor = [ 9 , 10 , -1, 3, 6, 2, 1, -3, 1, 0, -2, 15, 8, -7, 0] 
    HEAPsort(vetor) 
    Mostrar(vetor)

if __name__ == "__main__":
    main()