import guerreiro
import mago
import arqueiro

def iniciar_jogo():
    tente_novamente = True

    while(tente_novamente):
        
        classe = int(input("iniciando jogo, Escolha sua classe: Guerreiro {1} Mago {2} Arqueiro {3}"))
        
        if(classe == 1):
            guerreiro.iniciar()
    
            break
        elif(classe == 2):
            mago.iniciar()
            break
        elif(classe == 3):
            arqueiro.iniciar()
            break
        else:
            x = int(input("informação invalida, tentar novamente {1} Fechar jogo {2}"))
            if(x == 1):
                if(tente_novamente):
                    print("tente novamente")
                    continue
            else:
                print("jogo cancela")
                break
            

if(__name__ == "__main__"):
    iniciar_jogo()
    