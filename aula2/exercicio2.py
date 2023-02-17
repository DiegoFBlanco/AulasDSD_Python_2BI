peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

if imc <= 18.5:

    print("Magreza")

elif imc > 18.5 and imc <= 24.9:

    print("Normal")

elif imc > 24.9 and imc <= 29.9:

    print("Sobrepeso")

elif imc > 29.9 and imc <= 34.9:

    print("Obesidade grau I")

elif imc > 34.9 and imc <= 39.9:

    print("Obesidade grau II")

elif imc > 39.9:

    print("Obesidade grau III")





