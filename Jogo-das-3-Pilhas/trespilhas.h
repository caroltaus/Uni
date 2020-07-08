//arquivo trespilhas.h (definição da classe)

#include <iostream>
using namespace std;
#define tam 10


#ifndef TRESPILHAS_H   //if not defined
#define TRESPILHAS_H

class TadPilha{

	private:  //acessiveis só dentro da classe
		int vetor[tam];
    int topo;
     
				
	public:
		TadPilha();
		bool push(int n);     //push
		bool pop();           //pop
		void imprimir(); 
		bool vazia();
		bool cheia();
    bool top(int &item);
    bool ganhou1();
    bool ganhou2();
    		
	
};

#endif