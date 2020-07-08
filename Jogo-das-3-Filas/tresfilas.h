#include <iostream>
using namespace std;

#ifndef TRESFILAS_H
#define TRESFILAS_H
#define tam 10

class TadFila {
  private:
    int numeros[tam];
    int inicio;
    int fim;
    int contador;

  public:
    TadFila();
    bool inserir(int n);
    bool extrair();
    void imprimir();
    bool cheia();
    bool vazia();
    bool consulta(int &item);
    int quantidade();
    bool ganhou1();
    bool ganhou2();

};
#endif