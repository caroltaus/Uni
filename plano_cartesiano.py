# Autoras: Caroline Taus e Rebecca Mello

# entrada da origem e número de pontos a serem lidos
print('Digite o valor da origem do seu plano cartesiano:')
x = int(input('Abscissa (eixo x): '))
y = int(input('Ordenada (eixo y): '))
n = int(input('Indique a quantidade de pontos: '))

# declarações iniciais das variáveis
primeiro,segundo,terceiro,quarto,dist_maior,ponto_maior_x,ponto_maior_y,ponto_menor_x,ponto_menor_y = 0,0,0,0,0,0,0,0,0
dist_menor = 1000 

# função de determinação da distância
def distancia():
  import math
  global dist_maior,dist_menor,ponto_maior_x,ponto_maior_y,ponto_menor_x,ponto_menor_y
   
  # fórmula da distancia de um ponto até a origem
  dist = math.sqrt(((y - orde) ** 2)  + ((x - absc) ** 2))
  
  if dist > dist_maior:
    dist_maior = dist 
    ponto_maior_x = absc
    ponto_maior_y = orde
    
  if dist < dist_menor:
    dist_menor = dist
    ponto_menor_x = absc
    ponto_menor_y = orde

# entrada do X e Y de cada ponto 
for i in range(1, n+1):
  print('\n\nInforme o valor da abscissa', i, ':')
  absc = int(input())
  print('Informe o valor da ordenada', i, ':')
  orde = int(input())

  # determinação do quadrante de cada ponto
  if (absc > x) and (orde > y):
    print('Ponto (',absc,',',orde,') está no 1o quadrante.')
    primeiro = primeiro + 1

  elif (absc < x) and (orde > y):
    print('Ponto (',absc,',',orde,') está no 2o quadrante.')
    segundo = segundo + 1

  elif (absc < x) and (orde < y):
    print('Ponto (',absc,',',orde,') está no 3o quadrante.')
    terceiro = terceiro + 1
  
  elif (absc > x) and (orde < y):
    print('Ponto (',absc,',',orde,') está no 4o quadrante.')
    quarto = quarto + 1

  else:
    print('Ponto (',absc,',',orde,') esta na origem.')

  distancia() #chamada da função de distância dentro do 'for' para que todos o pontos sejam considerados nos cálculos


# print de resultados da distância
print('\n\nPonto (', ponto_menor_x, ',', ponto_menor_y,') eh o mais proximo, distancia =', format(dist_menor, '.2f'))
print('Ponto (', ponto_maior_x, ',',ponto_maior_y,') eh o mais distante, distancia =', format(dist_maior, '.2f'))
  
# funções para determinar a porcentagem de pontos por quadrante
def percentual1():
  conta1 = (primeiro * 100) / n
  return conta1
def percentual2():
  conta2 = (segundo * 100) / n
  return conta2
def percentual3():
  conta3 = (terceiro * 100) / n
  return conta3
def percentual4():
  conta4 = (quarto * 100) / n
  return conta4

# resultados de poncentagens
print('\n\nPorcentagem de pontos no 1o quadrante', percentual1(), '%.')
print('Porcentagem de pontos no 2o quadrante', percentual2(), '%.')
print('Porcentagem de pontos no 3o quadrante', percentual3(), '%.') 
print('Porcentagem de pontos no 4o quadrante', percentual4(), '%.')

