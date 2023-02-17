#comentário de uma linha

"""
São comentários
de
múltiplas
linhas
"""

# Trabalhando com dados e variáveis
"""
x = 6# int()
print(x, type(x))
x = "Edson"# str()
print(x, type(x))
x = 7464.85
print(x, type(x))
x = True # bool()
print(x, type(x))
"""

#casting
"""
conteudo = "45"
conteudo = int(conteudo)
print(conteudo, type(conteudo))
conteudo = float(conteudo)
outra_variavel = int(conteudo)
print(conteudo, type(conteudo))
conteudo = bool(conteudo)
print(conteudo, type(conteudo))

"""

# Saída de dados - print()

"""
print("Oi Python")
idade = 48
peso = 85.45
"""

# exemplo com vírgula

"""
print(idade, peso)
print("Eu tenho ", idade, "anos e peso", peso)
"""

#exemplo com +

"""
print("Eu tenho"+ str(idade)+"anos e peso"+ str(peso))
print(type, (idade), type(peso))
"""

# utilizando .format

"""
print("Eu tenho {} anos e peso {}".format(idade,peso))
print("Eu tenho {1} anos e peso {0}".format(idade,peso))
print("Eu tenho {0} anos e peso {0}".format(idade,peso))
print("Eu tenho {id} anos e peso {p}".format(id = idade, p = peso))
print("Eu tenho {id:7d} anos e peso {p:10.1f}".format(id = idade, p = peso))
valor_decimal = 20
print("o valor decimal {0} equivale a\n{0:o} em octal\n{0:x} em hexadecimal"
      .format(valor_decimal))
"""

# utilizando o print'f

"""
quantidade = 4
salario = 3456.56
print(f"Quantidade = {quantidade:5d}\nSalário  = R$  {salario: .2f}")
print("primeira linha", end='!')
print("segunda linha")
"""

"""
Exercício: crie um registro como o abaixo, mas com os seus dados
Nome......: Edson de Oliveira
Salário...: R$ 50000.00
Filhos....:           2
Idade.....:          48
"""

#operadores aritméticos

"""
valor1 = 17.4
valor2 = 7.6
resp = valor1 + valor2
print(resp)
resp = valor1 * valor2
print(resp)
resp = valor1 / valor2
print(resp)
resp = valor1 ** valor2 # exponenciação
print(resp)
resp = valor1 // valor2 # divisão inteira
print(resp)
resp = valor1 % valor2
print(resp)
"""

# Entrada de dados - input()
"""
v1 = float(input("Digite o valor 1: ")) # input só lê string
v2 = float(input("Digite o valor 2: "))

resp = v1 + v2
print(resp)
"""