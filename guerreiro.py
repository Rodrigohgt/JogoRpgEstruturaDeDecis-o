def iniciar():

    print("****************************************************")
    print("Iniciando jogo classe com classe guerreiro.")
    print("****************************************************")
    print("****************************************************")
    nome = str(input("Qual o nome do seu Guerreiro? "))
    print("Seja bem vindo ao mundo de Elyah {}".format(nome))
    print("iniciando jogo...")
    print("****************************************************")
    print("****************************************************")
    print("Atualmente você está na cidade de Elyah")
    print("caminhando normalmente na avida principal, você sabe que hoje tera um grande anuncio do Rei para as Guildas")

    #decisão 1
    print("O que você gostaria de fazer?")
    num_invalido = True
    while(num_invalido):
        descisao01 = int(input("Olhar equipamentos {1} Encontrar uma Taverna {2} Encontrar algum comerciante {3} Seguir ate o local do anuncio {4}"))
        if(descisao01 == 1):
            print("Você tem uma poção de cura, uma espada reta simples, e um escudo")
            break
        elif(descisao01 == 2):
            print("Você avista uma taverna de esquina com a proxima curva")
            break
        elif(descisao01 == 3):
            print("Você avista alguns comerciantes no meio da avenida")
            break
        elif(descisao01 == 4):
            print("Você segue reto para o local do anuncio")
            break
        else:
            print("insira uma numeração validaa")

if(__name__ == "__main__"):
    iniciar()
    