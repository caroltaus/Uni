#jogo_velha.py
#Autora: Caroline Taus

def initialize():   # função para a criação da matriz 3x3
  mat = [" "]* 3 
  for i in range (3):
    mat[i]=[" "]* 3 
  return mat

def printMat(mat):  # função para printar a matriz no formato de tabuleiro
  print("    1    2    3 ")
  for i in range(3):
    print(i+1,end=" ")
    for j in range(3):     
      print("|",mat[i][j],"|",end="")
    print()
    
def step (mat,jogador):    # função que verifica e insere a jogada na posição
  linha = int(input("\n-> Insira a linha: "))
  while (linha!=1 and linha!=2 and linha!=3): # verifica se está nas linhas 1 2 ou 3
     print("Linha inválida. Insira outra posição.")
     linha = int(input("\n-> Insira a linha: "))

  coluna = int(input("-> Insira a coluna: "))
  print()
  while (coluna!=1 and coluna !=2 and coluna !=3): # verifica se está nas colunas 1 2 ou 3
    print("Coluna inválida. Insira outra posição.")
    coluna = int(input("-> Insira a coluna: "))
    print()
    
  while mat[linha-1][coluna-1] == "X" or mat[linha-1][coluna-1] == "O": # verifica se a posição já está ocupada
    print("\nPosição ocupada. Insira outra posição.")
    linha = int(input("\n-> Insira a linha: "))
    while (linha!=1 and linha!=2 and linha!=3): # verifica se está nas linhas 1 2 ou 3
     print("Linha inválida. Insira outra posição.")
     linha = int(input("\n-> Insira a linha: "))
    coluna = int(input("-> Insira a coluna: "))
    while (coluna!=1 and coluna !=2 and coluna !=3): # verifica se está nas colunas 1 2 ou 3
      print("\nColuna inválida. Insira outra posição.")
      coluna = int(input("-> Insira a coluna: "))
  
  mat[linha-1][coluna-1] = jogador #coloca X ou O na posição desejada

  return mat

def status(mat):  #função que verifica se alguém ganhou, se empatou ou se o jogo deve continuar
  
  qtdO_lin = 0 #quantidade de posições ocupadas pelo jogador O em uma mesma linha
  qtdX_lin = 0 #quantidade de posições ocupadas pelo jogador X em uma mesma linha
  qtdO_col = 0 #quantidade de posições ocupadas pelo jogador O em uma mesma coluna
  qtdX_col = 0 #quantidade de posições ocupadas pelo jogador X em uma mesma coluna
  
  
  for i in range(3):  
    for j in range(3):
      if mat[i][j] == "O":  #verificando linhas para jogador O
        qtdO_lin += 1 
        if qtdO_lin == 3:   #se tiver 3 Os em uma mesma linha vitória do jogador O
          return 1

      if mat[i][j] =="X":  #verificando linhas para jogador X
        qtdX_lin += 1
        if qtdX_lin == 3:
          return 2

      if mat[j][i] == "O":  #verificando colunas para jogador O
        qtdO_col += 1
        if qtdO_col == 3:
          return 1

      if mat [j][i] == "X":   #verificando colunas para jogador O
        qtdX_col += 1
        if qtdX_col == 3:
          return 2

    #resetando variáveis
    qtdO_lin,qtdX_lin,qtdO_col,qtdX_col = 0,0,0,0

  #verificando diagonais
  if (mat[0][0] == "O" and mat[1][1] == "O" and mat[2][2] == "O") or (mat[2][0] == "O" and mat[1][1] == "O" and mat[0][2] == "O"):
    return 1
  if (mat[0][0] == "X" and mat[1][1] == "X" and mat[2][2] == "X") or (mat[2][0] == "X" and mat[1][1] == "X" and mat[0][2] == "X"):
    return 2

  #verificando empate
  qtd_ocupados = 0
  for i in range(3): 
    for j in range(3):
      if mat[i][j] == "O" or mat[i][j] == "X":  
        qtd_ocupados += 1 
        if qtd_ocupados == 9: #todas as posições ocupadas sem nenhum ganhador
          return 0


def game():  #função main do jogo
  mat = initialize()
  printMat(mat)
  
  for i in range(9): # jogo roda no máximo 9 vezes
    if i % 2 ==0: #alternando a vez de cada jogador
      print()
      print("***  vez do jogador O  ***")
      jogador = "O"
    else:
      print()
      print("***  vez do jogador X  ***")
      jogador = "X"
    
    
    mat = step (mat,jogador)
    print("-----------------")
    print()
    printMat(mat)
    st = status(mat)  # a cada rodada o status é verificado


    # resultados
    if st == 1:
      print("\n\n      ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆")
      print("            Jogador O venceu!")
      print("      ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆")
      print()
      print("              .-=========-.")
      print("              \-`-=====-´-/")
      print("              _|   .=.   |_")
      print("             ((|  {{O}}  |))")
      print("              \|   /|\   |/")
      print("               \__ '`' __/")
      print("                 _`) (`_")
      print("               _/_______\_")
      print("              /___________\ ")
      break

    elif st == 2:
      print("\n\n      ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆")
      print("            Jogador X venceu!")
      print("      ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆")
      print()
      print("              .-=========-.")
      print("              \-`-=====-´-/")
      print("              _|   .=.   |_")
      print("             ((|  {{X}}  |))")
      print("              \|   /|\   |/")
      print("               \__ '`' __/")
      print("                 _`) (`_")
      print("               _/_______\_")
      print("              /___________\ ")
      break

    elif st == 0:
      print("\n\n      = = = = = = = = = = = = = = =")
      print("                  Velha!")
      print("      = = = = = = = = = = = = = = =")
      print()   
      print("                    .-.")
      print('                  ,-"""-,')
      print("                 / \__   \ ")
      print("                |  /  `\  |")
      print("                \(  ^.^  )/")
      print("                  \  -  /")
      print("               .-'|;---;|-.")
      print("              /   ||___||  `\ ")
      break

game()