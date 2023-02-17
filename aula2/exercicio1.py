salario = float(input("Digite o seu salário: "))

desconto = salario * 0.11

if desconto > 877:

   desconto = 877


salariofinal = salario - desconto

print("Salário: R$ {}".format(salario))
print("Desconto: R$ {}".format(desconto))
print("Salário final: R$ {}".format(salariofinal))
