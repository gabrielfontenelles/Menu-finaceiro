import os
def opcao1(salario: float) -> None:
  if salario <500:
    print(f"O imposto é igual  R${(salario*0.05):.2f} equivalente a 5% do seu salário")
  if salario == 500 and salario <=850:
    print(f"O imposto é igual  R${(salario*0.10):.2f} equivalente a 10% do seu salário")
  if salario >850:
    print(f"O imposto é igual R${(salario*0.15):.2f} equivalente a 15% do seu salário")
  input("Digite qualquer tecla para continuar")
def opcao2(salario: float) -> None:
     if salario < 450:
         print(f"O novo salário é R${(salario + 100):.2f}")
     elif salario == 450 or salario <= 750:
         print(f"O novo salário é R${(salario + 75):.2f}")
     elif salario == 500 or salario <= 1500:
         print(f"O novo salário é R${(salario + 50):.2f}")
     elif salario > 1500:
         print(f"O novo salário é R${(salario + 25):.2f}")
     input("Digite qualquer tecla para continuar")
def opcao3(salario: float) -> None:
    if salario <= 700:
        print("Você é mal remunerado")
    else:
        print("Você é bem remunerado")
    input("Digite qualquer tecla para continuar")
def opcao4() -> None:
                             print("Encerrar execução do programa")
op =0
while (True):
      os.system("cls")
      salario: float = float(input("Escreva o salário: "))
      os.system("cls")
      print("MENU")
      print("Imposto")
      print("Novo Salário")
      print("Classificação")
      print("Sair")
      op = input("Digite a opção desejada: ")
      if op == 'Imposto':
          opcao1(salario)
      elif op == 'Novo salário':
         opcao2(salario)
      elif op == 'Classificação':
          opcao3(salario)
      else:
        opcao4()
        break
      

