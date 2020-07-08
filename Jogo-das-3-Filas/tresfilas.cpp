#include "tresfilas.h"

// ----------- CONSTRUTOR --------------
TadFila::TadFila(){
  contador = 0;
  inicio = 0;
  fim = tam -1;
}

// ----------- VAZIA --------------
bool TadFila::vazia(){
  if(contador == 0)
    return true;
  else
    return false;
}

// ----------- CHEIA --------------
bool TadFila::cheia(){
  if(contador==tam)
    return true;
  else
    return false;
}

// ----------- INSERIR --------------
bool TadFila::inserir(int item){
  if(cheia()==true)
    return false; //overflow

  if(fim==tam-1)  //se fim estiver na ultima posição
    fim = 0;  // novo fim é no indice 0
    // em vez desse if poderia usar mod: fim = (fim+1) % tam
  else
    fim++;
  numeros[fim]=item;
  contador++;
  return true;
}

// ----------- EXTRAIR --------------
bool TadFila::extrair(){
  if(vazia()==true)
    return false; //underflow
  if(inicio==tam-1) //se inicio estiver na ultima poisição volta pra 0
    inicio = 0;  // ou: inicio = (inicio+1) % tam
  else
    inicio++;
  contador--;
  return true;

}

// ----------- CONSULTA --------------
bool TadFila::consulta(int &item){ //valor do inicio da fila é passado poor referencia
  if(vazia()==true)
    return false;//underflow
  item = numeros[inicio];
  return true;
}

// ----------- IMPRIMIR --------------
void TadFila::imprimir(){
  TadFila aux;
  int item;
  while (vazia()==false){  
    consulta(item);
    cout << item << "  ";
    aux.inserir(item);
    extrair();
  }

  while (aux.vazia()==false){
    aux.consulta(item);
    inserir(item);
    aux.extrair();

  }
}

// ----------- QUANTIDADE --------------
int TadFila::quantidade(){
  return contador;
}

// -------- CHECAR SE GANHOU CRESCENTE------
bool TadFila::ganhou1(){
  TadFila Faux;
  int x,y=101,cont = 0;
  if (cheia()==false) return false; // para ganhar a fila deve estar cheia
  else{
    while (!vazia()){    
      consulta(x);
      if (x<=y) cont++;
      y = x;
      Faux.inserir(x);
      extrair();
    }
    while (!Faux.vazia()){    //voltando elementos da fila aux pra fila original
      Faux.consulta(x);
      inserir(x);
      Faux.extrair();
    }
    if (cont == quantidade()) return true;
    else return false;
  }
}

// -------- CHECAR SE GANHOU DECRESCENTE-----

bool TadFila::ganhou2(){
  TadFila Faux;
  int x,y=0,cont = 0;
  if (cheia()==false) return false; // para ganhar a fila deve estar cheia
  else{
    while (!vazia()){    
      consulta(x);
      if (x>=y) cont++;
      y = x;
      Faux.inserir(x);
      extrair();
    }
    while (!Faux.vazia()){    //voltando elementos da fila aux pra fila original
      Faux.consulta(x);
      inserir(x);
      Faux.extrair();
    }
    if (cont == quantidade()) return true;
    else return false;
  }
}




