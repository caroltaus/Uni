#Autoras: Caroline Taus e Rebecca Mello

# Função para printar o polinômio
def printaPoli(pol,grau):
  print()
  for x in range(grau,-1,-1):                            # percorre o vetor de trás para frente
    if pol[x] !=0:                                       # se a base for diferente de 0
      if x > 1:                                          # se o expoente for maior que 1 aparece o X e o expoente
        print("("+str(pol[x])+"X^"+str(x)+")",end="+")
      elif x == 1:                                       # se o expoente for 1 aparece apenas o X
        print("("+str(pol[x])+"X"+")",end="+")
      elif x == 0:                                       # se o expoente for 0 aparece apenas a base
        print("("+str(pol[x])+")",end="")

# Função da Opção 1 - Valor
def valor(pol1, x):
  conta = 0
  for i in range(len(pol1)):
    conta = conta + pol1[i] * (x ** i)  #eleva o numero digitado pelo índice e multiplica o resultado por número do vetor do polinomio  
  
  return conta

# Função da Opção 2 - Soma
def soma(pol1, pol2, grau1, grau2):
  j = 0

  if grau1 < grau2:                     # se o grau do primeiro polinômio for menor que o do segundo
    vetor = [0] * len(pol2)             # cria o vetor do tamanho do segundo polinômio

    for i in range(len(pol1)):          # realiza o laço com o tamanho do primeiro vetor
      conta = pol1[i] + pol2[j]         # soma os números com mesmo índice
      vetor[i] = conta                  # põe no novo vetor o resultado
      j = j + 1                         # acrescenta um no índice do segundo vetor
    
    while j < len(vetor):               # até acabar o segundo vetor para completar o novo
      vetor[j] = pol2[j]                # coloca o número do segundo vetor no novo
      j = j + 1                       

  else:                                 # caso o segundo vetor seja menor que o primeiro
    vetor = [0] * len(pol1)

    for i in range(len(pol2)):
      conta = pol2[i] + pol1[j]
      vetor[i] = conta 
      j = j + 1
    
    while j < len(vetor):
      vetor[j] = pol1[j]
      j = j + 1
  
  if grau1 > grau2:
    grau_polinovo = grau1 
  else:
    grau_polinovo = grau2

  printaPoli(vetor,grau_polinovo)       # chama a função de printar o polinômio

#Função da Opção 3 - Multiplicação
def multip(pol1, pol2, grau1, grau2):
  base = 0
  expo = 0
  ind = 0                                     # índice dos vetores vetorbase e vetorexpo
  vetorbase = [0] * (len(pol1) * len(pol2))   # criação do vetor para as bases
  vetorexpo = [0] * (len(vetorbase))          # criação do vetor para os expoentes
  
  for i in range (len(pol1)):
    for j in range (len(pol2)):
      base = pol1[i] * pol2[j]                # bases são multiplicadas
      expo = i + j                            # expoentes são somados
      vetorbase[ind] = base
      vetorexpo[ind] = expo 
      ind = ind + 1
  
  vetortotal = [0] * (grau1+grau2 +1)         # criação do vetor resposta
  grau_vettot = grau1+grau2                   # grau do polinômio resposta será a soma dos graus dos polinômios 1 e 2
  
  expoente = 0 
  soma_base = 0
  for ind_tot in range(len(vetortotal)):
    for c in range (len(vetorexpo)):
      if vetorexpo[c] == expoente: 
        soma_base = soma_base + vetorbase[c]  # soma todas as bases de mesmo expoente
      
      vetortotal[ind_tot] = vetortotal[ind_tot] + soma_base  # coloca a soma das bases no vetor resposta 
      soma_base = 0                           # reseta soma das bases
    expoente = expoente + 1
       
  printaPoli(vetortotal,grau_vettot)          # chama a função de printar o polinômio

# MAIN
def main():
  con = "1"

  while con != "0":
    # entrada do polinômio 1
    print('\nInsira o grau do polinômio que deseja realizar as operações:')
    grau1 = int(input())
    tam_pol1 = grau1+1
    pol1 = [0] * tam_pol1
    
    for x in range (len(pol1)):
      print("\nInsira o número que será multiplicado por X^"+str(x)+":")
      pol1[x] = int(input())

    print("\npolinômio 1:  ",end="")
    printaPoli(pol1,grau1)                   #chama a função de printar o polinômio

    # Menu 
    opc = "1"
    
    print("\n\n-----------------------------------------------")
    print('               Menu de Opções:\n')
    print('1 - Calcular o valor do polinômio')
    print('2 - Calcular a soma dos polinômios')
    print('3 - Calcular a multiplicação dos polinômios')
    print("\n-----------------------------------------------")
    opc = input('\nDigite a opção que deseja: ')

    while opc != "1" and opc != "2" and opc != "3":
      print("\nOpção inválida. Digite uma opção válida.")
      opc = input('\nDigite a opção que deseja: ')

    if opc == "1":
      x = int(input('\nDigite o valor de x: '))
      print("\n\nO valor total é:", valor(pol1, x))
    
    if opc == "2" or opc == "3":

      # entrada do polinômio 2
      print('\nInsira o grau do outro polinômio:')
      grau2 = int(input())
      tam_pol2 = grau2 + 1
      pol2 = [0] * tam_pol2
    
      for x in range (len(pol2)):
        print("\nInsira o número que será multiplicado por X^"+str(x)+":")
        pol2[x] = int(input())

      print()  
      print("\npolinômio 2:  ",end="")
      printaPoli(pol2,grau2)


    if opc == "2":
      print("\n\nA soma dos polinômios resulta em:")
      soma(pol1, pol2,grau1,grau2) # chamada da função de soma
      

    if opc == "3":
      print("\n\nA multiplicação dos polinômios resulta em:")
      multip(pol1, pol2, grau1, grau2)
    print("\n\n################################################")
    print("\nPara sair do programa digite 0, para executar novamente digite qualquer tecla.")
    con = input()
 
main()

