// Autora: Caroline Taus

// arquivo main.cpp
#include "tresfilas.h"
using namespace std;

int main(){

	TadFila F1,F2,F3;
  int rand (void),jogadas=0; 
  while (F1.cheia()==false) {F1.inserir(rand() % 100 + 1);}

  cout << "\nO Jogo das Tres Filas tem como objetivo organizar os números em ordem crescente ou decrescente no menos número de jogadas possíveis. Boa sorte!\n";
  
	while(true){

    cout <<"\n * Fila 1: "; F1.imprimir();
    cout <<"\n * Fila 2: "; F2.imprimir();
    cout <<"\n * Fila 3: "; F3.imprimir();
		
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
      cout << "\nDe qual fila deseja extrair (1, 2 ou 3)?\n";
      int p,r,x;  
      cin >> p;
      
      // ====== EXTRAIR DA P1 ======
      if (p == 1) {
        F1.consulta(x);
        if(F1.vazia()==false) {  //extrair da P1
          F1.extrair();
          jogadas++;
          cout << "\nPara qual fila deseja movimentar o valor (2 ou 3)?\n";
          cin >> r;
          while (r != 2 && r!=3) {
            cout << "\nPara qual fila deseja movimentar o valor (2 ou 3)?\n";
            cin >> r;
          }
          if (r == 2) {F2.inserir(x);}
          else if (r == 3) {F3.inserir(x);}}
        else {cout << "\nFila vazia. Impossível extrair.\n";}
      }

      // ====== EXTRAIR DA P2 ======
      else if (p == 2) {       
        F2.consulta(x);
        if(F2.vazia()==false) {
            F2.extrair();
            jogadas++;
            cout << "\nPara qual fila deseja movimentar o valor (1 ou 3)?\n";
            cin >> r;
            while (r != 1 && r!=3) {
            cout << "\nPara qual fila deseja movimentar o valor (1 ou 3)?\n";
            cin >> r;
          }
            if (r == 1) {F1.inserir(x);}
            else if (r == 3) {F3.inserir(x);}}
        else {cout << "\nFila vazia. Impossível extrair.\n";}
      }

      // ====== EXTRAIR DA P3 ======
      else if (p == 3) {       
        F3.consulta(x);
        if(F3.vazia()==false) {
          F3.extrair();
          jogadas++;
          cout << "\nPara qual fila deseja movimentar o valor (1 ou 2)?\n";
          cin >> r;
          while (r != 1 && r!=2) {
            cout << "\nPara qual fila deseja movimentar o valor (1 ou 2)?\n";
            cin >> r;
          }
          if (r == 1) {F1.inserir(x);}
          else if (r == 2) {F2.inserir(x);}}
        else {cout << "\nFila vazia. Impossível extrair.\n";}
        }
       
      // ====== CHECANDO VITÓRIA ======
      if (F1.ganhou1() || F2.ganhou1() || F3.ganhou1() || F1.ganhou2() || F2.ganhou2() || F3.ganhou2()) {
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
