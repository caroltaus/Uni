#include "trespilhas.h"

// construtor do tadpilha
TadPilha::TadPilha() {
  topo = -1;  //no começo a pilha está vazia
  
}

// verificação de pilha cheia

bool TadPilha::cheia(){
  if (topo+1 >= tam) {return true;} 
  return false;
}

// verificação de pilha vazia

bool TadPilha::vazia(){
  if (topo == -1) {return true;}
  else {return false;}
}

// opc 1 - PUSH na Pilha 

bool TadPilha::push(int n){
  if (cheia()==true) {return false;}
  else { 
  vetor[topo+1] = n;
  ++topo;
  return true;}
}

//----------POP
bool TadPilha::pop(){
  if (vazia() == true){return false;}
  else{
    --topo;
    return true;
  }
}

// opc 3 - Imprimir
void TadPilha::imprimir(){
  int i;
  for (i=0;i<=topo;i++) {cout << vetor[i]<< "  ";}
}


// ------- TOP --------

bool TadPilha::top(int &item){
  if (vazia()==true) return false;
  else item = vetor[topo];
  return true;
}

// -------- CHECAR SE GANHOU CRESCENTE------
bool TadPilha::ganhou1(){
  if (cheia()==false) return false; // para ganhar a pilha deve estar cheia
  else{
    int cont=0;
    for (int i=0; i<(tam-1); i++){    // verificando ordem
      if (vetor[i] <= vetor[i+1]) {cont++;}
      else {return false;}
    }
    if (cont == (tam-1)) return true;
    else return false;
  }
}

// -------- CHECAR SE GANHOU DECRESCENTE-----

bool TadPilha::ganhou2(){
  if (cheia()==false) return false; // para ganhar a pilha deve estar cheia
  else{
    int cont=0;
    for (int i=0; i<(tam-1); i++){    // verificando ordem
      if (vetor[i] >= vetor[i+1]) {cont++;}
      else {return false;}
    }
    if (cont == (tam-1)) return true;
    else return false;
  }
}




