print('######################')
print('Bem vindo ao jogo de adivinhacao')
print('######################')

numero_secreto = 42
total_tentativas = 3
rodada = 1

while rodada <= total_tentativas:
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute_str = input("Digite o seu numero:")
    print('Você Digitou:', chute_str)

    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você Acertou")
    else:
        if maior:
            print("Você Errou! O Seu chute foi maior do que o número secreto")
        elif menor:
            print("Você Errou! O Seu chute foi menor do que o número secreto")

    rodada = rodada + 1

print("Fim do Jogo")