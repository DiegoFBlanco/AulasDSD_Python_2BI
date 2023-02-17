salario = float(input("Digite seu salário: "))

if salario <= 1903.98:

    aliquota = 0

    print(f"Salário = R$ ", salario,f"e Alíquota = R${aliquota:.2f}")

elif salario > 1903.99 and  salario <= 2826.65:

    aliquota = salario * 0.075

    print(f"Salário = R$ ", salario,f"e Alíquota = R${aliquota:.2f}")

elif salario > 2826.65 and salario <= 3751.05:

    aliquota = salario * 0.15

    print(f"Salário = R$ ", salario,f"e Alíquota = R${aliquota:.2f}")

elif salario > 3751.05  and salario <= 4664.68:

    aliquota = salario * 0.225

    print(f"Salário = R$ ", salario,f"e Alíquota = R${aliquota:.2f}")