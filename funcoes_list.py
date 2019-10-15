# Autoras: Caroline Taus e Rebecca Mello

#Função para printar os elementos válidos do vetor:
def printaVetor(vetor,qtd): 
   print("\nVetor = [",end=' ')
   for i in range(qtd):
      print( vetor[i],end=' ')
   
   print("]\n")

#Função da escolha 1
def addFinal(vetor, qtd, elem):
    if qtd < 100:            #verifica se há posições livres
      vetor[qtd] = elem      #adiciona o elem na última posição livre
      qtd = qtd + 1               #passa o qtd para a nova ultima posição livre
    else:
      print("Não há posições livres.")
    return qtd               #return qtd para que a atualização em seu valor seja passada para outras funções

#Função da escolha 2
def addPos(vetor, posicao, elem, qtd):
  if qtd < 100:              #verifica se há posições livres
    if posicao == qtd:       #verifica se é para colocar no final
      vetor[posicao] = elem
      qtd = qtd + 1
    
    else:
      for i in range(qtd, posicao, -1):
        vetor[i] = vetor[i - 1]
      
      vetor[posicao] = elem
      qtd = qtd + 1

  return qtd

#Função da escolha 3 
def remove(vetor, posicao, qtd):
  for i in range(posicao + 1, qtd):
    vetor[posicao] = vetor[posicao + 1]   # a posicao digitada recebe o numero da direita 
    posicao = posicao + 1                 #acrescenta um na posicao para que continue a acao anterior ate acabar o vetor
    
  qtd = qtd - 1
  return qtd

#Função da escolha 4
def removePrimeira(vetor, elem, qtd):
  index = 0                     #index do elemento retirado

  for i in range(qtd):
    if vetor[i] == elem:
      index = i
      qtd = qtd - 1


      while index < qtd:  
        vetor[index] = vetor[index + 1]
        index = index + 1
      
      break
  
  return qtd

#Função da escolha 5
def removeTodas(vetor, elem, qtd):
  cont = 0                   #contador
  for x in range(qtd):       #for para contar quantos elementos do vetor são iguais ao elemento de entrada
    if vetor [x] == elem:
      cont = cont + 1

  for i in range (cont):     #chama função de remover um elemento o número de vezes do contador
    removePrimeira(vetor,elem,qtd)
    
  qtd = qtd - cont           #diminui qtd na quantidade de elementos retirados do vetor
       
  return qtd
  
#Função da escolha 6
def verifica(vetor, elem, qtd):
  conta = 0                  #contador que verifica se é diferente dos elementos

  for i in range(qtd):
    if vetor[i] == elem:
      print('O elemento está inserido no indice', i)
    else:
      conta = conta + 1
  
  if conta == qtd:           #caso o numero seja diferente de todos do vetor
    print('-1') 
  return qtd

#Função da escolha 7
def verSoma(vetor, soma, qtd):
  for i in range(qtd - 1):
    
    for r in range(i + 1, qtd):     #compara o elemento de indice i com todos os seguintes no vetor 
      if vetor[i] + vetor[r] == soma: 
        return True
        
  return False
  

def main():
  vetor = [0] * 100           #criação do vetor inicial
  opcao = 0
  qtd = 0                     #quantidade de elementos validos

  #Menu de Opções
  while opcao != 8:
    print('1 - Adicionar um elemento no final da coleção')
    print('2 - Adicionar um elemento em uma posição')
    print('3 - Remover um elemento de uma determinada posição')
    print('4 - Remover a primeira ocorrência de elemento na coleção')
    print('5 - Remover todas as ocorrências de um elemento')
    print('6 - Verificar se está contido')
    print('7 - Verificar se existem dois elementos que somados dá o valor informado')
    print('8 - Sair')
    print('\nDigite a opcao desejada:')
    opcao = int(input())

    if opcao == 1:
      print("Insira o elemento que deseja adicionar ao final:")
      elem = int(input())
      qtd = addFinal(vetor, qtd, elem) #atualiza o valor de qtd
      printaVetor(vetor,qtd)
      

    elif opcao == 2:
      print("Insira o elemento:")
      elem = int(input())
      print("Insira a posição:")
      posicao = int(input())
      qtd = addPos(vetor, posicao, elem, qtd)
      printaVetor(vetor,qtd)

    elif opcao == 3:
      print('Informe a posição:')
      posicao = int(input())
      qtd = remove(vetor, posicao, qtd)
      printaVetor(vetor,qtd)

    elif opcao == 4:
      print('Digite o elemento:')
      elem = int(input())
      qtd = removePrimeira(vetor, elem, qtd)
      printaVetor(vetor,qtd)

    elif opcao == 5:
      print('Digite o elemento:')
      elem = int(input())
      qtd = removeTodas(vetor, elem, qtd)
      printaVetor(vetor,qtd)

    elif opcao == 6:
      print('Digite o elemento:')
      elem = int(input())
      qtd = verifica(vetor, elem, qtd)
      printaVetor(vetor,qtd)

    elif opcao == 7:
      print('Insira o valor da soma:')
      soma = int(input())
      print(verSoma(vetor, soma, qtd))
      print()

    elif opcao > 8:           #caso o usuario digite uma opcao que nao esta no menu
      print('\nEscolha uma opção válida:')
      print("")
      print("-------------------------------------------")
  
  print("\n")
  print('########## FIM DO PROGRAMA ##########')
    
main() 
