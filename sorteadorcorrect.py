import random
#função random chamada para criar um array aleatório de números inteiros (random.randint)



def sorteio():

    x = random.randint(0, 100)
    print("**************************************************")
    print("Será que você está com sorte hoje?")
    import time
    t = 0
    for t in range (1,0,-1):
        time.sleep(1)
        print("___________________________________________________________")
        print("Vamos iniciar o sorteio!")
        time.sleep(1)
        print("___________________________________________________________")
        numescolhido = int(input('Digite um número de 0 a 100:'))
        i = 0
    for i in range(1, 0, -1):
        time.sleep(1)
        print("Sorteando...")
        time.sleep(2)
        print("Aguarde...")
        time.sleep(2)
        print("Pronto!")
        time.sleep(1)

    if numescolhido == x:
        print("___________________________________________________________")
        print("Parabéns! Você acertou! O número sorteado foi ", x,"e você escolheu o número", numescolhido,".")
    else:
        print("___________________________________________________________")
        print("Você não acertou. Tente novamente! O número sorteado foi ", x,"e você escolheu o número", numescolhido,".")




start = "true"
while start == "true" :
  sorteio()