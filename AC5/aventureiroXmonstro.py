from random import randint

def main():
#atributos aventureiro
    vida_aventureiro = 100
    atq_aventureiro = randint(10,20)
    defesa = randint(1,5)
#atributos monstro
    vida_monstro = randint(60,80)
    atq_monstro = randint(20,30)
#atributos iniciais
    print("Aventureiro: Vida = ",vida_aventureiro,"- Ataque = ",atq_aventureiro,"- Defesa = ",defesa)
    print("Monstro: Vida =",vida_monstro,"Ataque =",atq_monstro)

    rodada = 1
    while vida_aventureiro > 0 and vida_monstro > 0:
        print("\nRodada:",rodada)
        rodada = rodada + 1


#Aventureiro Ataque
        dano_aventureiro =  randint(1,atq_aventureiro)
        vida_monstro = vida_monstro - dano_aventureiro

#Monstro Ataque
        dano_monstro =  randint(1,atq_monstro) - defesa
        vida_aventureiro = vida_aventureiro - dano_monstro

        if vida_aventureiro <= 0:
            print("O Aventureiro MORREU!!!")
            break


        if vida_monstro <= 0:
            print("O Monstro MORREU!!!")
            break



        print(f"Aventureiro: Vida = ",vida_aventureiro,"- Ataque = ",atq_aventureiro,"- Defesa = ",defesa)
        print(f"Monstro: Vida =",vida_monstro,"Ataque =",atq_monstro)


main()