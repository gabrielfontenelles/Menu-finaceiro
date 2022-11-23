import os
def opcao1():
  salario = float(input("Escreva salario"))
  if salario <500:
    print(f"O imposto é igual  R${salario*0.05}")
  if salario == 500 and salario <=850:
    print(f"O imposto é igual  R${salario*0.10}")
  if salario >850:
    print(f"O imposto é igual R${salario*0.15}")
  input("Digite qualquer tecla para continuar")
def opcao2():
     salario = float(input("Escreva salario"))
     if salario < 450:
         print(f"O novo salário é {salario + 100}")
     elif salario == 450 or salario <= 750:
         print(f"O novo salário é {salario + 75}")
     elif salario == 500 or salario <= 1500:
         print(f"O novo salário é {salario + 50}")
     elif salario > 1500:
         print(f"O novo salário é {salario + 25}")
     input("Digite qualquer tecla para continuar")
def opcao3():
    salario = float(input("Escreva salario"))
    if salario <= 700:
        print("Você é mal remunerado")
    else:
        print("Você é bem remunerado")
    input("Digite qualquer tecla para continuar")
def opcao4():
                             print("Encerrar execução do programa")
op =0
while (op != 4):
      os.system("cls")
      print("MENU")
      print("1 - Imposto")
      print("2 - Novo Salário")
      print("3 - Classificação")
      print("4 - Sair")
      op = int(input("Digite a opção desejada"))
      if op == 1:
          opcao1()
      if op == 2:
         opcao2()
      if op == 3:
          opcao3()
      if op == 4:
          opcao4()







