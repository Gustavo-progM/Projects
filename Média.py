print("Boa tarde, qual seu nome?")

nmaluno = input()

print("Vc recebeu dispensa escolar?")

dispensa = input()

while dispensa != "sim" and dispensa != "nao":

    print("resposta invalida, digite sim ou nao")

    dispensa = input()

if dispensa == "sim":

    dispensa = "Sim"

    print("Rapaz tu é zica, vc está automaticamente aprovado")

else:

    if dispensa == "nao":

        dispensa = "Nao"

        print("Que pena, então vamos lá")

    print("Qual foi a sua frequencia escolar?")

    diasaula = int(input())

    while diasaula < 0 or diasaula > 100:

        print("Coloque a frequencia certa, POR GENTILEZA")

        diasaula = int(input())

    if diasaula >= 75:

        print("ok")

        print("Olá," + nmaluno + " qual foi a sua primeira nota?")

        nota4 = float(input())

        while nota4 < 0 or nota4 > 10:

            print("Nota inválida, por favor digite a nota correta")

            nota4 = float(input())

        print("E sua segunda nota?")

        nota5 = float(input())

        while nota5 < 0 or nota5 > 10:

            print("Nota inválida, por favor digite a nota correta")

            nota5 = float(input())

        print("E a terceira nota?")

        nota6 = float(input())

        while nota6 < 0 or nota6 > 10:

            print("Nota inválida, por favor digite a nota correta")

            nota6 = float(input())

        média = nota4 + nota5 + nota6 / 3

        print("sua média é =" +str(média))

        if média < 4:

            print("REPROVADO!!!")

        if média >= 4 and média < 7:

            print("VAI PRA RECUPERAÇÃO!!!")

        if média > 7:

            print("APROVADOOO!!!")

        print("Sua média foi: " + str(média) + ",sua frequência: " + str(diasaula))

    else:

        if diasaula < 75:

            print("Meus parabéns turista vc foi reprovadooo")
