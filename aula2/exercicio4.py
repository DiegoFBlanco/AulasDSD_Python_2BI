nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

nota3 = float(input("Digite a terceira nota: "))

medianotas = (nota1 + nota2 + nota3) / 3

trab1 = float(input("Digite a nota do primeiro trabalho: "))

trab2 = float(input("Digite a nota do segundo trabalho: "))

mediatrabs = (trab1 + trab2) / 2

notaprojeto = float(input("Digite a nota do projeto: "))

mediafinal = ((medianotas * 0.3) + (mediatrabs * 0.3) + (notaprojeto * 0.4))

print("Media final: ", mediafinal)

if mediafinal < 4:
    print("Reprovado sem direito a recuperação")

elif mediafinal >= 4 and mediafinal < 7:
    notarec = float(input("Digite a nota de recuperação: "))
    mediafinal = (mediafinal + notarec) / 2
    print("Media final após recuperação: ", mediafinal)

    if mediafinal >= 6:
        print("Aluno aprovado após recuperação")
    else:
        print("Aluno reprovado")

elif mediafinal >= 7:
    print("Aprovado")



