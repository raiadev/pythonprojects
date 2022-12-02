def calculadora(n1, n2, operacao):
    if operacao == 1:
        res = n1 + n2
    elif operacao == 2:
        res = n1 - n2
    elif operacao == 3:
        res = n1 * n2
    elif operacao == 4:
        res = n1 / n2
    else:
        res = 0
    print(res)

# Para soma
calculadora(10,5,1)
# Para subtração
calculadora (10,5,2)
#Para multiplicação
calculadora(10,5,3)
# Para divisão
calculadora (10,5,4)
# Testando calculadora, colocando um valor de operação diferente dos estabelecidos
calculadora (10,5,5)



