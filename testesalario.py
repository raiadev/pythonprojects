def salariodiario():
    teste = "sim"
    while teste == "sim":
     print("----------------------------------------------------------------------------------------------------")
     print("O programa está inicializando. Aguarde.")

     import time
     i = 0

     for i in range(3,0,-1):
         time.sleep(1)
         print(i,"...")

     if  i == 1:
         diastrabalhados = int(input('Digite a quantidade de dias trabalhados por mês:'))

         horasdia = int(input('Digite a quantidade de horas trabalhadas por dia:'))

         salario = float(input('Digite o valor do seu salário:'))

         horasmes = diastrabalhados * horasdia
         ganho_por_hora = salario/horasmes

         print("Você ganha", ganho_por_hora, "por hora de trabalho")






salariodiario()






