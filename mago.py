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
    vida = int(30)
    gold = float(70)
    espada_reta = int(15)
    escudo = int(15)

    while(num_invalido):
        descisao01 = int(input("Olhar equipamentos {1} Encontrar uma Taverna {2} Encontrar algum comerciante {3} Seguir ate o local do anuncio {4}"))

        if(descisao01 == 1):
            print("Você tem uma poção de cura, uma espada reta simples, um escudo e {} moedas de GOLD".format(gold))
            print("Você gostaria de fazer algo a mais")
            
            while(num_invalido):
                descisao02 = int(input("Ir para Taverna {1} Procurar comerciante {2} Seguir para local de anuncio {3}"))
                if(descisao02 == 1):
                    print("Você avista uma taverna de esquina com a proxima curva")
                    print("A taverna parece estar bem movimentada, muitas pessoas estão em volta dela")
                    print("Gostaria de ir ate a Taverna")
                    sim_nao = str(input("Sim {s} Não {n}"))
                    if(sim_nao == "s"):
                        print("Voce vai ate a Taverna")
                        print("Ao chegar perto você encontra um grupo de bebados brigando")
                        print("Gostaria de interferir ?")
                        sim_nao = str(input("Sim {s} Não {n}"))
                        if(sim_nao == "s"):
                            print("Você chega para separar a luta")
                            print("um dos bebados termina de desmair o outro e olha para voce e diz: ")
                            print("(Quer apanhar também ? eu vou matar você por se meter onde não é chamado)")
                            print("O que você faz ?")
                            descisao04 = int(input("sacar escudo e espada e lutar {1} Fugir {2}"))
                            if(descisao04 == 1):
                                print("O bebado parte para cima de você")
                                descisao05 = int(input("contra-ataquar com espada {1} defender {2}"))
                                if(descisao05 == 1):
                                    print("Você revida o ataque dando {} de dano ".format(20 - espada_reta))
                                    print("Apos revida com um corte o bebado fica no chão implorando pela vida")
                                elif(descisao05 == 2):
                                    print("Você apenas defende o soco dele com o escudo, anulando o dano")
                                else:
                                    print("Insira um valor valido")

                            elif(descisao04 == 2):
                                print("Você começa a correr para longe")
                            else:
                                print("Insira um valor valido")

                        elif(sim_nao == "n"):
                            print("Você ignora a luta e entra dentro da taverna")
                        else:
                            print("Insira um valor valido")

                    elif(sim_nao == "n"):
                        print("Você desiste de ir ate Taverna")
                        print("o que você gostaria de fazer agora?")
                        descisao03 = int(input("Procurar comerciante {1} Seguir para local de anuncio {2}"))
                        if(descisao03 == 1):
                            print("Você avista alguns comerciantes no meio da avenida")
                        elif(descisao03 == 2):
                            print("Você segue reto para o local do anuncio")
                        else:
                            print("Insira um valor val")
                    else:
                        print("Insira um valor valido")

                elif(descisao02 == 2):
                    print("Você avista alguns comerciantes no meio da avenida")
                    
                elif(descisao02 == 3):
                    print("Você segue reto para o local do anuncio")
                    
                else:
                    print("insira uma numeração valida")
                
        elif(descisao01 == 2):          
            print("Você avista uma taverna de esquina com a proxima curva")
            print("A taverna parece estar bem movimentada, muitas pessoas estão em volta dela")
            print("Gostaria de ir ate a Taverna")
            
            break
        elif(descisao01 == 3):
            print("Você avista alguns comerciantes no meio da avenida")
            break
        elif(descisao01 == 4):
            print("Você segue reto para o local do anuncio")
            break
        else:
            print("insira uma numeração valida")

if(__name__ == "__main__"):
    iniciar()