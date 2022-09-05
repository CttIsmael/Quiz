#Primeiro desafio - Criar um Quiz e imprimir o total de pontuação acertado no final.

print("No Python, como se chama uma 'caixa' usada para armazenar dados?")

score = 0

respostas = input().lower()

if respostas == "variavel":
    score = score + 1
    print("Acertou")
else:
    print("Errou")

print("Nome da operação que cria instruções nativas (built-ins) para armazenar texto?")

respostas = input().lower()

if respostas == "string":
    score = score + 1
    print("Acertou")
else:
    print("Errou ")

print(f"Obrigado por jogar! pontuação: {score}")
