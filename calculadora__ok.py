def calculadora():
    ficar = "sim"
    while ficar == "sim":
        print("Iniciando calculadora...")
        import time
        i = 0
        for i in range(2, 0, -1):
            time.sleep(1)
        if i == 1:
            print ("-------------------------------------------------------")
            print("Digite a operação:  --->>>> [1] - Soma / [2] - Subtração / [3] - Multiplicação / [4] - Divisão/ [0] - Sair")
        operacao = int(input())
        while (operacao != 0) and (operacao != 1) and (operacao != 2) and (operacao != 3) and (operacao != 4):
            print("Entrada inválida! :(  ")
            print ("-------------------------------------------------------")
            print("Tente novamente!")
            print ("-------------------------------------------------------")
            print("Voltando ao menu inicial...Aguarde!")
            import time
            i = 0
            for i in range(2, 0, -1):
                time.sleep(1)
            if i == 1:
                print("-------------------------------------------------------")
                print(
                    "Digite a operação: [1] - Soma / [2] - Subtração / [3] - Multiplicação / [4] - Divisão/ [0] - Sair")
            operacao = int(input())
        if (operacao == 0):
            print("Saindo...")
            import time
            i = 0
            for i in range(2, 0, -1):
                time.sleep(1)
            if (i == 1):
                print("-------------------------------------------------------")

                print("    Finalizado com sucesso! ;)      ")
            break

        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
        som = num1 + num2
        sub = num1 - num2
        mult = num1 * num2
        div = num1 / num2

        if (operacao == 1):
            print("Resultado: ", som)
        elif (operacao == 2):
            print("Resultado: ", sub)
        elif (operacao == 3):
            print("Resultado: ", mult)
        elif (operacao == 4):
            print(" = ", div)



calculadora()
