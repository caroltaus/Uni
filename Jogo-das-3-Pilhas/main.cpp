// Autora: Caroline Taus

// arquivo main.cpp
#include "trespilhas.h"
using namespace std;

int main(){

	TadPilha p1,p2,p3;
  int rand (void),jogadas=0; 
  while (p1.cheia()==false) {p1.push(rand() % 100 + 1);}

  cout << "\nO Jogo das Tres Pilhas tem como objetivo organizar os números em ordem crescente ou decrescente no menos número de jogadas possíveis. Boa sorte!\n";
  
	while(true){

    cout <<"\n * Pilha 1: "; p1.imprimir();
    cout <<"\n * Pilha 2: "; p2.imprimir();
    cout <<"\n * Pilha 3: "; p3.imprimir();
		
    cout << "\n\n   -------------------------------------";
		cout << "\n  |                  MENU               |";
		cout << "\n  |-------------------------------------|";
    cout << "\n  |                                     |  ";
		cout << "\n  |          * 0 - Sair do jogo         |";
		cout << "\n  |          * 1 - Movimentar           |";
    cout << "\n  |                                     |  ";
    cout << "\n   --------------------------------------";
		cout << "\n\nInformar a opcao: ";
		int opc;
		cin >> opc;

    // ====== OPC SAIR DO JOGO ======
    if (opc == 0){
      cout << "\nbye bye! ^_____^\n";
      break;
    }
    
    // ====== OPC MOVIMENTAR ======
    else if (opc ==1){
      cout << "\nDe qual pilha deseja extrair (1, 2 ou 3)?\n";
      int p,r,x;  
      cin >> p;
      
      // ====== EXTRAIR DA P1 ======
      if (p == 1) {
        p1.top(x);
        if(p1.vazia()==false) {  //extrair da P1
          p1.pop();
          jogadas++;
          cout << "\nPara qual pilha deseja movimentar o valor (2 ou 3)?\n";
          cin >> r;
          while (r != 2 && r!=3) {
            cout << "\nPara qual pilha deseja movimentar o valor (2 ou 3)?\n";
            cin >> r;
          }
          if (r == 2) {p2.push(x);}
          else if (r == 3) {p3.push(x);}}
        else {cout << "\nPilha vazia. Impossível extrair.\n";}
      }

      // ====== EXTRAIR DA P2 ======
      else if (p == 2) {       
        p2.top(x);
        if(p2.vazia()==false) {
            p2.pop();
            jogadas++;
            cout << "\nPara qual pilha deseja movimentar o valor (1 ou 3)?\n";
            cin >> r;
            while (r != 1 && r!=3) {
            cout << "\nPara qual pilha deseja movimentar o valor (1 ou 3)?\n";
            cin >> r;
          }
            if (r == 1) {p1.push(x);}
            else if (r == 3) {p3.push(x);}}
        else {cout << "\nPilha vazia. Impossível extrair.\n";}
      }

      // ====== EXTRAIR DA P3 ======
      else if (p == 3) {       
        p3.top(x);
        if(p3.vazia()==false) {
          p3.pop();
          jogadas++;
          cout << "\nPara qual pilha deseja movimentar o valor (1 ou 2)?\n";
          cin >> r;
          while (r != 1 && r!=2) {
            cout << "\nPara qual pilha deseja movimentar o valor (1 ou 2)?\n";
            cin >> r;
          }
          if (r == 1) {p1.push(x);}
          else if (r == 2) {p2.push(x);}}
        else {cout << "\nPilha vazia. Impossível extrair.\n";}
        }
       
      // ====== CHECANDO VITÓRIA ======
      if (p1.ganhou1() || p2.ganhou1() || p3.ganhou1() || p1.ganhou2() || p2.ganhou2() || p3.ganhou2()) {
        cout << "\n\n       FIM!!!!!!!\n\nVocê ganhou com " << jogadas<< " jogadas!\n\n";
        cout<<"     ___________\n";
        cout<<"    '._==_==_=_.'\n";
        cout<<"    .-\\:      /-.\n";
        cout<<"   | (|:.     |) |\n";
        cout<<"    '-|:.     |-'\n";
        cout<<"      \\::.    /\n";
        cout<<"       '::. .'\n";
        cout<<"         ) (\n";
        cout<<"       _.' '._\n";
        cout<<"       ```````\n\n";
        


      // ====== JOGAR NOVAMENTE ======
        cout <<"\nDeseja jogar de novo? Insira 1 para SIM e 0 para NÃO.\n";
        int jn;
        cin >> jn;
        while (jn != 1 && jn != 0){
          cout <<"\nDeseja jogar de novo? Insira 1 para SIM e 0 para NÃO.\n";
          cin >> jn;
        }
        if (jn == 1) {main();}
        else if (jn == 0) {cout << "\nbye bye! ^_____^\n"; break;}
      }
      
    

      }
    } 
    return 0;
  }
